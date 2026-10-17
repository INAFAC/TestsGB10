#!/usr/bin/env python3
"""Check the recorded long-answer regression with the real, idle tokenizer.

Run after the original campaign restores service. This does not generate an
answer or measure model capacity; it validates preparation of the next message.
"""
import argparse
import ast
import copy
import datetime
import gzip
import hashlib
import importlib.util
import json
import pathlib
import random
import re
import types
import urllib.request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--result', required=True)
    parser.add_argument('--base-url', default='http://127.0.0.1:8000')
    args = parser.parse_args()
    root = pathlib.Path(args.root)
    meta = json.loads((root / 'metadata.json').read_text())
    proof = json.loads((root / 'verificacion-final.json').read_text())
    if meta['state'] != 'stopped' or meta['restore_status'] != 'healthy' or not proof['verified']:
        raise RuntimeError('Finish the original campaign and verify restoration first')
    raw = urllib.request.urlopen(args.base_url + '/metrics', timeout=10).read().decode()
    for key in ('num_requests_running', 'num_requests_waiting'):
        values = re.findall(r'^vllm:' + key + r'(?:\{[^\n]*\})? ([^\n]+)', raw, re.M)
        if not values or any(float(value) for value in values):
            raise RuntimeError('The server must be idle before instrument validation')

    case = 'memoria-60-personas-2-recorrido-completo-intento-1'
    folder = root / 'pruebas' / case
    state_path = folder / 'historiales.json.gz'
    history = json.loads(gzip.decompress(state_path.read_bytes()))['histories']['0']
    records = json.loads((folder / 'mediciones.json').read_text())['requests']
    previous = next(r for r in records if r['user_id'] == 0 and r['turn'] == 130)
    assert previous['ok'] and previous['finish_reason'] == 'stop'
    assert previous['usage']['completion_tokens'] == 1003
    messages = copy.deepcopy(history['final_messages'])
    assert messages[-1] == previous['assistant_message']
    before = copy.deepcopy(messages)

    model = 'nvidia/Qwen3.8-27B-NVFP4'
    models = json.load(urllib.request.urlopen(args.base_url + '/v1/models', timeout=10))['data']
    model_info = next(value for value in models if value['id'] == model)
    assert model_info['max_model_len'] == 262144

    def post(endpoint, payload):
        request = urllib.request.Request(args.base_url + endpoint,
            data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
        return json.load(urllib.request.urlopen(request, timeout=60))

    def tokenize(value):
        return post('/tokenize', dict(model=model, messages=value,
            add_generation_prompt=True, chat_template_kwargs={'enable_thinking': False}))['count']

    source = pathlib.Path(__file__).with_name('capacity_probe_v2.py')
    spec = importlib.util.spec_from_file_location('probe_v2', source)
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    fn = next(node for node in ast.walk(ast.parse(source.read_text()))
        if isinstance(node, ast.FunctionDef) and node.name == 'add_small_message')
    namespace = dict(a=types.SimpleNamespace(turns=257, growth_stop_context=None, model=model),
        model_info=model_info, growth_message_target=probe.growth_message_target,
        tokenize=tokenize, post=post)
    exec(compile(ast.Module(body=[fn], type_ignores=[]), str(source), 'exec'), namespace)
    sizing = namespace['add_small_message'](messages,
        'Resume las decisiones que hemos tomado y dime cuál debería ser mi siguiente paso.',
        133632, random.Random(1), 130)
    actual = tokenize(messages)
    assert messages[:-1] == before
    assert sizing['minimum_input_with_new_message'] > sizing['nominal_input_target']
    assert sizing['effective_input_target'] == sizing['minimum_input_with_new_message']
    assert sizing['effective_input_target'] - 32 <= actual <= sizing['effective_input_target']
    result = dict(kind='instrument_tokenizer_regression', verified=True,
        checked_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        original_case=case, user_id=0, preceding_turn=130, prepared_turn=131,
        preceding_answer_tokens=1003, actual_input_tokens=actual,
        preserved_messages=len(before), history_unchanged=True,
        history_sha256=hashlib.sha256(state_path.read_bytes()).hexdigest(),
        probe_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        check_script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        generation_requests=0, **sizing)
    destination = pathlib.Path(args.result)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
