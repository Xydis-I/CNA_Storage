# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:40:17 2023

@author: christian.barrett
"""

def command_menu():
    print("COMMAND MENU\n"
          "show - Show book info\n"
          "add - Add book\n"
          "edit - Edit book\n"
          "del - Delete book\n"
          "exit - Exit program")


def show(books:dict):
    key = input("Title: ")
    try:
        print("Author name: %s\n"
              "Publication year: %s"
              % (books[key]['author'], books[key]['year']))
    except KeyError:
        print("Sorry, %s doesn't exist in the catalog." % key)


def update(books:dict):
    title = input("Title: ")
    author = input("Author name: ")
    year = input("Publication year: ")
    books.update({title:{'author':author, 'year':year}})


def delete(books:dict):
    key = input("Title: ")
    try:
        books.pop(key)
        print("%s was removed." % key)
    except KeyError:
        print("%s does not exist." % key)


def user_interface(books:dict):
    while True:
        cmd = input("\nCommand: ").lower()
        if cmd == "show":
            show(books)
        elif cmd == "add":
            update(books)
        elif cmd == "edit":
            update(books)
        elif cmd == "del":
            delete(books)
        elif cmd == "exit":
            break
        else:
            print("Invalid command.")


def main():
    books = {}
    command_menu()
    user_interface(books)


if __name__ == "__main__":
    main()
