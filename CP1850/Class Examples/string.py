# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 08:48:45 2023

@author: christian.barrett
"""

# get Ascii Values
ord('A')
ord('a')

# String properties
len('Arun   ')

# String Access Methods
string1 = 'This is the CP1850 class'
len(string1)
string1[0]
string1[5]
string1[12]
string1[-1]

string1[:3]
string1[12:18]
string1[::-1]

# Multiline string
query = '''SELECT name, value as CategoryValue
FROM CategoryTable where name = ?'''

# Check for substring in a string
if ('CP1850' in string1):
    print('Yes, substring exists.\n')
else:
    print('Substring does not exist.')            

# Looping a string
for char in string1:
    print(char)

# Some basic string functions
# Check if is integer
user_entry = '2345.345'
user_entry.isdigit()

# Check if it begins with a specific substring
string1.startswith('This')
string1.endswith('class')

# Transformations
string1.upper()
string1.lower()
string1.capitalize()
string1[12:18].capitalize()
string1.title()

string2 = '               This is string2'
string2.strip().upper()
string1.replace('CP1850', 'CP4477')

user_entry.replace('.', '').isdigit()
user_entry.isnumeric()

email = 'arun.rameshbabu@cnl.na.ca'
email.removeprefix('arun.rameshbabu')
email.removesuffix('@cnl.na.ca')

# Find elements
at_index = email.find('@')
email.removeprefix(email[:at_index])

# Spitting Strings
split_string = string1.split()
string1.split('is')
dates = '12/3/95'
dates.split('/')
name = 'BMW 330i Turbo'
name.split(' ', 1)

# Joining Strings
'/'.join(split_string)
' '.join(split_string)
' waka waka '.join(split_string)


#Files
_2d_array = [['Arun Rameshbabu', 'dshklr6e5643'],
            ['Brad Jones', '846756wrjysj'],
            ['Casey Kim', '56wjm734w5trj']]

import csv

with open('passwords.csv', 'w', newline='') as file:
    csv_fh = csv.writer(file)
    csv_fh.writerows(_2d_array)

with open('passwords2.csv', 'w') as file2:
    for row in _2d_array:
        string_to_write = ','.join(row) + '\n'
        file2.write(string_to_write)
        
        
with open('passwords.csv', 'r', newline='') as file:
    csv_fh = csv.reader(file)
    temp = []
    for row in csv_fh:
        temp.append(row)
    print(temp)

with open('passwords2.csv') as file2:
    lines = file2.readlines()
    temp = []
    for line in lines:
        row = line.strip('\n').split(',')
        temp.append(row)
    print(temp)
        




























        