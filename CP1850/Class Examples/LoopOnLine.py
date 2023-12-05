# -*- coding: utf-8 -*-
#Six Ways(Not Extensive):

#Refactor 1
x = 0
line1 = ""
while x < 10:
    print(line1, end = ("%d " % x))
    x+=1
    
print("\nThe loop has ended.")


#Refactor 2
y = 0
line2 = "\n"
while y < 10:
    line2 += ("%d " % y)
    y+=1
    
print(line2 + "\nThe loop has ended.")


#Refactor 3
z = 0
line3 = "\n"
while z < 10:
    line3 += "{} ".format(z)
    z+=1
    
print(line3 + "\nThe loop has ended.")


#Refactor 4
line4 = "\n"
for num in range(10):
    line4 += ("%d " % num)
    
print(line4 + "\nThe loop has ended.")


#Refactor 5
line5 = "\n"
for num in range(10):
    line5 += "{} ".format(num)
    
print(line5 + "\nThe loop has ended.\n")


#Refactor 6
print(*range(0,10))
print("The loop has ended.\n")


#Refactor 7
for num in range(10):
    print(num, end=" ")
print("\nThe loop has ended.")