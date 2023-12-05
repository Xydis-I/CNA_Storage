# -*- coding: utf-8 -*-
print("The Miles Per Gallon Program")

def CalcMPG(milesDriven, gallonsUsed):    
    if gallonsUsed <= 0:
        print("Gallons used must be greater than zero. Try again.\n\nBye!")
    else:
        print("\nMiles Per Gallion: \t\t\t\t %.2f \n" % (milesDriven/gallonsUsed))
        
while True:
    milesDriven = float(input("\nEnter miles driven: \t\t\t "))
    gallonsUsed = float(input("Enter gallons of gas used: \t\t "))
    CalcMPG(milesDriven, gallonsUsed)
    if input("Continue? (y/n): ").lower() != "y":
        break

print("\nBye!")