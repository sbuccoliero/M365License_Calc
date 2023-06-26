# coding=utf-8
M365Calcversion="2.13"
# June 2023 By Salvatore.Buccoliero@rubrik.com
# Input Amount of Users and Required capacity in GB
# Outputs minimum Required amount of 2,20,50GB,Unlimited Subscriptions
#
# Requires Python3
# 
# To execute: 
# python3 ./M365_Solve_R.py
#
# If "Rubrik-M365-Sizing.html" file is present in the same directory it will read values and calculate from file.
#
# To execute in Automatic mode with Required users and Capacity:  
# python3 ./M365_Solve_R.py uuu(number) ccc(number)
#
# To Compile: pyinstaller --onefile M365_Solve_R.py
# Compiled to .exe for Windows 10 platform: "M365_Solve_R.exe" 
# Compiled to MacOS Executable: "M365_Solve_R"


from ast import Not
import os
from pickle import FALSE, TRUE
from time import sleep
import math
import sys
import re
#from tkinter import S
import requests
from requests.structures import CaseInsensitiveDict

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

# total arguments
n = len(sys.argv)
#print("Total arguments passed:", n)
# Arguments passed
#print("\nName of Python script:", sys.argv[0])
#print("\nArguments passed:", end = " ")
#for i in range(1, n):
#    print(sys.argv[i], end = " ")

File_Input_Method_Activated=False
if os.path.isfile('Rubrik-M365-Sizing.html'):
    File_Input_Method_Activated=True
#print("File_Input_Method_Activated:",bool(File_Input_Method_Activated))

if (n == 3):
    print("CMD Line Arguments entered, automatic input mode Activated")
    #print()
    Users = int(sys.argv[1])
    #print("Total Required Amount of Users = ",Users)
    Capacity = int(sys.argv[2])
    #print("Total Required Capacity(GB) = ", Capacity)
    #Capacity = int(input("\033[1A \033[37C"))
    #print('Calculating....:')
    #print()
elif File_Input_Method_Activated:
    print ("Rubrik-M365-Sizing.html File exist. Reading Users & Capacity")

    import chardet
    with open('Rubrik-M365-Sizing.html','rb') as f:
        rawdata = b''.join([f.readline() for _ in range(20)])
        #print(chardet.detect(rawdata)['encoding'])
        File_Encoding=chardet.detect(rawdata)['encoding']
        print(File_Encoding)

    #print("Reading Rubrik-M365-Sizing.html")
    com="Required Number of Licenses"
    with open("Rubrik-M365-Sizing.html", 'r', encoding=File_Encoding) as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if com in line:
                str1 = (lines[index+9])
                Users = int(re.search(r'\d+', str1).group())
                #print ("Read Users: ",Users)             
                str2 = (lines[index+10])
                #Capacity = int("".join(filter(str.isdigit, str2)))
                #Capacity = float(re.search(r'\d+', str2).group())
                Capacity = int(re.search(r'\d+', str2).group())
                #print ("Read Capacity: ",Capacity)


else:
    print(" Enter Total Required Amount of Users = ")
    Users = int(input("\033[1A \033[39C"))
    print(" Enter Total Required Capacity(GB) = ")
    Capacity = int(input("\033[1A \033[37C"))
    print('Calculating....:')
    print()
# Users=100
# Capacity=1000

AvgCapacityperUser =Capacity / Users
AvgCapacityperUser = (round(AvgCapacityperUser, 2))

print('Required Number of Users :', Users)
print('Total Required Capacity :', Capacity, 'GB')
print('Average Capacity Required per User:', AvgCapacityperUser, 'GB')

if (AvgCapacityperUser > 76):
    print('AvgCapacity Over 76, Unlimited is the best option')
    SolvedRoundupX=0
    LowestbyY=0
    LowestbyZ=0
    UnlimitedGBPacks=math.ceil((Users) / 10)
    SolvedTotalUsers = (UnlimitedGBPacks * 10)
    OverUsers = SolvedTotalUsers - Users
    SolvedTotalCapacity = Capacity
    OverCapacity = Capacity
    LowestCombinedPrice = (UnlimitedGBPacks * 10* 6)
    PricePerUser = LowestCombinedPrice / SolvedTotalUsers
