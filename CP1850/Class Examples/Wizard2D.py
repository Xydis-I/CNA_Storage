# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett
"""
def header():
    print("The Wizard Inventory Program\n\nCOMMAND MENU\nshow - Show all items\ngrab - Grab an item\nedit - Edit an item\ndrop - Drop and item\nexit - Exit program")


def show(inventory:list):
    for n,item in enumerate(inventory, start=1):
        print("%d. %s" % (n, item))


def grab(inventory:list):
    if len(inventory) < 4:
        name = input("Name: ")
        inventory.append(name)
        print(name + " was added.")
    else:
        print("You can't carry any more items. Drop something first.")


def edit(inventory:list):
    while True:
        index = input("Number: ")
        if index.isnumeric():
            index = int(index) - 1
            if 0 <= index < len(inventory):
                name = input("Updated name: ")
                inventory[index] = name
                print("Item number %d was updated." % (index + 1))
                break
        print("Invalid item. Number out of range.")


def drop(inventory:list):
    while True:
        index = input("Number: ")
        if index.isnumeric():
            index = int(index)
            if 0 < index < len(inventory):
                name = inventory.pop(index - 1)
                print(name + " was dropped.")
                break
        print("Invalid item. Number out of range.")


def commandMenu(inventory:list):
    while True:
        command = input("\nCommand: ").lower()
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab(inventory)
        elif command == "edit":
            edit(inventory)
        elif command == "drop":
            drop(inventory)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command.")
            
            
def main():
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]
    header()
    commandMenu(inventory)


main()