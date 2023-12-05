# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:44:48 2023

@author: christian.barrett

2020-12-22,west,12493
2021-09-15,east,13761
2021-05-15,east,9710
2021-08-08,cent,8934

"""
import csv
from math import ceil

fileName = "salesData.csv"


def command_menu():
    print("SALES DATA IMPORTER\n\n"
          "COMMAND MENU\n"
          "view   - View all sales\n"
          "add    - Add sales\n"
          "import - Import sales from file\n"
          "menu   - Show menu\n"
          "exit   - Exit program")
    

def interface():
    while True:
        user_input = input("Please enter a command: ").lower()
        if user_input == "view":
            view(read_file())
        elif user_input == "add":
            add()
        elif user_input == "import":
            import_file()
        elif user_input == "menu":
            command_menu()
        elif user_input == "exit":
            print("Bye!")
            break


def view(salesData:list):
    print("\t Date\t\t\tQuarter\t\t   Region\t\t\t  Amount", "\n" + ("-" * 60))
    total = 0
    for n, sale in enumerate(salesData, 1):
        total += sale['amount']
        print("%d.\t %s\t\t%d\t\t\t   %-7s\t  %14s" % (n, sale['date'], ceil(int(sale['date'][5:7])/3), sale['region'].capitalize(), ("${:,.2f}".format(sale['amount']))))
    print(("-" * 60), "\nTOTAL:\t\t\t\t\t\t\t\t\t\t  %14s" % (("${:,.2f}".format(total))))
    

def add():
    print()
    
    
def import_file():
    print()


def read_file() -> list:
    with open(fileName, 'r', newline='') as file:
        data = []
        reader = csv.reader(file)
        for row in reader:
            data.append({'date':row[0],'region':row[1],'amount':float(row[2])})
        return data
    
    
def write_file(currentData:list):
    contents = read_file()
    #with open(fileName, 'w', newline='') as file:
        


def main():
    command_menu()
    
    
if __name__ == "__main__":
    main()