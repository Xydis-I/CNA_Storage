# -*- coding: utf-8 -*-
def Divider(length = 64, char = "="):
    return length*char

def Menu():
    print(Divider() + "\n\t\t\t\t   Baseball Team Manager\nMENU OPTIONS\n"
          + "1 - Calculate batting average\n2 - Exit Program\n" + Divider())

def MenuLogic():
    while True:
        userInput = input("Menu option: ")
        
        if userInput == "1":
            print("Calculate batting average...")
            numAtBats = float(input("Official number of at bats: "))
            numOfHits = float(input("Number of hits: "))
            print("Batting average: %.3f\n" % (CalculateBattingAverage(numOfHits, numAtBats)))
        
        elif userInput == "2":
            print("Bye!")
            break
            
        else:
            print("Not a valid option. Please try again.\n")
            
def CalculateBattingAverage(numOfHits, numAtBats):
    return numOfHits/numAtBats
    
def main():
    Menu()
    MenuLogic()

main()
