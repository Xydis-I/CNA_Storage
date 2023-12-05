# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett
"""

file_name = input("Enter filename: ")
movies = []
try:
    with open(file_name) as file:
        movies = file.readlines()
except FileNotFoundError:
    print("Could not find the file named %s" % file_name)
except OSError:
    print("File is found. Error reading the file")
except Exception:
    print("Unexpected Error Occured")