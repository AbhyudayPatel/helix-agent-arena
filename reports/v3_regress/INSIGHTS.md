# HELIX — Insights (auto-generated)
_generated 2026-06-06T12:49:16 over 6 trajectories_

- **Task Goal Completion**: 66.7% (4/6)
- **Avg steps**: 13.17 | **avg cost**: $1.4204 | **avg wall**: 57.06s | **total cost**: $8.5227
- **Recovery rate**: 0.0% (0/7 error-steps healed)
- **World-model**: accuracy 50.0% (Brier 0.3885, n=6)

## Knowledge reuse (memory)
- tasks informed by recalled trajectories: 0
- solve-rate WITH memory: None% | WITHOUT: 66.7%

## World-model calibration
- predicted low(<0.5): n=1, actual solve-rate 100.0%
- predicted high(>=0.5): n=5, actual solve-rate 60.0%

## Failure patterns (error types in failed tasks)
- `NameError` × 2
- `SyntaxError` × 1

## Per-template performance
- `0d8a4ee`: 100.0% (1/1)
- `4ec8de5`: 100.0% (1/1)
- `50e1ac9`: 0.0% (0/1)
- `b119b1f`: 100.0% (1/1)
- `d4e9306`: 100.0% (1/1)
- `fac291d`: 0.0% (0/1)

## Most expensive tasks
- 0d8a4ee_1: $1.8413 (solved=True)
- 50e1ac9_3: $1.8309 (solved=False)
- d4e9306_1: $1.7558 (solved=True)
- 4ec8de5_1: $1.263 (solved=True)
- fac291d_3: $1.197 (solved=False)

## Slowest tasks
- 0d8a4ee_1: 80.34s, 15 steps
- d4e9306_1: 69.71s, 16 steps
- 50e1ac9_3: 56.7s, 15 steps
- 4ec8de5_1: 48.4s, 12 steps
- b119b1f_2: 45.63s, 8 steps
