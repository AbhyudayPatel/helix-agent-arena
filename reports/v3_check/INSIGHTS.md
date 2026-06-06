# HELIX — Insights (auto-generated)
_generated 2026-06-06T12:20:49 over 6 trajectories_

- **Task Goal Completion**: 50.0% (3/6)
- **Avg steps**: 18.5 | **avg cost**: $3.0216 | **avg wall**: 167.67s | **total cost**: $18.1296
- **Recovery rate**: 41.7% (5/12 error-steps healed)
- **World-model**: accuracy 84.6% (Brier 0.1403, n=39)

## Knowledge reuse (memory)
- tasks informed by recalled trajectories: 0
- solve-rate WITH memory: None% | WITHOUT: 50.0%

## World-model calibration
- predicted low(<0.5): n=1, actual solve-rate 100.0%
- predicted high(>=0.5): n=38, actual solve-rate 86.8%

## Failure patterns (error types in failed tasks)
- `SyntaxError` × 3
- `NameError` × 2

## Per-template performance
- `50e1ac9`: 50.0% (1/2)
- `530b157`: 100.0% (2/2)
- `fac291d`: 0.0% (0/2)

## Most expensive tasks
- 530b157_3: $6.1659 (solved=True)
- 530b157_2: $4.4791 (solved=True)
- 50e1ac9_2: $2.2555 (solved=False)
- 50e1ac9_1: $2.0851 (solved=True)
- fac291d_2: $2.0052 (solved=False)

## Slowest tasks
- 530b157_3: 395.64s, 27 steps
- 530b157_2: 255.81s, 24 steps
- fac291d_2: 182.82s, 15 steps
- 50e1ac9_2: 72.37s, 17 steps
- 50e1ac9_1: 58.52s, 17 steps
