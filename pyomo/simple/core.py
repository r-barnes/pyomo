#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2014 Sandia Corporation.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  This software is distributed under the BSD License.
#  _________________________________________________________________________

__all__ = ['SimpleModel']

from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.var import Var, VarList
from pyomo.core.base.objective import ObjectiveList()
from pyomo.core.base.constraint import ConstraintList
from pyomo.core.opt import SolverFactory


class SimpleModel(object):

    def __init__(self):
        self.model = ConcreteModel()
        self.model.o = ObjectiveList()
        self.model.c = ConstraintList()

    def var(self, *args, **kwds):
        _args = args[1:]
        name = args[0]
        _v = setattr(self.model, name, Var(*_args, **kwds))
        return _v

    def __iadd__(self, expr):
        if expr is True:
            self
        elif expr.is_relational():
            self.model.c.add( expr )
        else:
            self.model.o.add( expr )
        return self

    def solve(self, name):
        solver = SolverFactory(name)
        return solver.solve(self.model)
   
    def pprint(self):
        self.model.pprint()

    def display(self):
        self.model.display()
 
    def objective(self, i=0):
        return self.model.o[i]

    def constraint(self, i=0):
        return self.model.c[i]

