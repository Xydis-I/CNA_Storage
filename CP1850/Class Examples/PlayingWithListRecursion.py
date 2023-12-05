# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:43:15 2023

@author: christian.barrett
"""

testList = list(range(20))

def RecursiveList(otherList):
    firstItem, *otherList = otherList
    print(firstItem)
    if len(otherList) > 0:
        RecursiveList(otherList)
        
RecursiveList(testList)