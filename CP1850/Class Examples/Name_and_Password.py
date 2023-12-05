# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:55:43 2023

@author: christian.barrett
"""

def get_name() -> str:
    while True:
        name = input("Enter full name: ").strip()
        if ' ' in name:
            return name
        print("You must enter your full name.")


def get_password() -> str:
    while True:
        password = input("Enter password: ").strip()
        if (len(password) > 7 and len([l for l in password if l.isupper()]) > 0 and len([l for l in password if l.isdigit()]) > 0):
            return password
        print("Password must be 8 characters or more\n"
              "with at least one digit and one uppercase letter")


def create_account():
    name = get_name()
    print()
    passwd = get_password()
    print("\nHi %s, thanks for creating an account." % (name[:name.find(' ')]))


def main():
    create_account()


if __name__ == "__main__":
    main()
