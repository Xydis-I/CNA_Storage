# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett
"""
from math import ceil


def header():
    print("SALES DATA IMPORTER")
    
    
def displayMenu() -> str:
    return "\nCOMMAND MENU\nview - View all sales\nadd  - Add sales\nmenu - Show menu\nexit - Exit program"
    

def commandMenu(salesData:list):
    print(displayMenu())
    while True:
        command = input("\nPlease enter a command: ")
        if command == "view":
            view(salesData)
        elif command == "add":
            add(salesData)
        elif command == "menu":
            commandMenu(salesData)
        elif command == "exit":
            print("\nBye!")
            break
        else:
            print("Invalid command. Please try again.\n" + displayMenu())
            
    
    
def view(salesData:list):
    if len(salesData) == 0:
        print("No sales to view")
    else:
        print("\t\tDate\t\t\tQuarter\t\t\tAmount\n" + (47 * "-"))
        total = 0
        for number, data in enumerate(salesData):
            total += data[0]
            print("%d.\t\t%d-%d-%d\t\t%d\t\t\t\t$%.1f"
                  % (number + 1, data[1], data[2], data[3], ceil(data[2]/3), data[0]))
        print((47 * "-") + "\nTotal:" + (9 * "\t") + "$%.1f" % total)
    
    
def add(salesData:list):
    amount = getInt("Amount:\t\t\t")
    year = getInt("Year:\t\t\t")
    month = getInt("Month (1-12):\t", 1, 12)
    day = getInt("Day (1-%d):\t\t" % checkMonth(month), 1, checkMonth(month))
    
    salesData.append([amount, year, month, day])
    print("\nSales for %d-%d-%d added." % (year, month, day))
    
    
def getInt(prompt:str,start=0, stop=0) -> int:
    while True:
        num = input(prompt)
        if num.isnumeric():
            num = int(num)
            if (start <= num <= stop) or (start == 0 and stop == 0):
                return num
        print("Please enter valid number.")
        
        
def checkMonth(month:int) -> int:
    if (1,3,5,7,8,10,12).count(month) == 1:
        return 31
    elif (4,6,9,11).count(month) == 1:
        return 30
    else:
        return 28
    
    
def main():
    salesData = []
    header()
    commandMenu(salesData)

if __name__ == "__main__":
    main()
  
