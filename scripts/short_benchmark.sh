#!/usr/bin/env bash
# Run on the GB10 while vllm-qwen38 is ready. This generates load, not a new model.
set -euo pipefail
result_dir="${1:-/tmp/gb10-short-benchmark}"
docker exec vllm-qwen38 mkdir -p "$result_dir"
seed=100
for concurrency in 1 2 4 8; do
  docker exec vllm-qwen38 vllm bench serve \
    --backend openai --base-url http://127.0.0.1:8000 \
    --model nvidia/Qwen3.8-27B-NVFP4 --dataset-name random \
    --random-input-len 1024 --random-output-len 128 --random-range-ratio 0 \
    --num-prompts 20 --max-concurrency "$concurrency" --request-rate inf \
    --ignore-eos --temperature 0 --seed "$seed" --num-warmups 1 \
    --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,95 \
    --save-result --result-dir "$result_dir" \
    --result-filename "c${concurrency}-in1024.json" --disable-tqdm
  seed=$((seed+1))
done
docker exec vllm-qwen38 vllm bench serve \
  --backend openai --base-url http://127.0.0.1:8000 \
  --model nvidia/Qwen3.8-27B-NVFP4 --dataset-name random \
  --random-input-len 8192 --random-output-len 128 --random-range-ratio 0 \
  --num-prompts 12 --max-concurrency 4 --request-rate inf \
  --ignore-eos --temperature 0 --seed 104 --num-warmups 1 \
  --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,95 \
  --save-result --result-dir "$result_dir" \
  --result-filename c4-in8192.json --disable-tqdm
