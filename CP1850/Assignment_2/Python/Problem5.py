# Assignment 2 - Problem 5
# Import get_int from Problem1 to promote code reuse.
from Problem1 import get_int
import csv


def header():
    print("Contact Manager")


def command_menu():
    print("\nCOMMAND MENU\nlist - Display all contacts\nview - View a contact"
          "\nadd  - Add a contact\ndel  - Delete a contact\nexit - Exit program")


# Enumerates, formats, and prints contacts list if there is at least one contact.
def list_contacts(contacts: list):
    if len(contacts) < 1:
        print("No contacts found.")
    else:
        for i, name in enumerate(contacts, 1):
            print("%d. %s" % (i, name[0]))


# Reads contacts file, creates one if not found.
def check_contacts() -> list:
    try:
        with open("contacts.csv", "r") as file:
            contacts = [c.split(',') for c in file.read().split('\n')]
            return contacts[:len(contacts) - 1]
    except FileNotFoundError:
        with open("contacts.csv", "w") as file:
            return []


# Formats and prints individual contact if there is at least one contact.
def view_contact(contacts: list):
    if len(contacts) < 1:
        print("No contacts found.")
    else:
        index = get_int("Number: ", 0, len(contacts)) - 1
        print("Name: %s\nEmail: %s\nPhone: %s" % (contacts[index][0], contacts[index][1], contacts[index][2]))


# Append new contact to contacts file(.csv).
def add_contact(name: str, email: str, phone: str):
    with open("contacts.csv", 'a', newline='') as file:
        csv.writer(file).writerow([name, email, phone])
    print("%s was added." % name)


# Delete indexed item and rewrite remaining contacts if there is at least one contact.
def delete_contact(contacts: list):
    if len(contacts) < 1:
        print("No contacts found.")
    else:
        contact = contacts.pop(get_int("Number: ", 0, len(check_contacts())) - 1)
        with open("contacts.csv", 'w', newline='') as file:
            csv.writer(file).writerows(contacts)
        print("%s was deleted." % contact[0])


# Logic for user interactions.
def interface():
    while True:
        command = input("\nCommand: ").lower()
        if command == "list":
            list_contacts(check_contacts())
        elif command == "view":
            view_contact(check_contacts())
        elif command == "add":
            add_contact(input("Name: "), input("Email: "), input("Phone: "))
        elif command == "del":
            delete_contact(check_contacts())
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid Command.")


def main():
    header()
    command_menu()
    interface()


if __name__ == "__main__":
    main()
