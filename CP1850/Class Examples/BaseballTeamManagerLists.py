# -*- coding: utf-8 -*-
"""
Author: C. C. Barrett
"""

def header(positions: list):
    menuOptions = ["Display lineup","Add player","Remove player","Move player","Edit player position","edit player stats","Exit program\n"]
    print((63*"=") + "\n\t\t\t\t   Baseball Team Manager\nMENU OPTIONS")
    for i, option in enumerate(menuOptions):
        print("%d - %s" % (i + 1,option))
    printPositions(positions)
    print(63*"=")

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
        elif len(player[0]) < 6:
            largeTab = 3
        elif len(player[0]) < 11:
            largeTab = 2
        else:
            largeTab = 1
            
        if player[3] / player[2] == 1.0:
            avg = "1.0"
        else:
            avg = str(round((player[3] / player[2]),3)).rstrip('0')
        
        print("%d \t\t%s %s%s \t\t%d \t\t%d \t\t%s" % (i + 1, player[0], largeTab*"\t", player[1], player[2], player[3], avg))
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
            print("%s was added.\n" % name)
            break
        else:
            print("Invalid position. Try again.")
            printPositions(positions)
    
def removePlayer(players: list):
    lineupNum = getLineupNumber(players, "Lineup number: ")
    print("%s was removed." % players[lineupNum][0])
    players.pop(lineupNum)
    
def movePlayer(players: list):
    currentLineNum = getLineupNumber(players, "Current lineup number: ")
    print("%s was selected." % players[currentLineNum][0])
    newLineNum = int(input("New lineup number: ")) - 1
    player = players.pop(currentLineNum)
    players.insert(newLineNum, player)
    print("%s was moved.\n" % players[newLineNum][0])
    
def editPlayerPosition(positions: list, players: list):
    lineupNum = getLineupNumber(players, "Lineup number: ")
    print("You selected %s POS=%s." % (players[lineupNum][0], players[lineupNum][1]))
    while True:
        newPos = input("New position: ")
        if positions.count(newPos) == 1:
            players[lineupNum][1] = newPos
            print("%s was updated.\n" % players[lineupNum][0])
            break      
        else:
            print("Invalid position. Try again.")
            printPositions(positions)
    
def editPlayerStats(players: list):
    lineupNum = getLineupNumber(players, "Lineup number: ")
    print("You selected %s AB=%d H=%d" % (players[lineupNum][0], players[lineupNum][2], players[lineupNum][3]))
    atBats = getAtBats()
    hits = getHits()
    players[lineupNum][2] = atBats
    players[lineupNum][3] = hits
    print("%s was updated.\n" % players[lineupNum][0])
    
def userCommands(positions: list, players: list):
    while True:
        command = input("Menu Option: ")
        if command == "1":
               displayLineup(players)
            
        elif command == "2":
            addPlayer(positions, players)
                
        elif command == "3":
            removePlayer(players)
            
        elif command == "4":
            movePlayer(players)
            
        elif command == "5":
            editPlayerPosition(positions, players)
            
        elif command == "6":
            editPlayerStats(players)
            
        elif command == "7":
            print("Bye!")
            break
        
        else:
            print("Invalid Command.")      

def main():
    positions = ("C","1B","2B","3B","SS","LF","CF","RF","P")
    players = [["Joe", "P", 10, 2], ["Tom", "SS", 11, 4] ,["Ben", "3B", 9, 3]]
    
    header(positions)
    userCommands(positions, players)
    
if __name__ == "__main__":
    main()