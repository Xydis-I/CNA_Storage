# -*- coding: utf-8 -*-

print("BLACKJACK!\nBlackjack payout is 3:2\nEnter 'x' for bet to exit\n")
startMoney = float(input("Starting money:\t  "))
while True:
    bet = input("\nBet amount: ")
    if bet.lower() == "x":
        print("bye!")
        break
    betType = input("Blackjack, win, push, or lose? (b/w/p/l): ")
    if betType.lower() == "b":
        startMoney += float(bet) * 1.5
        print("Money: %.1f" % startMoney)
    elif betType.lower() == "w":
        startMoney += float(bet)
        print("Money: %.1f" % startMoney)
    elif betType.lower() == "p":
        print("Money: %.1f" % startMoney)
    elif betType.lower() == "l":
        startMoney -= float(bet)
        print("Money: %.1f" % startMoney)
    else:
        print("Not a valid option. Please try again.\n")