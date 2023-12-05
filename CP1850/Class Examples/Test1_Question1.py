# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:02:05 2023

@author: christian.barrett
"""

# Prompts user for year and casts to an int.
year = int(input("Enter the value for year: "))

# Determines if year is divisible by 4 but not divisible by 100 unless its also divisible by 400
if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
    # Output if year is a leap year
    print("True")
else:
    # Output if year is not a leap year
    print("False")