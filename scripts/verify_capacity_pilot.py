#!/usr/bin/env python3
"""Independently verify the short, real-server pilot of the corrected instrument."""
import argparse
import datetime
import gzip
import hashlib
import json
import pathlib


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False,
        separators=(',', ':')).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--folder', required=True)
    parser.add_argument('--probe', required=True)
    args = parser.parse_args()
    folder = pathlib.Path(args.folder)
    measurement = folder / 'mediciones.json'
    histories_path = folder / 'historiales.json.gz'
    data = json.loads(measurement.read_text())
    summary = data['summary']
    requests = data['requests']
    histories = json.loads(gzip.decompress(histories_path.read_bytes()))['histories']
    probe_hash = hashlib.sha256(pathlib.Path(args.probe).read_bytes()).hexdigest()
    assert summary['script_sha256'] == probe_hash
    assert summary['growth_protocol_version'] == 2
    assert summary['status'] == 'complete' and not summary['growth_stop_reason']
    assert summary['concurrency'] == 2 and summary['server_max_num_seqs'] >= 2
    assert summary['reasoning_mode'] == 'disabled'
    assert summary['growth_targets'] == list(range(512, 8192, 1024)) + [8192]
    assert summary['completed'] == len(requests) == 18
    assert summary['failed'] == summary['not_attempted'] == 0
    assert set(histories) == {'0', '1'}
    for user, history in histories.items():
        own = sorted((r for r in requests if str(r['user_id']) == user),
            key=lambda r: r['turn'])
        assert [r['turn'] for r in own] == list(range(1, 10))
        assert len(history['exchanges']) == 9
        messages = list(history['initial_messages'])
        for index, (record, exchange) in enumerate(zip(own, history['exchanges'])):
            assert record['ok'] and record['has_visible_answer']
            assert record['naturally_finished'] and record['finish_reason'] == 'stop'
            target = summary['growth_targets'][index]
            if index:
                messages.append(exchange['user_message'])
                assert record['started_at_s'] >= own[index - 1]['finished_at_s'] + summary['think_seconds'] - .01
                assert record['nominal_input_target'] == target
                target = max(target, record['minimum_input_with_new_message'])
                assert record['effective_input_target'] == target
            else:
                assert messages[-1] == exchange['user_message']
            assert digest(messages) == record['prompt_sha256']
            assert exchange['assistant_message'] == record['assistant_message']
            assert target - 32 <= record['input_tokens'] <= target
            usage = record['usage']
            assert usage['prompt_tokens'] == record['input_tokens']
            assert usage['total_tokens'] == usage['prompt_tokens'] + usage['completion_tokens']
            assert usage['total_tokens'] <= summary['max_model_len']
            assert 0 < usage['completion_tokens'] <= record['effective_output_budget']
            assert record['started_at_s'] <= record['first_token_at_s'] <= record['finished_at_s']
            assert 0 <= record['visible_ttft_s'] <= record['total_s']
            assert abs(record['total_s'] - (record['finished_at_s'] - record['started_at_s'])) < .00001
            messages.append(record['assistant_message'])
        assert messages == history['final_messages']
    result = dict(kind='instrument_generation_pilot_verification', verified=True,
        checked_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        users=2, rounds_per_user=9, natural_visible_responses=18,
        history_continuity_verified=True, timing_and_token_counts_verified=True,
        full_context_capacity_measured=False, probe_sha256=probe_hash,
        measurement_sha256=hashlib.sha256(measurement.read_bytes()).hexdigest(),
        histories_sha256=hashlib.sha256(histories_path.read_bytes()).hexdigest(),
        verifier_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
    (folder / 'verificacion.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
