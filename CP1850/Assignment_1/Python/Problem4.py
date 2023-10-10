# Assignment 1 - Problem 4
print((63 * "=") + "\nShipping Calculator\n" + (63 * "="))

# Start of prompt loop
while True:
    # Prompt User for Cost until number greater than zero is entered
    while True:
        # User Prompt
        cost = float(input("Cost of items ordered:\t"))

        # Cost greater than 75.00
        if cost >= 75:
            shippingCost = 0
            break
        # Cost =>  50.00 - 74.99
        elif cost >= 50:
            shippingCost = 9.95
            break
        # Cost => 30.00 - 49.99
        elif cost >= 30:
            shippingCost = 7.95
            break
        # Cost => 0.00 - 29.99
        elif cost >= 0:
            shippingCost = 5.95
            break
        # Print Error and continue loop until user enters valid number
        else:
            print("You must enter a positive number. Please try again.")

    # Print costs
    print("Shipping cost:\t\t\t%.2f\nTotal cost:\t\t\t\t%.2f" % (shippingCost, cost + shippingCost))

    # Continue Prompt
    loop = input("\nContinue? (y/n): ")
    print((63 * "="))
    if loop.lower() != "y":
        # Break out of loop if user hasn't explicitly agreed to continue
        break

print("Bye!")
