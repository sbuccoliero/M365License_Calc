from ortools.linear_solver import pywraplp

# Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')

infinity = solver.infinity()
# x and y are integer non-negative variables.
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')
z = solver.IntVar(0.0, infinity, 'z')


import os
from time import sleep

def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

# Calling the clear_screen() function
clear_screen()
print("Rubrik M365 License Calculator 1.3")
print()
print(" Enter Total Required Amount of Users = ")
Users = int(input("\033[1A \033[39C"))

# print('Enter Amount of Users =')
# Users = int(input())

# print('Enter Total Amount of Capacity (GB)')
# Capacity = int(input())

print(" Enter Total Required Capacity(GB) = ")
Capacity = int(input("\033[1A \033[37C"))
print('Calculating....:')
print()
# Users=100
# Capacity=1000

AvgCapacityperUser =Capacity / Users

print('Required Number of Users :', Users)
print('Total Required Capacity :', Capacity, 'GB')
print('Average Capacity Required per User:', AvgCapacityperUser, 'GB')

# print('Number of variables =', solver.NumVariables())

# Users : x + y +z <= 100.
solver.Add( x + y + z >= Users)

# Capacity: 5X + 20Y + 50Z skal være min 1000.
solver.Add( 5 * x + 20 * y + 50 * z >= Capacity)

# X,Y,z Must be Dividable by 10
# solver.MakeModulo( x,10 == 0)


#print('Number of constraints =', solver.NumConstraints())
print()

# Minimize1,5X + 2Y + 4Z.
solver.Minimize( 1.5 * x + 2 * y + 4 * z )
status = solver.Solve()

#print('Initial  5GB Licenses @$1.5:', int(x.solution_value()))
#print('Initial 20GB Licenses @$2:', int(y.solution_value()))
#print('Initial 50GB Licenses @$4:', int(z.solution_value()))
#print('Rounding Z:, Second Solve')
SolvedRoundZ= round(z.solution_value()/10)*10
solver.Add(  z == SolvedRoundZ)
status = solver.Solve()
#print('Second solve 5GB Licenses @$1.5:', int(x.solution_value()))
#print('Second solve 20GB Licenses @$2:', int(y.solution_value()))
#print('Second solve 50GB Licenses @$4:', int(z.solution_value()))
#print('Rounding Y:, Third Solve:')
SolvedRoundY= round(y.solution_value()/10)*10
solver.Add(  y == SolvedRoundY)
status = solver.Solve()
#print('3rd solve 5GB Licenses @$1.5:', int(x.solution_value()))
#print('3rd solve 20GB Licenses @$2:', int(y.solution_value()))
#print('3rd solve 50GB Licenses @$4:', int(z.solution_value()))
#print('Rounding X:,Last Solve:')

SolvedRoundX= ((x.solution_value() + 9) //10 * 10)
#print('4th solve 5GB Licenses @$1.5:', SolvedRoundX)
SolvedTotalUsers = SolvedRoundX + SolvedRoundY + SolvedRoundZ
SolvedTotalCapacity = ((SolvedRoundX*5) + (SolvedRoundY*20) + (SolvedRoundZ*50))

OverUsers = SolvedTotalUsers - Users
OverCapacity = SolvedTotalCapacity - Capacity

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print(('Total Amount of Users: '),int(SolvedTotalUsers))
    print(('Overcapacity of Users: '),int(OverUsers))
    print(('Total Amount of Capacity: '),int(SolvedTotalCapacity))
    print(('Overcapacity of Storage : '),int(OverCapacity))
    print('Lowest Combined Price per month ($):', int(solver.Objective().Value()))
    print()
    # print('Amount of 5GB Licenses @$1.5:', int(x.solution_value()))
    # print('Amount of 20GB Licenses @$2:', int(y.solution_value()))
    # print('Amount of 50GB Licenses @$4:', int(z.solution_value()))
    print('Amount of 5GB Licenses @$1.5:', int(SolvedRoundX))
    print('Amount of 20GB Licenses @$2:', SolvedRoundY)
    print('Amount of 50GB Licenses @$4:', SolvedRoundZ)
else:
    print('The problem does not have an optimal solution.')