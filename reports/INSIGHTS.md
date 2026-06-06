# HELIX — Insights (auto-generated)
_generated 2026-06-05T02:43:02 over 87 trajectories_

- **Task Goal Completion**: 69.0% (60/87)
- **Avg steps**: 14.97 | **avg cost**: $2.0502 | **avg wall**: 94.52s | **total cost**: $178.3702
- **Recovery rate**: 28.2% (46/163 error-steps healed)
- **World-model**: accuracy 80.5% (Brier 0.1571, n=215)

## Knowledge reuse (memory)
- tasks informed by recalled trajectories: 54
- solve-rate WITH memory: 75.9% | WITHOUT: 57.6%

## World-model calibration
- predicted low(<0.5): n=8, actual solve-rate 75.0%
- predicted high(>=0.5): n=207, actual solve-rate 82.6%

## Failure patterns (error types in failed tasks)
- `NameError` × 31
- `Error` × 26
- `KeyError` × 2
- `TypeError` × 2
- `IndexError` × 1

## Per-template performance
- `0d8a4ee`: 100.0% (3/3)
- `22cc237`: 66.7% (2/3)
- `23cf851`: 100.0% (3/3)
- `27e1026`: 66.7% (2/3)
- `287e338`: 66.7% (2/3)
- `29caf6f`: 33.3% (1/3)
- `2a163ab`: 33.3% (1/3)
- `37a8675`: 66.7% (2/3)
- `383cbac`: 100.0% (3/3)
- `396c5a2`: 33.3% (1/3)
- `3ab5b8b`: 66.7% (2/3)
- `4ec8de5`: 0.0% (0/3)
- `4fab96f`: 100.0% (3/3)
- `50e1ac9`: 33.3% (1/3)
- `530b157`: 33.3% (1/3)
- `57c3486`: 100.0% (3/3)
- `6104387`: 66.7% (2/3)
- `6171bbc`: 100.0% (3/3)
- `68ee2c9`: 100.0% (3/3)
- `692c77d`: 100.0% (3/3)
- `6bdbc26`: 0.0% (0/3)
- `6c2c621`: 100.0% (3/3)
- `82e2fac`: 100.0% (3/3)
- `afc0fce`: 66.7% (2/3)
- `b119b1f`: 100.0% (3/3)
- `d0b1f43`: 0.0% (0/3)
- `d4e9306`: 100.0% (3/3)
- `df61dc5`: 100.0% (3/3)
- `fac291d`: 66.7% (2/3)

## Most expensive tasks
- 2a163ab_2: $6.402 (solved=False)
- 37a8675_1: $5.8975 (solved=True)
- afc0fce_1: $5.807 (solved=True)
- 22cc237_1: $5.4736 (solved=True)
- 6104387_2: $4.7151 (solved=False)

## Slowest tasks
- 22cc237_1: 342.64s, 26 steps
- 37a8675_1: 299.4s, 24 steps
- afc0fce_1: 276.67s, 25 steps
- 29caf6f_2: 257.54s, 22 steps
- 6104387_2: 256.24s, 24 steps
