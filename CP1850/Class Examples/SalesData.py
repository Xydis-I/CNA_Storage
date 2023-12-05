# -*- coding: utf-8 -*-
import sales

_30DayMonths = [4, 6, 9, 11]

def Header():
    print("SALES DATA IMPORTER\n\nEnter sales data")

def SalesDataFormat():
    total = 0
    record = 0
    
    while True:
        record += 1 
        
        while True:
            amount = input("\nAmount:\t\t\t")
            if amount.isnumeric():
                amount = sales.get_amount(amount)
            else:
                print("Please enter valid number.")
                continue
                
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                break
        total += amount
        
        while True:
            year = input("Year:\t\t\t")
            if year.isnumeric():
                year = sales.get_year(year)
            else:
                print("Please enter valid number.")
                continue
                
            if year < 2000 or year > 9999:
                print("Year must be between 2000 and 9999.")
            else:
                break
        
        while True:
            month = input("\nMonth (1 - 12):\t")
            if month.isnumeric():
                month = sales.get_month(month)
            else:
                print("Please enter valid number.")
                continue
                
            if month < 1 or month > 12:
                print("Month must be between 1 and 12.")
            else:
                break
        
        while True:
            day = input("\nDay (1 - 31):\t").lower()
            if day.isnumeric():
                day = sales.get_day(day)
            else:
                print("Please enter valid number.")
                continue
                
            if (_30DayMonths.count(month) > 0 and day > 30) or (month == 2 and day > 28) or day > 31:
                print("Please enter valid day.")
            else:
                break
        
        if month < 4:
            quarter = 1
        elif month < 7:
            quarter = 2
        elif month < 10:
            quarter = 3
        else:
            quarter = 4
        print("\n%d.\t\t\t\t%d-%d-%d\t\tQuarter %d\t\t$%.1f\n" % (record, year, month, day, quarter, amount))
        
        if input("Enter more sales? (y/n): ").lower() != "y":
            break
        
    print("\nTotal Sales\n" + (11 * "-") + "\n$%.1f\n\nBye!" % total)
    
def main():
    Header()
    SalesDataFormat()
    
main()