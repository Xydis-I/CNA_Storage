# Assignment 1 - Problem 3
print("Change Calculator")

# Start of prompt loop
while True:
    # Prompt User for amount of change
    change = int(input("\nEnter number of cents (0-99): "))

    # Add Quarter, Remove Cents from Change
    quarters = change // 25
    change = change % 25
    # Add Dime, Remove Cents from Change
    dimes = change // 10
    change = change % 10
    # Add Nickel, Remove Cents from Change
    nickels = change // 5
    change = change % 5

    # Print minimum number of coins
    print("\nQuarters: %d\nDimes:\t  %d\nNickels:  %d\nPennies:  %d" % (quarters, dimes, nickels, change))

    # Continue Prompt
    loop = input("\nContinue? (y/n): ")
    if loop.lower() != "y":
        # Break out of loop if user hasn't explicitly agreed to continue
        break

print("\nBye!")
