# Assignment 2 - Problem 2
# Import get_int from Problem1 to promote code reuse.
from Problem1 import get_int


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


# Formats and prints individual contact if there is at least one contact.
def view_contact(contacts: list):
    if len(contacts) < 1:
        print("No contacts found.")
    else:
        contact = contacts[get_int("Number: ", 1, len(contacts)) - 1]
        print("Name: %s\nEmail: %s\nPhone: %s" % (contact[0], contact[1], contact[2]))


# Append contact to list.
def add_contact(contacts: list):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contacts.append([name, email, phone])
    print("%s was added." % name)


# Remove contacts based on index if there is at least one contact.
def delete_contact(contacts: list):
    if len(contacts) < 1:
        print("No contacts found.")
    else:
        contact = contacts.pop(get_int("Number: ", 1, len(contacts)) - 1)
        print("%s was deleted." % contact[0])


# Logic for user interactions.
def interface():
    contacts = [["Guido van Rossum", "guido@python.org", "123-456-7890"],
                ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]

    while True:
        command = input("\nCommand: ").lower()
        if command == "list":
            list_contacts(contacts)
        elif command == "view":
            view_contact(contacts)
        elif command == "add":
            add_contact(contacts)
        elif command == "del":
            delete_contact(contacts)
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
