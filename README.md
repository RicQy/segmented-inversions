# Segmented Inversions – Problemsetter Assessment

This repository contains a custom Div1/Div2-style competitive programming problem:

> **Segmented Inversions**  
> Partition an array into exactly `k` segments to minimize the maximum inversion count among the segments.

## Contents

- `problem.md` – Full statement with input/output specification and examples.

- `idea.md` – Design notes: how the problem idea evolved and why the final version was chosen.

- `solution.md` – Explanation of the optimal algorithm (binary search + greedy + Fenwick tree).

- `solution.py` – Optimized Python solution intended to pass under 2s / 256MB.

- `solution_bf.py` – Optional brute-force solution for small `n` used for local verification.

- `generator.py` – Optional random test generator.

- `test_cases/` – At least five sample input/output files.

- `qwen/` – Qwen attempts and conversation links:

  - `conversations.md` – Paste shared Qwen links here.

  - `run_01.py`, `run_02.py`, `run_03.py` – Code from three Qwen attempts that should fail the tests.

- `requirements.json` – Time and memory limits for the intended judge environment.

## Running

To run the main solution on a file:

```bash
python solution.py < test_cases/1.in
```

To compare solution.py vs solution_bf.py on random tests, you can:

Use generator.py to create random input,

Pipe it into both programs and compare outputs.

## Limits

Time limit: 2 seconds.

Memory limit: 256 MB.

Sum of n across all test cases: ≤ 200000.

