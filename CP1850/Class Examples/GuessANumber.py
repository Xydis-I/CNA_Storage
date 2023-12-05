# -*- coding: utf-8 -*-
from random import randint

def Header():
    print("Guess the Number!\n\nI'm thinking of a number from 1 to 10\n")

def Guessing():
    answer = randint(1, 10)
    attempt = 0
    while True:
        guess = int(input("Your guess: "))
        attempt += 1
        if guess < answer:
            print("Too low.")
        elif guess > answer:
            print("Too high.")
        else:
            print("You guessed it in %d tries." % attempt)
            break
            
    if input("\nWould you like to play again? (y/n): ").lower() == "y":
        Guessing()

def main():
    Header()
    Guessing()
    print("\nBye!")
    
if __name__ == "__main__":
    main()