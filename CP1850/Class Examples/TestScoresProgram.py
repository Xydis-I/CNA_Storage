# -*- coding: utf-8 -*-

def TestScores():
    print("\nThe Test Scores Program\n\nEnter 3 Test Scores\n" + (22 * "="))
    scoreOne = int(input("Enter Test Score: "))
    scoreTwo = int(input("Enter Test Score: "))
    scoreThree = int(input("Enter Test Score: "))
    
    totalScore = scoreOne + scoreTwo + scoreThree
    averageScore = totalScore/3
    letterGrade = ""
    
    if (averageScore >= 90):
        letterGrade = "A"
    elif ((averageScore >= 80 and averageScore <= 89)):
        letterGrade = "B"
    elif ((averageScore >= 60 and averageScore <= 79)):
        letterGrade = "C"
    elif ((averageScore >= 40 and averageScore <= 59)):
        letterGrade = "D"
    else:
        letterGrade = "F"
        
    print((22 * "=") + "\nTotal Score: \t%d\nAverage Score: \t%d\nLetter Grade: \t%s\n\nBye!" % (totalScore,averageScore,letterGrade))


def RunTestScores():
    try:
        TestScores()
    except Exception:
        print("\nPlease Enter Valid Integer.")
    finally:
        userInput = input("\nContinue(y/n)?: ")
        if (userInput == "y"):
            RunTestScores()
        
RunTestScores()