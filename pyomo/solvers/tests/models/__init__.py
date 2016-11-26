#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2014 Sandia Corporation.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  This software is distributed under the BSD License.
#  _________________________________________________________________________

import pyomo.solvers.tests.models.base

import pyomo.solvers.tests.models.LP_block
import pyomo.solvers.tests.models.LP_compiled
import pyomo.solvers.tests.models.LP_constant_objective1
import pyomo.solvers.tests.models.LP_constant_objective2
import pyomo.solvers.tests.models.LP_duals_maximize
import pyomo.solvers.tests.models.LP_duals_minimize
import pyomo.solvers.tests.models.LP_inactive_index
import pyomo.solvers.tests.models.LP_piecewise
import pyomo.solvers.tests.models.LP_simple
import pyomo.solvers.tests.models.LP_trivial_constraints
import pyomo.solvers.tests.models.LP_unused_vars

import pyomo.solvers.tests.models.MILP_discrete_var_bounds
import pyomo.solvers.tests.models.MILP_simple
import pyomo.solvers.tests.models.MILP_unused_vars

import pyomo.solvers.tests.models.MIQCP_simple

import pyomo.solvers.tests.models.MIQP_simple

import pyomo.solvers.tests.models.QCP_simple

import pyomo.solvers.tests.models.QP_constant_objective
import pyomo.solvers.tests.models.QP_simple

import pyomo.solvers.tests.models.SOS1_simple
import pyomo.solvers.tests.models.SOS2_simple