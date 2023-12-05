# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett
"""

def menu_options():
    print("COMMAND MENU\n"
          "view - View country name\n"
          "add  - Add a country\n"
          "del  - Delete a country\n"
          "exit - Exit program")


def interface(countries:dict):
    while True:
        cmd = input("\nCommand: ").lower()
        if cmd == "view":
            view(countries)
        elif cmd == "add":
            add(countries)
        elif cmd == "del":
            delete(countries)
        elif cmd == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command.")


def view(countries:dict):
    print("Country codes:", *sorted(countries.keys()))
    cmd = input("Enter country code: ").upper()
    print("Country name: %s" % countries[cmd])


def add(countries:dict):
    key = input("Enter country code: ").upper()
    name = input("Enter country name: ").capitalize()
    countries.update({key:name})
    print("%s was added." % name)


def delete(countries:dict):
    cmd = input("Enter country code: ").upper()
    temp = countries.pop(cmd)
    print("%s was deleted." % temp)


def main():
    countries = {"CA":"Canada",
                 "MX":"Mexico",
                 "US":"United States"}
    menu_options()
    interface(countries)


main()
