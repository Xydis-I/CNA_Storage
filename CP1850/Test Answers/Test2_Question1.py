# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 08:51:01 2023

@author: christian.barrett
"""
# Prints header and menu
def header():
    print("------ Class Students Managemnet ------\n"
          "1. Add Student\n"
          "2. Remove Student\n"
          "3. Display Students\n"
          "4. Calculate Average Age\n"
          "5. Quit")

# Makes sure user input is a valid int before continuing
def get_int(prompt: str) -> int:
    while True:
        userInput = input(prompt)
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Please enter valid number.")

# Adds student to inputed list
def add_student(students:list):
    name = input("Enter student name: ")
    age = get_int("Enter student age: ")
    students.append([name, age])
    print("Student added successfully!")

# Removes student from inputed list if there is at least one student
def remove_student(students:list):
    if len(students) < 1:
        print("No students entered.")
        return
    while True:
        name = input("Enter student name to be removed: ")
        # I couldn't remember if there was a good way to count and remove a 2d array
        # so I sorta just list comprehended my way around it
        if [student[0] for student in students].count(name) > 0:
            students.pop([student[0] for student in students].index(name))
            print("Student removed successfully!")
            break
        else:
            print("Student not found. Please try again.")

# Displays list of students if there is at least one student
def display_students(students:list):
    if len(students) < 1:
        print("No students entered.")
        return
    print("List of Students:")
    for student in students:
        print("Name: %s, Age: %d" % (student[0], student[1]))

# Calculate average age if there is at least one student
def calculate_average_age(students:list):
    if len(students) < 1:
        print("No students entered.")
        return
    print("Average age of students: %.1f" % (sum([student[1] for student in students])/len(students)))

# Main Menu
def menu_options(students:list):
    while True:
        header()
        userInput = input("Enter your choice (1-5): ")
        if userInput == "1":
            add_student(students)
        elif userInput == "2":
            remove_student(students)
        elif userInput == "3":
            display_students(students)
        elif userInput == "4":
            calculate_average_age(students)
        elif userInput == "5":
            print("Program terminated.")
            break
        else:
            print("Please enter valid selection.")


def main():
    students = []
    menu_options(students)
    
    
if __name__ == "__main__":
    main()
    