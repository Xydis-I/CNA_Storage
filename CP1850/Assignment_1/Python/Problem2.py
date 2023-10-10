# Assignment 1 - Problem 2
print("Tip Calculator\n")

# Prompt User for Cost
cost = float(input("Cost of meal: "))

# Print 15% Totals
print("\n15%%\nTip amount:\t  %.2f\nTotal amount: %.2f" % (cost * 0.15, cost + cost * 0.15))

# Print 20% Totals
print("\n20%%\nTip amount:\t  %.2f\nTotal amount: %.2f" % (cost * 0.20, cost + cost * 0.20))

# Print 25% Totals
print("\n25%%\nTip amount:\t  %.2f\nTotal amount: %.2f" % (cost * 0.25, cost + cost * 0.25))
