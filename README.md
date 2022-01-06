Rubrik M365 License Calculator 1.4.1
Dec 2021 By Salvatore Buccoliero
Input Amount of Users and Required capacity in GB
Outputs minimum Required amount of 2,20,50GB Licens packs

Requires Google OR-Tools: https://developers.google.com/optimization/mip/mip_example#python
to install: python -m pip install --upgrade --user ortools
to validate OR-Tools: python -c "from ortools.linear_solver import pywraplp"

To execute: python3 ./M365_License_Calc.py

Compiled to Windows10 executable as "M365_License_Calc.exe"
.exe version requires Win10 platform

Compiled to MacOS as "M365_License_Calc"
To Compile: pyinstaller --onefile M365_License_Calc.py
