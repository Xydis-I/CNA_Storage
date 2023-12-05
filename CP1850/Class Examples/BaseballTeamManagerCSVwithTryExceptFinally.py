# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett

Tommy,3B,1316,360
Mike,RF,563,168
Donovan,2B,1473,407
Buster,C,4575,1380

"""
import csv

file_location = 'lineup.csv'

def header(positions: list, file_location: str):
    print((63*"=") + "\n\t\t\t\t   Baseball Team Manager")
    menu_options()
    printPositions(positions)
    check_file(file_location)
    print(63*"=")

def menu_options():
    menuOptions = ["Display lineup","Add player","Remove player","Move player","Edit player position","edit player stats","Exit program\n"]
    print("\nMENU OPTIONS")
    for i, option in enumerate(menuOptions):
        print("%d - %s" % (i + 1,option))

def check_file(file_location): 
    try:
        with open(file_location) as file:
            file.readlines()
    except OSError:
        print("\nTeam data file counld not be found.\nA new file will be created.")
        with open(file_location, 'w') as file:
            file.writelines([])

def get_lineup() -> list:
    with open(file_location, 'r') as file:
        lineup = [l.split(',') for l in file.read().split('\n')]
        return lineup[:len(lineup) - 1]

def printPositions(positions: list):
    print("POSITIONS")
    for position in positions:
        if position == positions[-1]:
            print("%s" % position)
        else:
            print("%s" % position, end=", ")
            
def getLineupNumber(players: list,text: str) -> int:
    while True:
        lineupNum = input(text)
        if lineupNum.isnumeric():
            lineupNum = int(lineupNum) - 1
            if 0 <= lineupNum < len(players):
                return lineupNum
            else:
                print("Invalid number.")
        else:
            print("Invalid number.")
            
def getAtBats() -> int:
    while True:
        atBats = input("At bats: ")
        if atBats.isnumeric():
            atBats = int(atBats)
            if 0 > atBats > 600:
                print("Number must be in range 0 - 600")
            else:
                return atBats
        else:
            print("Invalid number.")
            
def getHits() -> int:
    while True:
        hits = input("Hits: ")
        if hits.isnumeric():
            hits = int(hits)
            if 0 > hits > 600:
                print("Number must be in range 0 - 600")
            else:
                return hits
        else:
            print("Invalid number.")
        
def displayLineup(players: list):
    print("\t\tPlayer\t\t\tPOS\t\tAB\t\tH\t\tAVG\n" + (63 * "-"))
    for i, player in enumerate(players):
        if len(player[0]) < 3:
            largeTab = 4
        elif len(player[0]) < 7:
            largeTab = 3
        elif len(player[0]) < 11:
            largeTab = 2
        else:
            largeTab = 1
        try:
            if int(player[3]) / int(player[2]) == 1.0:
                avg = "1.0"
            else:
                avg = str(round((int(player[3]) / int(player[2])),3)).rstrip('0')
        except ZeroDivisionError:
            avg = "0.0"
            
        print("%d \t\t%s %s%s \t %4s \t %4s \t\t%s" % (i + 1, player[0], largeTab*"\t", player[1], player[2], player[3], avg))
    print()   
            
def addPlayer(positions: list, players: list):
    while True:
        name = input("Name: ")
        if name.isalnum():
            break
        else:
            print("Enter valid name.")
    
    if len(name) > 14:
        name = name[:14]

    while True:
        position = input("Position: ").upper()
        if positions.count(position) == 1:
            atBats = getAtBats()
            hits = getHits()
            players.append([name, position, atBats, hits])
            with open(file_location, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(players)
            print("%s was added.\n" % name)
            break
        else:
            print("Invalid position. Try again.")
            printPositions(positions)
    
def removePlayer(players: list):
    lineupNum = getLineupNumber(players, "Lineup number: ")
    print("%s was removed." % players[lineupNum][0])
    with open(file_location, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([p for p in players if players.index(p) != lineupNum])
    
def movePlayer(players: list):
    currentLineNum = getLineupNumber(players, "Current lineup number: ")
    print("%s was selected." % players[currentLineNum][0])
    newLineNum = int(input("New lineup number: ")) - 1
    player = players.pop(currentLineNum)
    players.insert(newLineNum, player)
    with open(file_location, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(players)
    print("%s was moved.\n" % players[newLineNum][0])
    
def editPlayerPosition(positions: list, players: list):
    lineupNum = getLineupNumber(players, "Lineup number: ")
    print("You selected %s POS=%s." % (players[lineupNum][0], players[lineupNum][1]))
    while True:
        newPos = input("New position: ")
        if positions.count(newPos) == 1:
            players[lineupNum][1] = newPos
            with open(file_location, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(players)
            print("%s was updated.\n" % players[lineupNum][0])
            break      
        else:
            print("Invalid position. Try again.")
            printPositions(positions)
    
def editPlayerStats(players: list):
    lineupNum = getLineupNumber(players, "Lineup number: ")
    print("You selected %s AB=%s H=%s" % (players[lineupNum][0], players[lineupNum][2], players[lineupNum][3]))
    atBats = getAtBats()
    hits = getHits()
    players[lineupNum][2] = atBats
    players[lineupNum][3] = hits
    with open(file_location, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(players)
    print("%s was updated.\n" % players[lineupNum][0])
    
def userCommands(positions: list):
    while True:
        command = input("Menu Option: ")
        if command == "1":
            displayLineup(get_lineup())
        elif command == "2":
            addPlayer(positions, get_lineup())
        elif command == "3":
            removePlayer(get_lineup())
        elif command == "4":
            movePlayer(get_lineup())
        elif command == "5":
            editPlayerPosition(positions, get_lineup())
        elif command == "6":
            editPlayerStats(get_lineup())
        elif command == "7":
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.")    
            menu_options()
            

def main():
    positions = ("C","1B","2B","3B","SS","LF","CF","RF","P")
    
    header(positions, file_location)
    userCommands(positions)
    
if __name__ == "__main__":
    main()