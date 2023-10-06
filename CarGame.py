# -*- coding: utf-8 -*-
"""
    Author: C. C. Barrett
"""


# Examples of structure for while, if, elif, else, for, range, and plenty of def statements

# Basic Types
#   String -> Anything Contained Within Quotation Marks.    ex.     "Something like this"
#   Int -> Any Whole Number                                 ex.     25
#   Float -> Any Floating Point Value                       ex.     25.252525252525252525
#   Bool -> True or False

# Basic Casting/Parsing
#   float("10.5")  =>  10.5
#   float(10)  =>  10.0
#   int("6")  =>  6
#   int(8.1)  =>  8
#   int(8.9)  =>  8

# Structure of a def example
#       def [Name]([Parameter Name]:[Input Annotation]) -> [Output Annotation]
#
#       An annotation just tells you what the expected type should be and is written as :[type]

# This is a definition(also called a function) that is used to create the divider whenever
# it is called upon. It takes an int (aka whole) number as an input and returns a string of equal signs '='
# of that length. Length should be of type 'int' so length is annotated with :int. It outputs a string to the whole
# line can end with '-> str' to annotate its return type. Also, a dif that only does one thing can be written as one
# line, you do not have to do this if you think it'll cause confusion.
def Divider(length: int) -> str: return length * "="


# This is a definition(also called a function) that is used to create the Header for the console program.
# It makes use of the 'Divider()' to quickly create separators and print the title, the resulting output is:
# ============================================
# 				The Car Game
# ============================================
def Header():
    print("\n" + Divider(44) + "\n\t\t\t\tThe Car Game\n" + Divider(44))


# This is a definition(also called a function) that is used to calculate the distance the car has travelled.
# It takes three(3) input parameters, gear(a string), speed(a float), and time(a float).
# It returns(outputs) of type float and is annotated with '-> float'
def CalculateDistance(gear: str, speed: float, time: float) -> float:
    # if [condition]
    if gear.lower() == "d":
        return speed * time
    # elif [condition]
    elif gear.lower() == "n":
        return 0
    # else does not require or even take a condition
    elif gear.lower() == "r":
        return -speed * time


# This is a definition(also called a function) that prompts (or questions) the user with an 'input()'
# An input should preferably be stored and also ask a question, formatted as [variable] = input([question])
# For the sake of example you can think of a variable as a box to store things in. Now, you may notice the
# code below looks a little different, in Python you can very easily return multiple things at the same time.
# This is called a 'Tuple' type, essentially a little list or a box with multiple things in it. This is a
# little beyond what has been taught as of the time of writing, but it may help you understand how things work
# so I've chosen to include it, it may also help you more easily understand lists later on.
def Prompts() -> (str, float, float):
    # [variable] = input([question])
    gear = input("What Gear Is The Car In? (D/N/R):\t\t")
    # [variable] = input([question])
    speed = float(input("How Fast Are You Driving? (kph):\t\t"))
    # [variable] = input([question])
    time = float(input("How Many Hours Did You Drive? (Hours):\t"))
    return gear, speed, time


# This is a definition(also called a function) that handles the logic loop for our script.
# As it is car themed it firsts asks to start the car, this creates a variable called 'key'
# which is of 'Boolean' type (aka 'True' or 'False'). Then the 'key' variable (boolean) is used as the
# condition for the 'While' loop which serves as our ignition. Once the car is running it then uses the 'Prompt()'
# function to ask for current 'gear', 'speed', and 'time' spent driving. Since it uses a 'Tuple' type we can quickly
# assign all three variables, remember you can do this anyway you like, a 'Tuple' is just my own preference. The
# three(3) variables are then sent to 'CalculateDistance()' to do the math and return the result(a float) that we
# assume to be km for simplicity. Finally, it asks the user if they would like to continue driving, the distance
# is NOT saved between runs in this example but that is definitely a change we could choose to make if we wish.
def Driving():
    # Key       [variable] = input([question])
    key = input("Would You Like To Start The Car? (y/n):\t").lower() == "y"

    # Ignition
    # while [condition]
    while key:
        gear, speed, time = Prompts()
        distance = CalculateDistance(gear, speed, time)

        # Output Current Gear & Math for distance
        print("\nCurrent Gear:\t\t%s\nDistance Traveled:\t%.2fkm\nToll Booths Past:\t%d" % (gear.capitalize(), distance, TollBooths(distance)))

        # Short Continue Prompt - Combines Three(3) Previous Techniques
        # 'if [condition]' used in combination with 'input([question])'
        # The 'input()' serves as part of the condition.
        # Syntax wise this could be on one line, however, you shouldn't put 2 statements(if & break) on the same line
        if input("\nKeep Driving? (y/n): ").lower() != "y":
            break

# This is a definition(also called a function) that counts the toll booths that the car passes every 5km.
# This isn't meant to be a good example of how to do that, it's just an excuse to throw a 'for' loop and
# a 'range()' into this script because I didn't write a problem for that originally.
# range([start], [stop])
# for [item] in [items]
# In this case [item] is a number from a range(or list) of numbers which serves as the [items].
# distance is a float when it needs to be an int, as such we need to cast or parse it with 'int()'
# distance can also be negative sometimes so absolute aka 'abs()' is used to make it positive.
#                                                     i.e. abs(-10) => 10 and abs(10) => 10
# The '+1' is because a range will always stop one short of the number you give it.     i.e. range(1,10) will give 1 - 9
def TollBooths(distance: float) -> int:
    counter = 0
    for num in range(1, int(abs(distance))+1):
        if num % 5 == 0:
            counter += 1
    return counter


# This is a definition(also called a function) that handles Game Overs, mostly just here for a little bit of fun.
# It prints/outputs as:
# Game Over!
# Play Again? (y/n):
def GameOver():
    # if [condition]
    if input("\nGame Over!\nPlay Again? (y/n): ").lower() == "y":
        # Sure you could create yet another nested loop for the whole script to sit in but do you need to?
        # More than likely you should have everything inside a 'main()' to keep things clean, so why not
        # just call it like any other function to start off fresh. Best practice is to reduce unnecessary
        # nesting whenever possible, but it's also not something to stress over right now, just useful to
        # keep in mind.
        Main()


# Once you've broken down the rest of your code into clean functions you'll need somewhere to call them from,
# that's where the 'main()' comes in. A nice neat place to call everything, and then only one function call
# at the bottom of the script.
def Main():
    Header()
    Driving()
    GameOver()


# The function call itself.
Main()


# Additional Notes:
#   Single Responsibility Principle (SRP)
#       -> The idea that any single object or function should be made to handle one specific task.
#           That is to say it's best practice that each one should have a clear singular use.
#
#   String Formatting
#       ->testString = "World!"
#         print(f"Hello {testString}")
#         print("Hello {}".format(testString))
#         print("Hello %s" % testString)
#
#         The three(3) lines above all do the same thing, they are just different methods for formatting a string.
#         Best to pick the one you find easiest to learn/remember for now.
#
#   .lower() is your friend when prompting for inputs
#
#   a += b is a useful shorthand for a = a + b, can also use  ' -= '   ' *= '   ' /= '
#
#   The computer always does exactly what you told it to do, if something isn't working as you expected take the time
#   to read it to yourself in plain english or explain it to yourself as if talking to a stranger

