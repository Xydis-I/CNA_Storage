# -*- coding: utf-8 -*-

import random

def Header():
    print("BLACKJACK!\nBlackjack payout is 3:2\nEnter 'x' for bet to exit")
    
def Betting():
    while True:
        startMoney = input("\nStarting money:\t  ")
        if startMoney.isnumeric():
            startMoney = float(startMoney)
        else:
            print("Please enter valid number.")
            continue
            
        if startMoney < 5:
            print("The minimum amount of starting money is $5.")
            continue
        if startMoney > 10000:
            print("The maximum amount of starting money is $10,000.")
            continue
        
        while True:
            bet = input("\nBet amount: ")
            if bet.isnumeric():
                bet = float(bet)
            elif bet.lower() == "x":
                print("Bye!")
                break
            else:
                print("Please enter valid number.")
                continue
            
            betType = random.randint(1,100)
            if 96 <= betType <= 100:
                startMoney += bet * 1.5
                print("You got a blackjack!.\nMoney: %.1f" % startMoney)
            elif 59 <= betType <= 95:
                startMoney += bet
                print("You won.\nMoney: %.1f" % startMoney)
            elif 50 <= betType <= 58:
                print("You pushed.\nMoney: %.1f" % startMoney)
            elif 1 <= betType <= 49:
                startMoney -= bet
                print("You lost.\nMoney: %.1f" % startMoney)
            else:
                print("Not a valid option. Please try again.\n")
        break

def main():
    Header()
    Betting()

if __name__ == "__main__":        
    main()  