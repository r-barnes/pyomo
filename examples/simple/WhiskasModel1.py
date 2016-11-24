# The Simplified Whiskas Model adapted from PuLP
# Authors: Antony Phillips, Dr Stuart Mitchell  2007

from pyomo.simple import *

# Create the 'prob' variable to contain the problem data
prob = SimpleModel()

# The 2 variables Beef and Chicken are created with a lower limit of zero
x1 = prob.var("ChickenPercent", within=NonNegativeIntegers)
x2 = prob.var("BeefPercent", within=NonNegativeReals)

# The objective function is added to 'prob' first
prob += 0.013*x1 + 0.008*x2 # "Total Cost of Ingredients per can"

# The five constraints are entered
prob += x1 + x2 == 100 # "PercentagesSum"
prob += 0.100*x1 + 0.200*x2 >= 8.0 # "ProteinRequirement"
prob += 0.080*x1 + 0.100*x2 >= 6.0 # "FatRequirement"
prob += 0.001*x1 + 0.005*x2 <= 2.0 # "FibreRequirement"
prob += 0.002*x1 + 0.005*x2 <= 0.4 # "SaltRequirement"

# Solve
status = prob.solve("glpk")

# The status of the solution is printed to the screen
print("Status: %s" % status['Solver'][0]['termination condition'])

# Each of the variables is printed with it's resolved optimum value
print("%s = %f" % (x1, value(x1)))
print("%s = %f" % (x2, value(x2)))
    
# The optimised objective function value is printed to the screen
print("Total Cost of Ingredients per can = %f" % value(prob.objective()))
