# HELIX — Insights (auto-generated)
_generated 2026-06-05T02:48:10 over 1 trajectories_

- **Task Goal Completion**: 0.0% (0/1)
- **Avg steps**: 9.0 | **avg cost**: $0.7993 | **avg wall**: 64.1s | **total cost**: $0.7993
- **Recovery rate**: 50.0% (1/2 error-steps healed)
- **World-model**: accuracy 50.0% (Brier 0.2313, n=2)

## Knowledge reuse (memory)
- tasks informed by recalled trajectories: 0
- solve-rate WITH memory: None% | WITHOUT: 0.0%

## World-model calibration
- predicted low(<0.5): n=0, actual solve-rate None%
- predicted high(>=0.5): n=2, actual solve-rate 50.0%

## Failure patterns (error types in failed tasks)
- `NameError` × 1
- `IndexError` × 1

## Per-template performance
- `82e2fac`: 0.0% (0/1)

## Most expensive tasks
- 82e2fac_1: $0.7993 (solved=False)

## Slowest tasks
- 82e2fac_1: 64.1s, 9 steps
