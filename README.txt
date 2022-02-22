# Rubrik M365 License Calculator 0.9.5.4
# Febr 2022 By Salvatore.Buccoliero@rubrik.com
# Input Amount of Users and Required capacity in GB
# Outputs minimum Required amount of 2,20,50GB Licens packs
#
# Requires Python3
# Requires Google OR-Tools: https://developers.google.com/optimization/mip/mip_example#python
#  to install: python -m pip install --upgrade --user ortools
#  to validate OR-Tools: python -c "from ortools.linear_solver import pywraplp"
#
# To execute: 
# python3 ./M365_License_Calc.py
#
# If "Rubrik-M365-Sizing.html" file present it will read values and calculate from file.
#
# To execute in Automatic mode with Required users and Capacity:  
# python3 ./M365_License_Calc.py uuu(number) ccc(number)
#
# To Compile: pyinstaller --onefile M365_License_Calc.py
# Compiled to .exe for Windows 10 platform: "M365_License_Calc.exe" 
# Compiled to MacOS Executable: "M365_License_Calc"
