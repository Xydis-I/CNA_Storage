# Assignment 1 - Problem 1
print("Letter Grade Converter")

# Start of prompt loop
while True:
    # User inputted grade number
    userInput = int(input("\nEnter numerical grade: "))
    # A => 88 - 100
    if userInput >= 88:
        letterGrade = "A"
    # B => 80 - 87
    elif userInput >= 80:
        letterGrade = "B"
    # C => 67 - 79
    elif userInput >= 67:
        letterGrade = "C"
    # D => 60 - 66
    elif userInput >= 60:
        letterGrade = "D"
    # F => 0 - 59
    else:
        letterGrade = "F"
    # Print converted grade
    print("Letter Grade: %s" % letterGrade)

    # Continue Prompt
    loop = input("\nContinue? (y/n): ")
    if loop.lower() != "y":
        # Break out of loop if user hasn't explicitly agreed to continue
        break

print("\nBye!")
