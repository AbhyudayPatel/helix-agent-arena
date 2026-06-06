# HELIX — Insights (auto-generated)
_generated 2026-06-06T02:23:04 over 4 trajectories_

- **Task Goal Completion**: 75.0% (3/4)
- **Avg steps**: 27.5 | **avg cost**: $4.8267 | **avg wall**: 192.46s | **total cost**: $19.3068
- **Recovery rate**: 23.5% (4/17 error-steps healed)
- **World-model**: accuracy 84.0% (Brier 0.1374, n=25)

## Knowledge reuse (memory)
- tasks informed by recalled trajectories: 0
- solve-rate WITH memory: None% | WITHOUT: 75.0%

## World-model calibration
- predicted low(<0.5): n=1, actual solve-rate 100.0%
- predicted high(>=0.5): n=24, actual solve-rate 87.5%

## Failure patterns (error types in failed tasks)
- `NameError` × 4
- `Error` × 3
- `TypeError` × 2

## Per-template performance
- `27e1026`: 100.0% (1/1)
- `29caf6f`: 100.0% (1/1)
- `2a163ab`: 100.0% (1/1)
- `afc0fce`: 0.0% (0/1)

## Most expensive tasks
- afc0fce_2: $8.5525 (solved=False)
- 27e1026_1: $5.4142 (solved=True)
- 29caf6f_1: $3.2944 (solved=True)
- 2a163ab_2: $2.0457 (solved=True)

## Slowest tasks
- afc0fce_2: 322.62s, 40 steps
- 27e1026_1: 288.61s, 27 steps
- 2a163ab_2: 86.4s, 18 steps
- 29caf6f_1: 72.2s, 25 steps
