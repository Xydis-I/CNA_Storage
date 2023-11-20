# Assignment 2 - Problem 3
# Import get_int from Problem1 to promote code reuse.
from Problem1 import get_int


def header():
    print("Welcome to Tic Tac Toe")


# Draw gameboard to console.
def display_game(gameboard: list):
    print("\n+---+---+---+")
    for row in gameboard:
        print("| %s | %s | %s |\n" % (row[0], row[1], row[2]) + "+---+---+---+")


# Check rows for a winner using set length.
def check_rows(gameboard: list) -> bool:
    for row in gameboard:
        if len(set(row)) == 1 and row[0] != " ":
            return True
    return False


# Check columns for a winner using set length.
def check_columns(gameboard: list) -> bool:
    for column in range(2):
        if len({gameboard[0][column], gameboard[1][column], gameboard[2][column]}) == 1 and gameboard[0][column] != " ":
            return True
    return False


# Check diagonals for a winner using set length.
def check_diagonals(gameboard: list) -> bool:
    if len({gameboard[0][0], gameboard[1][1], gameboard[2][2]}) == 1 and gameboard[0][0] != " ":
        return True
    if len({gameboard[0][2], gameboard[1][1], gameboard[2][0]}) == 1 and gameboard[0][2] != " ":
        return True
    return False


# Handle players turn actions.
def player_turn(gameboard: list, player: str):
    print("\n%s's turn" % player)
    while True:
        row = get_int("Pick a row (1, 2, 3): ", 1, 3) - 1
        column = get_int("Pick a column (1, 2, 3): ", 1, 3) - 1
        if gameboard[row][column] == " ":
            break
        else:
            print("Please select empty cell.")
    gameboard[row][column] = player


# Check win states
def check_state(gameboard: list) -> bool:
    return check_rows(gameboard) or check_columns(gameboard) or check_diagonals(gameboard)


# Logic for user interactions and displaying game
def game_logic():
    gameboard = [[" " for _ in range(3)] for _ in range(3)]
    turnCounter = 0
    while True:
        display_game(gameboard)
        player_turn(gameboard, "X")
        currentTurn = "X"
        turnCounter += 1
        if check_state(gameboard) or turnCounter == 9:
            display_game(gameboard)
            break
        display_game(gameboard)
        player_turn(gameboard, "O")
        currentTurn = "O"
        turnCounter += 1
        if check_state(gameboard):
            display_game(gameboard)
            break
    if turnCounter < 9:
        print("\n%s wins!" % currentTurn)
    else:
        print("\nTie!")
    print("\nGame over!")


def main():
    header()
    game_logic()


if __name__ == "__main__":
    main()
