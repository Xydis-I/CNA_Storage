# -*- coding: utf-8 -*-
import sys

startNum = 1


def Recursion(start, end):
    if start <= end:
        print(start * f"{start}")
        counter = start + 1
        Recursion(counter, end)


def RunRecursion():
    try:
        userInput = input("Recursion End Value: ")
        Recursion(1, int(userInput))

    except Exception:
        print("Please Enter Value Int #.")

    finally:
        userInput = input("Continue(y/n)?: ")
        if userInput == "y":
            RunRecursion()
        elif userInput == "n":
            sys.exit()


RunRecursion()
