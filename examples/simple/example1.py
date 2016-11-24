# Example adapted from PuLP file test1.py


# Import PuLP modeler functions
from pyomo.simple import *

# A new LP problem
prob = SimpleProblem()

# Variables
# 0 <= x <= 4
x = prob.var("x", bounds=(0,4))
# -1 <= y <= 1
y = prob.var("y", bounds=(-1,1))
# 0 <= z
z = prob.var("z", bounds=(0,None))

# Objective
prob += x + 4*y + 9*z, "obj"
# (the name at the end is facultative)

# Constraints
prob += x+y <= 5, "c1"
prob += x+z >= 10, "c2"
prob += -y+z == 7, "c3"

# Solve the problem using glpk
status = prob.solve("glpk")

# Print the status of the solved LP
print("Status:", LpStatus[prob.status])

# Print the value of the variables at the optimum
print("x = ", value(x))
print("y = ", value(y))
print("z = ", value(z))

# Print the value of the objective
print("objective=", value(prob.objective()))

