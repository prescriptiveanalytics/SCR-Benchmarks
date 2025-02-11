
import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark, FEYNMAN_SRSD_HARD

for equation_name in list(srsdf.AllEquations):
      print(equation_name)
      benchmark = Benchmark(srsdf.AllEquations[equation_name])
      (valid, violated) = benchmark.check_constraints(str(benchmark.equation.sympy_eq), Library="SymPy", use_display_names = False)
      if(not valid):
        print(violated)
      assert valid
