# coding=utf-8
# Rubrik M365 License Calculator
M365Calcversion="2.12"
# June 2022 By Salvatore.Buccoliero@rubrik.com
# Input Amount of Users and Required capacity in GB
# Outputs minimum Required amount of 2,20,50GB,Unlimited Subscriptions
#
# Requires Python3 as a python script. Alternatively the binary can be downloaded for Windows or Mac and requires no python.
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
