# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:52:26 2023

@author: christian.barrett
"""

"""
Files
    -Text
    -Binary
"""

from Blackjack_ListOfLists import createDeck

file_name = "first_file.txt"

output_example_handle = open(file_name, 'w')
# r, a(w+), w, b

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist
"""

output_example_handle.write("This is my first file operation")
output_example_handle.close()

with open(file_name, 'w') as outfile_handle:
    outfile_handle.write("This is my second file operation\n")

with open(file_name, 'r') as outfile_handle:
    print(outfile_handle.readline())
   
with open(file_name, 'a') as outfile_handle:
    outfile_handle.write("We are doing the files module.\n")
    
"""
read()
readline()
readlines()
"""

# Reading Files
with open(file_name) as file_handle:
    for line in file_handle:
        print(line, end='')
    print()
    
with open(file_name) as file_handle:
    content = file_handle.read()
    print(content)
    
with open(file_name) as file_handle:
    content_lines = file_handle.readlines()
    print(content_lines)
    print(content_lines[0])
    
deck = createDeck()
with open("cards.txt", 'a') as card_file_handle:
    for card in deck:
        card_file_handle.write(str(card) + "\n")
        
with open("cards.txt", 'r') as card_handle:
    card_lines = card_handle.readlines()
    print(card_lines)
    print(card_lines[0])