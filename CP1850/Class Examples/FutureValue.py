# -*- coding: utf-8 -*-
#100, 12, 10, 23233.91

def InvestmentCalculator(monthlyInput, yearlyRate, numOfYears):
    futureValue = 0
    for month in range(1, (numOfYears * 12) + 1):
        futureValue += monthlyInput
        futureValue += ((futureValue*(yearlyRate/12)/100))
    
    print("Future value:\t\t\t\t\t%.2f" % futureValue)
    
if __name__ == "__main__":
    while True:
        monthlyInput = float(input("\nEnter monthly investment:\t\t"))
        yearlyRate = float(input("Enter yearly interest rate:\t\t"))
        numOfYears = int(input("Enter number of years:\t\t\t"))
        InvestmentCalculator(monthlyInput, yearlyRate, numOfYears)
        if input("\nContinue? (y/n): ").lower() != "y":
            break