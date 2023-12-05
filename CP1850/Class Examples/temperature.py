# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:03:55 2023

@author: christian.barrett
"""

def CelsiusToFahrenheit(f:float) -> float:
    return (((f*9)/5)+32)

def FahrenheitToCelsius(c:float) -> float:
    return (((c - 32) * 5)/9)

if __name__ == "__main__":
    print("%.0f Fahrenheit = %.0f Celsius" % (0,FahrenheitToCelsius(0)))
    print("%.0f Fahrenheit = %.0f Celsius" % (40,FahrenheitToCelsius(40)))
    print("%.0f Fahrenheit = %.0f Celsius" % (80,FahrenheitToCelsius(80)))
    print("%.0f Fahrenheit = %.0f Celsius" % (120,FahrenheitToCelsius(120)))
    print("%.0f Fahrenheit = %.0f Celsius" % (160,FahrenheitToCelsius(160)))
    print("%.0f Fahrenheit = %.0f Celsius" % (200,FahrenheitToCelsius(200)))
    print("%.0f Celsius = %.0f Fahrenheit" % (0,CelsiusToFahrenheit(0)))
    print("%.0f Celsius = %.0f Fahrenheit" % (20,CelsiusToFahrenheit(20)))