# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:05:47 2023

@author: christian.barrett
"""

file_location = 'money.txt'

def read() -> float:
    with open(file_location, 'r', newline='') as readFile:
        return float(readFile.read())

def write(money:float):
    with open(file_location, 'w', newline='') as writeFile:
        writeFile.write(str(money))