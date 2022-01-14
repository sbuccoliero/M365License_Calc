# coding=utf-8
# Rubrik M365 License Calculator 0.9.4.2
M365Calcversion="0.9.4.2"
# Jan 2021 By Salvatore Buccoliero
# Input Amount of Users and Required capacity in GB
# Outputs minimum Required amount of 2,20,50GB Licens packs
#
# Requires Google OR-Tools: https://developers.google.com/optimization/mip/mip_example#python
#  to install: python -m pip install --upgrade --user ortools
#  to validate OR-Tools: python -c "from ortools.linear_solver import pywraplp"
#
# To execute: python3 ./M365_License_Calc.py
#
# Also compiled to .exe
# .exe version requires Win10 platform
# To Compile: pyinstaller --onefile M365_License_Calc.py


import os
from time import sleep

import math

def clear_screen():
    
    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

# Calling the clear_screen() function
clear_screen()

print("Rubrik M365 License Calculator",M365Calcversion)
print()

from ortools.linear_solver import pywraplp

# Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')

infinity = solver.infinity()
# x and y are integer non-negative variables.
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')
z = solver.IntVar(0.0, infinity, 'z')

print(" Enter Total Required Amount of Users = ")
Users = int(input("\033[1A \033[39C"))
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

#print('Number of constraints =', solver.NumConstraints())
#print()

# Minimize1,5X + 2Y + 4Z.
solver.Minimize( 1.5 * x + 2 * y + 4 * z )
status = solver.Solve()
SolvedRoundupZ = math.ceil(z.solution_value() / 10) * 10
SolvedRounddownZ= z.solution_value() - (z.solution_value() % 10)
# print('Initial  5GB Licenses @$1.5:', int(x.solution_value()))
# print('Initial 20GB Licenses @$2:', int(y.solution_value()))
# print('Initial 50GB Licenses @$4:', int(z.solution_value()))
# print('Initial Lowest Price per month ($):', int(solver.Objective().Value()))
SolvedRoundZ= round(z.solution_value()/10)*10
print('---------------------------------')
print()

# Rounding Z, Second Solve
solver.Add(  z == SolvedRoundupZ)
status = solver.Solve()
LowestPriceByRoundUpZ = int(solver.Objective().Value())
# print('Rounding Z:, Second Solve')
# print('Roundup Z: ',SolvedRoundupZ)
# print('Rounddown Z: ', SolvedRounddownZ)
# print('Lowest Price per month ($) by RoundupZ:', LowestPriceByRoundUpZ)
solver = pywraplp.Solver.CreateSolver('SCIP')
infinity = solver.infinity()
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')
z = solver.IntVar(0.0, infinity, 'z')
solver.Add( x + y + z >= Users)
solver.Add( 5 * x + 20 * y + 50 * z >= Capacity)
solver.Add(  z == SolvedRounddownZ)
solver.Minimize( 1.5 * x + 2 * y + 4 * z )
status = solver.Solve()
LowestPriceByRounddownZ = int(solver.Objective().Value())
# print('Lowest Price per month ($) by RounddownZ:', LowestPriceByRounddownZ)

if ( LowestPriceByRoundUpZ < LowestPriceByRounddownZ ):
    LowestbyZ = SolvedRoundupZ
#     print('Lowest Price IS  by Round UP Z', LowestbyZ )
else:
    LowestbyZ = SolvedRounddownZ
#     print('Lowest Price IS  by Round Down Z',LowestbyZ )

solver = pywraplp.Solver.CreateSolver('SCIP')
infinity = solver.infinity()
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')
z = solver.IntVar(0.0, infinity, 'z')
solver.Add( x + y + z >= Users)
solver.Add( 5 * x + 20 * y + 50 * z >= Capacity)
solver.Add(  z == LowestbyZ)
solver.Minimize( 1.5 * x + 2 * y + 4 * z )
status = solver.Solve()
# print('Second solve 5GB Licenses @$1.5:', int(x.solution_value()))
# print('Second solve 20GB Licenses @$2:', int(y.solution_value()))
# print('Second solve 50GB Licenses @$4:', int(z.solution_value()))
# print('Second solve Price per month ($):', int(solver.Objective().Value()))
# print('---------------------------------')
# print()


# print('Rounding Y:, Third Solve:')
SolvedRoundupY = math.ceil(y.solution_value() / 10) * 10
SolvedRounddownY= y.solution_value() - (y.solution_value() % 10)
# print('Roundup Y: ',SolvedRoundupY)
# print('Rounddown Y: ', SolvedRounddownY)

