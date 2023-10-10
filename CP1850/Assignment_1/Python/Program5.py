# Assignment 1 - Problem 5
print("Table of Powers\n")

# Prompt User for valid inputs
while True:
    startNum = int(input("Start number:\t"))
    stopNum = int(input("Stop number:\t"))

    # Valid inputs break loop
    if startNum < stopNum:
        break
    # Print input error
    else:
        print("\nStart number must be less than Stop number\n")

# Print Header
print("\nNumber\t\tSquared\t\tCubed\n======\t\t=======\t\t=====")
# Print Squared & Cubed Table
for num in range(startNum, stopNum + 1):
    print("%d\t\t\t%d\t\t%d" % (num, num ** 2, num ** 3))
