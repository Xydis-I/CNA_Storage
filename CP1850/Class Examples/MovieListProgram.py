# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:09:43 2023

@author: christian.barrett
"""
# Test Input: Gone with the Wind 1939

movies = [["Monty Python and the Holy Grail", 1975],
          ["On the Waterfront", 1954],
          ["Cat on a Hot Tin Roof", 1958]]

def main():
    header()
    commandMenu()

def header():
    print("COMMAND MENU\nlist - List all movies\nadd  - Add a movie\ndel  - Delete a movie\nexit - Exit program")

def listMovies():
    for i, name in enumerate(movies):
        print("%d. %s (%d)" % (i + 1, name[0], name[1]))
        
def addMovie(name:str, year:int):
    movies.append([name,year])
    print("%s was added." % name)
    
def deleteMovie(index:int):
    if index > len(movies):
        print("Invalid Selection.")
    else:
        print("%s was deleted." % movies[index - 1][0])
        movies.pop(index - 1)

def commandMenu():
    while True:
        command = input("\nCommand: ").lower()
        
        if command == "list":
            listMovies()
                
        elif command == "add":
            addMovie(input("Name: "), int(input("Year: ")))
            
        elif command == "del":
            deleteMovie(int(input("Number: ")))
            
        elif command == "exit":
            break
        
        else:
            print("Invalid Command.")
          
if __name__ == "__main__":
    main()
