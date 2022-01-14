{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww13440\viewh7800\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # coding=utf-8\
# Rubrik M365 License Calculator 0.9.4.2\
M365Calcversion="0.9.4.2"\
# Jan 2022 By Salvatore.Buccoliero@rubrik.com\
# Input Amount of Users and Required capacity in GB\
# Outputs minimum Required amount of 2,20,50GB Licens packs\
#\
# Requires Python3\
# Requires Google OR-Tools: https://developers.google.com/optimization/mip/mip_example#python\
#  to install: python -m pip install --upgrade --user ortools\
#  to validate OR-Tools: python -c "from ortools.linear_solver import pywraplp"\
#\
# To execute: python3 ./M365_License_Calc.py\
#\
# To Compile: pyinstaller --onefile M365_License_Calc.py\
# Compiled to .exe for Windows 10 platform: "M365_License_Calc.exe" \
# Compiled to MacOS Executable: "M365_License_Calc"}