# Particle Simulation with Benchmarking and Profiling

## Project Overview

HPC course assignment implementing a 2D particle simulation that models circular motion. The project follows the "Benchmarking and Profiling" chapter, applying progressively more sophisticated profiling tools to identify and optimize bottlenecks.

## Python Version

Use Python 3.13 explicitly: `C:\Users\YourUser\AppData\Local\Programs\Python\Python313\python.exe`. The default `python` on this system resolves to Python 3.10 which lacks the installed packages.

## Key Commands

### Run tests
```
python -m pytest test_simul.py::test_evolve -v
```

### Run pytest-benchmark
```
python -m pytest test_simul.py::test_evolve_benchmark -v
```

### Time benchmark (Windows)
```
powershell -Command "Measure-Command { python simul.py }"
```

### cProfile
```
python -m cProfile -s tottime simul.py
python -m cProfile -o prof.out simul.py
```

### Convert cProfile output for KCachegrind/QCacheGrind
```
python -m pyprof2calltree -i prof.out -o prof.calltree
```

### line_profiler (requires @profile decorator on target function)
```
python -m kernprof -l -v simul_line_profiler.py
```

### memory_profiler (requires @profile decorator from memory_profiler)
```
python simul_memory.py
python simul_memory_slots.py
```

## Architecture

- **simul.py** — Core module. Contains `Particle` (x, y, ang_vel), `ParticleSimulator` (with `evolve` and optimized `evolve_fast`), visualization, and all benchmark/test functions. This is the primary import target for tests and profiling scripts.
- **particle.py** — Original classroom implementation (uses `v` instead of `ang_vel`). Kept as reference; not used by tests or profiling.
- **test_simul.py** — pytest tests importing from `simul`. `test_evolve` validates correctness; `test_evolve_benchmark` uses the pytest-benchmark fixture.
- **taylor.py** — Separate example (factorial, taylor_exp, taylor_sin) for demonstrating cProfile + pyprof2calltree + KCachegrind workflow.
- **simul_line_profiler.py** — Copy of simul with `@profile` decorator on `evolve` for use with `kernprof`.
- **simul_memory.py / simul_memory_slots.py** — Memory profiling variants: without and with `__slots__` on `Particle`, showing memory reduction.
- **benchmarking_notebook.ipynb** — Jupyter notebook demonstrating `%timeit` and `timeit` module usage.

## Dependencies

pytest, pytest-benchmark, line_profiler, memory_profiler, pyprof2calltree, psutil, matplotlib
