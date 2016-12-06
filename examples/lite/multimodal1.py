# multimodal1.py

from pyomo.lite import *
from math import pi

m = LiteModel()
x = m.var('x', initialize = 0.25, bounds=(0,4))
y = m.var('y', initialize = 0.25, bounds=(0,4))

m += (2-cos(pi*x)-cos(pi*y)) * (x**2) * (y**2)

status = m.solve("ipopt")

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (x, value(x)))
print("%s = %f" % (y, value(y)))
print("Objective = %f" % value(m.objective()))

