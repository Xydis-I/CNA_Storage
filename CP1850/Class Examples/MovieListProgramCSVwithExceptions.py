# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:09:43 2023

@author: christian.barrett

Monty Python and the Holy Grail,1975
On the Waterfront,1954
Cat on a Hot Tin Roof,1958
Gone with the Wind,1939
"""
# Test Input: Gone with the Wind 1939
import csv

file_name = "MovieList.csv"

def getMovies(file_name:str) -> list:
    movies = []
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            movies.append(line.strip('\n').split(','))
    return movies

def main():
    header()
    commandMenu()

def header():
    print("The Movie List Program\n\nCOMMAND MENU\nlist - List all movies\nadd  - Add a movie\ndel  - Delete a movie\nexit - Exit program")

def listMovies(movies:list):
    for i, movie in enumerate(movies):
        print("%d. %s (%s)" % (i + 1, movie[0], movie[1]))
        
def addMovie(movies:list, name:str, year:str):
    movies.append([name,year])
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(movies)
    print("%s was added." % name)
    
def deleteMovie(movies:list,index:int):
    movie = movies.pop(index - 1)
    print("%s was deleted." % movie[0])
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(movies)

def commandMenu():
    while True:
        movies = getMovies(file_name)
        command = input("\nCommand: ").lower()
        
        if command == "list":
            listMovies(getMovies(file_name))
        elif command == "add":
            addMovie(movies, input("Name: "), input("Year: "))
        elif command == "del":
            while True:
                try:
                    deleteMovie(movies, int(input("Number: ")))
                    break
                except ValueError:
                    print("Invalid integer. Please try again.")
                except IndexError:
                    print("There is no movie with that number. Please try again.")
        elif command == "exit":
            break
        else:
            print("Invalid Command.")
          
if __name__ == "__main__":
    main()
