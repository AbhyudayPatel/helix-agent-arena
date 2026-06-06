# HELIX — Insights (auto-generated)
_generated 2026-06-06T03:01:53 over 20 trajectories_

- **Task Goal Completion**: 70.0% (14/20)
- **Avg steps**: 17.25 | **avg cost**: $2.0901 | **avg wall**: 101.09s | **total cost**: $41.8024
- **Recovery rate**: 31.2% (15/48 error-steps healed)
- **World-model**: accuracy 75.0% (Brier 0.1956, n=64)

## Knowledge reuse (memory)
- tasks informed by recalled trajectories: 0
- solve-rate WITH memory: None% | WITHOUT: 70.0%

## World-model calibration
- predicted low(<0.5): n=2, actual solve-rate 100.0%
- predicted high(>=0.5): n=62, actual solve-rate 77.4%

## Failure patterns (error types in failed tasks)
- `NameError` × 6
- `Error` × 4
- `SyntaxError` × 3
- `KeyError` × 1

## Per-template performance
- `0d8a4ee`: 100.0% (2/2)
- `4ec8de5`: 100.0% (3/3)
- `50e1ac9`: 33.3% (1/3)
- `530b157`: 33.3% (1/3)
- `b119b1f`: 100.0% (3/3)
- `d4e9306`: 100.0% (3/3)
- `fac291d`: 33.3% (1/3)

## Most expensive tasks
- 0d8a4ee_2: $4.0671 (solved=True)
- 530b157_3: $3.9871 (solved=False)
- 50e1ac9_1: $3.8464 (solved=False)
- 50e1ac9_3: $3.4995 (solved=True)
- 530b157_1: $3.3455 (solved=True)

## Slowest tasks
- 50e1ac9_1: 201.35s, 25 steps
- 50e1ac9_3: 175.32s, 23 steps
- 0d8a4ee_2: 164.24s, 26 steps
- 530b157_3: 153.67s, 25 steps
- b119b1f_2: 150.56s, 15 steps
