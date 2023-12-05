# -*- coding: utf-8 -*-
"""
This module contains functions for getting
sales data from a user.
"""

def get_amount(salesAmount: str) -> float:
    """
    Gets a sales amount from the user, converts it to a
    float value, and returns the float value.
    
    """
    return float(salesAmount)

def get_day(day:str) -> int:
    """
    Gets a day from the user, converts it to an
    int value, and returns the int value.
    
    """
    return int(day)

def get_month(month:str) -> int:
    """
    Gets a month from the user, converts it to an
    int value, and returns the int value.
    
    """
    return int(month)

def get_year(year: str) -> int:
    """
    Gets a year from the user, converts it to an
    int value, and returns the int value.
    
    """
    return int(year)