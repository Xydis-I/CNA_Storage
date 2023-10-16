# -*- coding: utf-8 -*-
"""
    Author: C. C. Barrett
"""

movies = ["Monty Python and the Holy Grail",
          "On the Waterfront",
          "Cat on a Hot Tin Roof"]

def main():
    header()
    commandMenu()

def header():
    print("COMMAND MENU\nlist - List all movies\nadd  - Add a movie\ndel  - Delete a movie\nexit - Exit program")

def listMovies():
    for i, name in enumerate(movies):
        print("%d. %s" % (i + 1, name))
        
def addMovie(name):
    movies.append(name)
    print("%s was added." % name)
    
def deleteMovie(index):
    print("%s was deleted." % movies[index])
    movies.pop(index)

def commandMenu():
    while True:
        command = input("\nCommand: ")
        
        if command.lower() == "list":
            listMovies()
                
        elif command.lower() == "add":
            addMovie(input("Name: "))
            
        elif command.lower() == "del":
            deleteMovie(int(input("Number: ")) - 1)
            
        elif command.lower() == "exit":
            break
        
        else:
            print("Invalid command.")
            
main()
