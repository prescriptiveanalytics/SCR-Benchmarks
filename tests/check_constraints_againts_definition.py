import numpy as np
import shutil
import filecmp
import os
import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark


for benchmark_name in srsdf.AllEquations:
      benchmark = Benchmark(benchmark_name)
      (valid, violated) = benchmark.check_constraints(benchmark.eq)
      assert valid

