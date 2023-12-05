# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:36:18 2023

@author: christian.barrett
"""

# It doesn't ask to loop or anything, just display an error so I choose to let it return a 'NoneType'
def request_file() -> list:
    fileName = input("Enter the name of the file: ")
    try:
        with open(fileName) as file:
            return file.readlines()
    except FileNotFoundError:
        print("File not found. Please check file name and try again.")

# Rather than let it throw another exception to catch I just handled the 'NoneType' I returned before continuing
def print_rules(rules:list):
    if str(type(rules)) != "<class 'NoneType'>":
        print("\nRules ---\n")
        for i, rule in enumerate(rules, start=1):
            print("\t%d. %s" % (i, rule))


def main():
    print_rules(request_file())
    
    
if __name__ == "__main__":
    main()
    