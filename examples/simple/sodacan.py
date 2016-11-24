# sodacan.py
from pyomo.simple import *
from math import pi

m = SimpleModel()

r = m.var('r', bounds=(0,None))
h = m.var('h', bounds=(0,None))

m += 2*pi*r*(r + h)
m += pi*h*r**2 == 355

status = m.solve("ipopt")

print("Status = %s" % status['Solver'][0]['termination condition'])

print("%s = %f" % (r, value(r)))
print("%s = %f" % (h, value(h)))
print("Objective = %f" % value(m.objective()))

