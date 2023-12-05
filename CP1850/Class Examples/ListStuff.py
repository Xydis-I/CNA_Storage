# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:23:19 2023

@author: christian.barrett
"""
"""
from queue import LifoQueue

stack = LifoQueue(maxsize=3)
for i in range(0,3):
    stack.put(i)
    
print(stack.qsize())

"""

movies = ["The Dark Knight", 2005, 9.99]
type(movies)
str_objects_list = ['sword', 'hat', 'cat']
flt_objects_list = [48.0, 88.0, 100.0, 40.0]
empty_list_ex = []

scores = [0] * 10
flt_objects_list[0]
type(flt_objects_list[0])
type(movies[0])
type(movies[1])

flt_objects_list[-1]
flt_objects_list[-4]
#flt_objects_list[4] #Error

flt_objects_list[2] = 'Hello'
flt_objects_list[3] = False

movies.append(400)
movies.insert(2, "USA")
['car', 2, 40, 2005]

movies.remove("USA") # removes first instance found
flt_objects_list.pop() # removes last item if not given specific index

len(movies)
year = 2005
year in movies
year in str_objects_list
if year in movies:
    movies.append("Add this item")

for item in movies:
    print(item)
    
scores = [70, 80, 90, 100, 60]
total = 0
i = 0
while i < len(scores):
    total += scores[i]
    i+=1
print(total)

for j, item in enumerate(scores):
    print("%d - %d" % (j,item))
    
cars = ["Vw", "Ford", "BMW", "Audi"]
prices = [30000, 15000, 40000, 35000]

for car, price in zip(cars, prices):
    print("%s - %d" % (car, price))
