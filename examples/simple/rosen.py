# rosen.py - Adapted from pyomo/examples/concrete/rosen.py

from pyomo.simple import *

m = SimpleModel()

x = m.var('x')
y = m.var('y')

m += (x-1)**2 + 100*(y-x**2)**2

status = m.solve("ipopt")

print("Status = %s" % status['Solver'][0]['termination condition'])

print("%s = %f" % (x, value(x)))
print("%s = %f" % (y, value(y)))
print("Objective = %f" % value(m.objective()))
