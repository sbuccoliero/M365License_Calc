from ortools.linear_solver import pywraplp

# Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')

infinity = solver.infinity()
# x and y are integer non-negative variables.
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')
z = solver.IntVar(0.0, infinity, 'z')

print('Number of variables =', solver.NumVariables())

# Users : x + y +z <= 100.
solver.Add( x + y + z >= 100)

# Capacity: 5X + 20Y + 50Z skal være min 1000.
solver.Add( 5 * x + 20 * y + 50 * z >= 1000)

print('Number of constraints =', solver.NumConstraints())

# Minimize1,5X + 2Y + 4Z.
solver.Minimize( 1.5 * x + 2 * y + 4 * z )

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())
    print('z =', z.solution_value())
else:
    print('The problem does not have an optimal solution.')