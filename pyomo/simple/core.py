#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2014 Sandia Corporation.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  This software is distributed under the BSD License.
#  _________________________________________________________________________

__all__ = ['SimpleModel']

import six
from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.var import Var
from pyomo.core.base.objective import ObjectiveList, maximize
from pyomo.core.base.suffix import Suffix
from pyomo.core.base.constraint import ConstraintList
from pyomo.opt.base.solvers import SolverFactory


class SimpleModel(object):

    def __init__(self, maximize=False):
        import pyomo.environ
        self.model = ConcreteModel()
        self.model.o = ObjectiveList()
        self.model.c = ConstraintList()
        self._maximize = maximize

    def suffix(self, name):
        setattr(self.model, name, Suffix(direction=Suffix.IMPORT))

    def var(self, *args, **kwds):
        _args = args[1:]
        name = args[0]
        _v = Var(*_args, **kwds)
        setattr(self.model, name, _v)
        return _v

    def __iadd__(self, expr):
        if expr is True:
            self
        elif expr.is_relational():
            self.model.c.add( expr )
        else:
            self.model.o.add( expr )
            if self._maximize:
                n = len(self.model.o)
                self.model.o._data[n].sense = maximize
        return self

    def solve(self, name, *args, **kwargs):
        solver = SolverFactory(name)
        return solver.solve(self.model, *args, **kwargs)
   
    def pprint(self):
        self.model.pprint()

    def display(self):
        self.model.display()
 
    def objective(self, i=1):
        return self.model.o._data[i]

    def constraint(self, i=1):
        return self.model.c._data[i]

    def constraints(self):
        return six.itervalues(self.model.c)

