import numpy as np
from pymoo.core.problem import ElementwiseProblem
from .problem import *

class PymooHPA(ElementwiseProblem):
    def __init__(self, problem_name, n_div=4, level=0, NORMALIZED=True):
        self.hpa = eval(problem_name + '(n_div=' + str(n_div) + ', level=' + str(level) + ', NORMALIZED=' + str(NORMALIZED) + ')')
        self.nx = self.hpa.nx
        self.nf = self.hpa.nf
        self.ng = self.hpa.ng
        if NORMALIZED:
            self.lb = np.zeros(self.nx)
            self.ub = np.ones(self.nx)
        else:
            self.lb = self.hpa.lbound
            self.ub = self.hpa.ubound
        super().__init__(n_var=self.nx, n_obj=self.nf, n_constr=self.ng, xl=self.lb, xu=self.ub)
    def _evaluate(self, x, out, *args, **kwargs):
        if self.ng > 0:
            f, g = self.hpa(x)
            out["F"] = f
            out["G"] = g
        else:
            f = self.hpa(x)
            out["F"] = f