solver.Add(  y == SolvedRoundupY)
status = solver.Solve()
LowestPriceByRoundUpY = int(solver.Objective().Value())
# print('Lowest Price per month ($) by RoundupY:', LowestPriceByRoundUpY)

solver = pywraplp.Solver.CreateSolver('SCIP')
infinity = solver.infinity()
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')
z = solver.IntVar(0.0, infinity, 'z')
solver.Add( x + y + z >= Users)
solver.Add( 5 * x + 20 * y + 50 * z >= Capacity)
solver.Add(  z == LowestbyZ)
solver.Add(  y == SolvedRounddownY)
solver.Minimize( 1.5 * x + 2 * y + 4 * z )
status = solver.Solve()
LowestPriceByRounddownY = int(solver.Objective().Value())
# print('Lowest Price per month ($) by RounddownY:', LowestPriceByRounddownY)
if ( LowestPriceByRoundUpY < LowestPriceByRounddownY ):
    LowestbyY = SolvedRoundupY
    # print('Lowest Price IS  by Round UP Y', LowestbyY )
else:
    LowestbyY = SolvedRounddownY
    # print('Lowest Price IS  by Round Down Y',LowestbyY )

solver = pywraplp.Solver.CreateSolver('SCIP')
infinity = solver.infinity()
x = solver.IntVar(0.0, infinity, 'x')
y = solver.IntVar(0.0, infinity, 'y')
z = solver.IntVar(0.0, infinity, 'z')
solver.Add( x + y + z >= Users)
solver.Add( 5 * x + 20 * y + 50 * z >= Capacity)
solver.Add(  z == LowestbyZ)
solver.Add(  y == LowestbyY)
solver.Minimize( 1.5 * x + 2 * y + 4 * z )
status = solver.Solve()
# print('3rd solve 5GB Licenses @$1.5:', int(x.solution_value()))
# print('3rd solve 20GB Licenses @$2:', int(y.solution_value()))
# print('3rd solve 50GB Licenses @$4:', int(z.solution_value()))
# print('3rd solve Price per month ($):', int(solver.Objective().Value()))
# print('---------------------------------')
# print()

# print('Rounding UP X:,Last Solve:')
SolvedRoundupX = math.ceil(x.solution_value() / 10) * 10
# print('Rounded UP X: ', SolvedRoundupX)



# SolvedRoundX= round(x.solution_value()/10)*10
# print('4th solve 5GB Licenses @$1.5:', SolvedRoundupX)
SolvedTotalUsers = SolvedRoundupX + LowestbyY + LowestbyZ
SolvedTotalCapacity = ((SolvedRoundupX*5) + (LowestbyY*20) + (LowestbyZ*50))

OverUsers = SolvedTotalUsers - Users
OverCapacity = SolvedTotalCapacity - Capacity
LowestCombinedPrice = (SolvedRoundupX * 1.5)  + (LowestbyY * 2) + (LowestbyZ * 4)
PricePerUser = LowestCombinedPrice / SolvedTotalUsers 

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print(('Total Amount of Users   : '),int(SolvedTotalUsers))
    print(('Overcapacity of Users   : '),int(OverUsers))
    print(('Total Amount of Storage : '),int(SolvedTotalCapacity))
    print(('Overcapacity of Storage : '),int(OverCapacity))
    #print('Lowest Combined Price per month ($):', int(solver.Objective().Value()))
    print('Lowest List Price per month    ($):', int(LowestCombinedPrice))
    print('Lowest List Price per Year     ($):', int(LowestCombinedPrice)*12)
    print('Lowest List Price Per User Per Month ($): ',PricePerUser)
    print('Lowest List Price Per User Per Year  ($): ',PricePerUser*12)
    print()
    # print('Amount of 5GB Licenses @$1.5:', int(x.solution_value()))
    # print('Amount of 20GB Licenses @$2:', int(y.solution_value()))
    # print('Amount of 50GB Licenses @$4:', int(z.solution_value()))
    print('Amount of  5GB License Packs @$1.5:', int(SolvedRoundupX/10))
    print('Amount of 20GB License Packs @$2.0:', int(LowestbyY/10))
    print('Amount of 50GB License Packs @$4.0:', int(LowestbyZ/10))
else:
    print('The problem does not have an optimal solution.')
print()

# It is for MacOS and Linux(here, os.name is 'posix')
if os.name == 'posix':
    print()
else:
    # It is for Windows platfrom
    input("Press Enter to continue...")
