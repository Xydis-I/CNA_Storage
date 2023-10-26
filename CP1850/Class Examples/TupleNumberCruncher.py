# -*- coding: utf-8 -*-
"""
@Author: C. C. Barrett
"""

from math import trunc
from random import randint

tupleData = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
randomData = [randint(0, 50) for x in range(0, 12)]

def median(items:tuple) -> int:
    return sorted(items)[trunc(len(items)/2)]
    
def listInfo(listData: list):
    return ("Average = %d Median = %d Min = %d Max = %d Dups = " % (sum(listData)/len(listData), median(listData), min(listData), max(listData)) + str(duplicates(listData)))
    
def duplicates(items:list) -> list:
    dups = []
    for item in items:
        if items.count(item) > 1 and dups.count(item) < 1:
            dups.append(item)
    return dups
    
print("Tuple Data: %s\n%s" % (str(tupleData), listInfo(tupleData)))
print("\nRandom Data: %s\n%s" % (str(randomData), listInfo(randomData)))
