# sodacan.py

from pyomo.environ import *
from math import pi

M = ConcreteModel()
M.r = Var(bounds=(0,None))
M.h = Var(bounds=(0,None))
M.o = Objective(expr= 2*pi*M.r*(M.r + M.h))
M.c = Constraint(expr= pi*M.h*M.r**2 == 355)

solver = SolverFactory('ipopt')

status = solver.solve(M)

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (M.r, value(M.r)))
print("%s = %f" % (M.h, value(M.h)))
print("Objective = %f" % value(M.o))
