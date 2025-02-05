import numpy as np
import shutil
import filecmp
import os
import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark


for equation_name in srsdf.AllEquations:
      print(equation_name)
      benchmark = Benchmark(srsdf.AllEquations[equation_name])
      (valid, violated) = benchmark.check_constraints(benchmark.equation.get_eq_raw(),Library="SymPy",use_display_names = True)
      if(not valid):
        print(violated)
      assert valid


for equation_name in srsdf.AllEquations:
      print(equation_name)
      benchmark = Benchmark(srsdf.AllEquations[equation_name])
      (valid, violated) = benchmark.check_constraints(benchmark.equation.get_eq_raw(),Library="JAX", use_display_names = True)
      if(not valid):
        print(violated)
      assert valid