else:

    # CURL LookupResult
    print ('Querying solver using HTML...')
    url = "https://m365licsolver-azure.azurewebsites.net:/api/httpexample"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"users":"'+str(Users)+'","data":"'+str(Capacity)+'"}'
    #print ('data: ',data)
    #print ('data1: ',data1)
    resp = requests.post(url, headers=headers, data=data)
    #print(resp.status_code)
    #print(resp._content)
    mumbo=resp._content
    html = mumbo.decode('utf-8')

    #print(html)
    new_result = re.findall(r'\d+', html)
    #print(new_result)
    SolvedRoundupX=int(new_result[0])*10
    LowestbyY=int(new_result[1])*10
    LowestbyZ= int(new_result[2])*10
    UnlimitedGBPacks=0
    SolvedTotalUsers = SolvedRoundupX + LowestbyY + LowestbyZ
    SolvedTotalCapacity = ((SolvedRoundupX*5) + (LowestbyY*20) + (LowestbyZ*50))

    OverUsers = SolvedTotalUsers - Users
    OverCapacity = SolvedTotalCapacity - Capacity
    LowestCombinedPrice = (SolvedRoundupX * 1.5)  + (LowestbyY * 2) + (LowestbyZ * 4)
    PricePerUser = LowestCombinedPrice / SolvedTotalUsers 
    LicenseonlyTeamsAndSharepoint = math.ceil((Capacity / 50) / 10) * 10
    LicenseonlyTeamsAndSharepoint = int(LicenseonlyTeamsAndSharepoint/10)
    LicenseonlyTeamsAndSharepointCapacity = LicenseonlyTeamsAndSharepoint * 10 * 50


print('Solution:')
print(('Total Amount of Users   : '),int(SolvedTotalUsers))
print(('Overcapacity of Users   : '),int(OverUsers))
print(('Total Amount of Storage : '),int(SolvedTotalCapacity),'GB') 
print(('Overcapacity of Storage : '),int(OverCapacity),'GB')
#print('Lowest Combined Price per month ($):', int(solver.Objective().Value()))
print('List Price per month    ($):', int(LowestCombinedPrice))
print('List Price per Year     ($):', int(LowestCombinedPrice)*12)
print('List Price Per User Per Month ($): ', (round(PricePerUser, 2)))
print('List Price Per User Per Year  ($): ', (round((PricePerUser*12), 2)))
#print()
# print('Amount of 5GB Licenses @$1.5:', int(x.solution_value()))
# print('Amount of 20GB Licenses @$2:', int(y.solution_value()))
# print('Amount of 50GB Licenses @$4:', int(z.solution_value()))
print(' 5GB Subscriptions ...... @$0.95:', int(SolvedRoundupX/10), ', ', (int(SolvedRoundupX/10))*10,' Users')
print('20GB Subscriptions ...... @$1.25:', int(LowestbyY/10), ', ', (int(LowestbyY/10))*10,' Users')
print('50GB Subscriptions ...... @$2.50:', int(LowestbyZ/10), ', ', (int(LowestbyZ/10))*10,' Users')
print('UnlimitedGB Subscriptions @$3.80:', int(UnlimitedGBPacks), ', ', (int(UnlimitedGBPacks))*10,' Users')
#print('________________________________________________________________________________')
# print()
#print('Min 50GB Licenses to cover only Teams and Sharepoint (NO Mailbox & Onedrive):', LicenseonlyTeamsAndSharepoint)
#print('Capacity provided for those', LicenseonlyTeamsAndSharepoint * 10, 'Licenses:',  LicenseonlyTeamsAndSharepointCapacity )


# It is for MacOS and Linux(here, os.name is 'posix')
# if os.name == 'posix':
#    print()
#else:
# It is for Windows platfrom
print('________________________________________________________________________________')
input("Copy Output, Then Press Enter to Exit Solver...")