# -*- coding: utf-8 -*-
print((64 * "=") + "\nShipping Calculator\n" + (64 * "="))

shippingCost = 0

def CalculateShippingCost():
    itemCost = float(input("Cost of items ordered:\t"))
    if (itemCost >= 0):
        if itemCost < 30:
            shippingCost = 5.95
        elif 30 <= itemCost <= 49.99:
            shippingCost = 7.95
        elif 50 <= itemCost <= 74.99:
            shippingCost = 9.95
        elif itemCost >= 75:
            shippingCost = 0
        print("Shipping cost:\t\t\t%.2f\nTotal cost:\t\t\t\t%.2f" %
              (shippingCost,itemCost + shippingCost))
    else:
        print("You must enter a positive number. Please try again.")
        CalculateShippingCost()

while True:
    CalculateShippingCost()
    userInput = input("\nContinue? (y/n): ")
    print((64 * "="))
    if userInput.lower() == "n":
        break
    
print("Bye!")