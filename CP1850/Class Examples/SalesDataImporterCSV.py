# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett
"""

from math import ceil
import csv

file_location = 'all_sales.csv'
imported_sales = 'importedsales.txt'

def header():
    print("SALES DATA IMPORTER")
    
def displayMenu() -> str:
    return "\nCOMMAND MENU\nview - View all sales\nadd  - Add sales\nmenu - Show menu\nexit - Exit program"
    
def get_imported_sales() -> list:
    with open(imported_sales, 'r', newline='') as file:
        return file.read().split('\r\n')

def get_sales_data(file_location) -> list:
    with open(file_location, 'r', newline='') as file:
        salesdata = [s.split(',') for s in file.read().split('\r\n')]
        return salesdata[:len(salesdata) - 1]

def get_csv_file() -> str:
    while True:
        imported = input("Enter name of file to import: ")
        if imported[-4:] == ".csv":
            return imported
        else:
            print("Invalid File Name.")

def import_csv(main_file, csv_file):
    if get_imported_sales().count(csv_file) > 0:
        print("\nFile '%s' has already been imported." % csv_file)
    else:
        with open(csv_file, 'r', newline='') as newfile:
            newSalesData = [s.split(',') for s in newfile.read().split('\r\n')]
            newSalesData = newSalesData[:len(newSalesData) - 1]
        view(newSalesData)
        
        with open(file_location, 'w', newline='') as file:
            temp = main_file + newSalesData
            writer = csv.writer(file)
            writer.writerows(temp)
            
        with open(imported_sales, 'a') as txtfile:
            txtfile.write("\n" + csv_file)
    
        print("\nImported sales added to list.")

def commandMenu():
    print(displayMenu())
    while True:
        command = input("\nPlease enter a command: ").lower()
        if command == "view":
            view(get_sales_data(file_location))
        elif command == "add":
            add(get_sales_data(file_location))
        elif command == "import":
            import_csv(get_sales_data(file_location) ,get_csv_file())
        elif command == "menu":
            commandMenu(get_sales_data(file_location))
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
        for number, data in enumerate(salesData, 1):
            total += float(data[0])
            print("%d.\t\t%s-%s-%s\t\t%d\t\t\t\t$%.1f"
                  % (number, data[1], data[2], data[3], ceil(int(data[2])/3), float(data[0])))
        print((47 * "-") + "\nTotal:" + (9 * "\t") + "$%.1f" % total)
    
def add(salesData:list):
    amount = getInt("Amount:\t\t\t")
    year = getInt("Year:\t\t\t")
    month = getInt("Month (1-12):\t", 1, 12)
    day = getInt("Day (1-%d):\t\t" % checkMonth(month), 1, checkMonth(month))
    salesData.append([amount, year, month, day])
    
    with open(file_location, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(salesData)
    
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
    header()
    commandMenu()
    
if __name__ == "__main__":
    main()