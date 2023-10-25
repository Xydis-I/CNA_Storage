# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett
"""
from random import randint

def header():
    print("BLACKJACK!\nBlackjack payout is 3:2\nEnter 'x' for bet to exit\n")

def createDeck() -> list:
    deck = []
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    ranks = ["Ace", "King", "Queen", "Jack"] + [str(x) for x in range(10, 1, -1)]
    for suit in suits:
        for rank in ranks:
            if rank.isnumeric():
                value = int(rank)
            elif rank == "Ace":
                value = 11
            else:
                value = 10
            deck.append([suit, rank, value])
    return deck

def getStartMoney(prompt: str) -> float:
    while True:
        money = input(prompt)
        if money.isnumeric() and float(money) > 0:
            return float(money)
        else:
            print("Invalid value.\n")

def hitOrStand() -> bool:
    while True:
        choice = input("\nHit or stand? (h/s): ").lower()
        if choice == "h":
            return True
        elif choice == "s":
            return False
        else:
            print("Invalid selection.")

def displayCards(user: str, cards: list):
    print("\n%s CARDS:" % user)
    for card in cards:
        print("%s of %s" % (card[1], card[0]))
    print("Total: %d" % getTotal(cards))

def getTotal(hand: list) -> int:
    total = 0
    for card in hand:
        total += card[2]
    return total

def drawCard(deck: list) -> list:
    return deck.pop(randint(0, len(deck) - 1))

def dealCards(deck: list) -> (list, list):
    dealer = [drawCard(deck)]
    player = []
    for x in range(0, 2):
        card = drawCard(deck)
        aceHandling(card, player)
    return dealer, player

def aceHandling(card: list, cards: list):
    total = getTotal(cards)
    if card[1] == "Ace" and (total + 11) > 21:
        card[2] = 1
        cards.append(card)

    else:
        cards.append(card)

def gameLogic():
    startMoney = getStartMoney("Starting money: ")

    while True:
        deck = createDeck()
        betAmount = input("Bet amount: ")
        if betAmount.lower() == "x":
            break
        elif betAmount.isnumeric() and float(betAmount) > 0:
            betAmount = float(betAmount)
            dealerCards, playerCards = dealCards(deck)
            if getTotal(playerCards) == 21:
                startMoney += 2 * betAmount
                print("\nBlackjack!\nMoney: %.1f\n" % startMoney)
                break

            print("\nDEALER'S SHOW CARD:\n%s of %s" % (dealerCards[0][1], dealerCards[0][0]))

            displayCards("YOUR", playerCards)

            playing = hitOrStand()
            while playing:
                card = drawCard(deck)
                aceHandling(card, playerCards)
                displayCards("YOUR", playerCards)

                if getTotal(playerCards) > 21:
                    startMoney -= betAmount
                    print("\nBust!\nMoney: %.1f\n" % startMoney)
                    break

                if getTotal(playerCards) == 21:
                    startMoney += 2 * betAmount
                    print("\nBlackjack!\nMoney: %.1f\n" % startMoney)
                    break

                playing = hitOrStand()

            if not playing:
                while getTotal(dealerCards) < 17:
                    card = drawCard(deck)
                    aceHandling(card, dealerCards)
                displayCards("DEALER'S", dealerCards)

                print("\nYOUR POINTS:\t %d" % getTotal(playerCards))
                print("DEALER'S POINTS: %d" % getTotal(dealerCards))

                if getTotal(playerCards) > getTotal(dealerCards) or getTotal(dealerCards) > 21:
                    startMoney += betAmount
                    print("\nHooray! You win!\nMoney: %.1f\n" % startMoney)

                elif getTotal(playerCards) == getTotal(dealerCards):
                    print("\nTie!\nMoney: %.1f\n" % startMoney)

                else:
                    startMoney -= betAmount
                    print("\nBoo! You lose!\nMoney: %.1f\n" % startMoney)
        else:
            print("Invalid value.\n")

def main():
    header()
    gameLogic()
    print("\nBye!")

if __name__ == "__main__":
    main()
