# -*- coding: utf-8 -*-
"""
    Author: C. C. Barrett
"""

# Prints Header
print((63 * "=") + "\nShipping Calculator\n" + (63 * "="))

# Creates primary logic loop for calculator
while True:
    # Repeats prompt asking user for cost of items
    while True:
        cost = float(input("Cost of items ordered:\t"))
        # Throws error if user input is less than 0 (i.e. negative)
        if cost < 0:
            print("You must enter a positive number. Please try again.")
        # Breaks prompt loop when input is valid
        else:
            break
    
    # Determines Shipping Cost
    # Cost less than $30 
    if cost < 30:
        shippingCost = 5.95
    # Cost ranging from $30 to $49.99
    elif 30 <= cost < 50:
        shippingCost = 7.95
    # Cost ranging from $50 to $74.99
    elif 50 <= cost < 75:
        shippingCost = 9.95
    # Cost of $75 or higher
    else:
        shippingCost = 0
        
    # Prints both outputs
    print("Shipping cost:\t\t\t%.2f\nTotal cost:\t\t\t\t%.2f\n" % (shippingCost, cost + shippingCost))
    
    # Ends shipping calculator unless user explicitly states they would like to continue
    if input("Continue? (y/n): ").lower() != "y":
        break
    # Footer
    print(63 * "=")

# Footer & End Statement
print((63 * "=") + "\nBye!")
