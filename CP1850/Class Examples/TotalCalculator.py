# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett
"""

def header():
    print("The Total Calculator program\n")

def get_price() -> float:
    while True:
        try:
            return float(input("Enter price: "))
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity() -> int:
    while True:
        try:
            return int(input("Enter quantity: "))
        except ValueError:
            print("Invalid integer number. Please try again.")

def total(price: float, quantity: int):
    print("\nPRICE:\t\t%.2f\nQUANTITY:\t%d\nPRICE:\t\t%.2f" % (price, quantity, (price * quantity)))

def main():
    header()
    total(get_price(), get_quantity())
    
if __name__ == "__main__":
    main()
    