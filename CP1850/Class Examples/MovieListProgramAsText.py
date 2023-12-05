# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:09:43 2023

@author: christian.barrett
"""
# Test Input: Gone with the Wind 1939

file_name = "MovieList.txt"

def getMovies(file_name:str) -> list:
    movies = []
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            movies.append(line)
    return movies

def main():
    header()
    commandMenu()

def header():
    print("The Movie List Program\n\nCOMMAND MENU\nlist - List all movies\nadd  - Add a movie\ndel  - Delete a movie\nexit - Exit program")

def listMovies(movies:list):
    for i, name in enumerate(movies):
        print("%d. %s" % (i + 1, name), end='')
    print()
        
def addMovie(movies:list,name:str):
    with open(file_name, 'a') as file_handle:
        file_handle.write("\n" + name)
    print("%s was added." % name)
    
def deleteMovie(movies:list,index:int):
    if index > len(movies):
        print("Invalid Selection.")
    else:
        print("%s was deleted." % str(movies[index - 1]).strip('\n'))
        movies.pop(index - 1)
    with open(file_name, 'w') as file_handle:
        for movie in movies:
            file_handle.write(movie)

def commandMenu():
    while True:
        movies = getMovies(file_name)
        command = input("\nCommand: ").lower()
        
        if command == "list":
            listMovies(movies)
                
        elif command == "add":
            addMovie(movies, input("Name: "))
            
        elif command == "del":
            deleteMovie(movies, int(input("Number: ")))
            
        elif command == "exit":
            break
        
        else:
            print("Invalid Command.")
          
if __name__ == "__main__":
    main()
