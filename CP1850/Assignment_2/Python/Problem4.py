# Assignment 2 - Problem 4
# Import get_int from Problem1 to promote code reuse.
from Problem1 import get_int
from random import randint


def header():
    print("The Wizard Inventory program")


def command_menu():
    print("\nCOMMAND MENU\nwalk - Walk down the path\nshow - Show all items"
          "\ndrop - Drop an item\nexit - Exit program")


# Reads inventory file, creates one if not found.
def check_inventory() -> list:
    try:
        with open("wizard_inventory.txt", "r") as inv:
            return inv.read().splitlines()
    except FileNotFoundError:
        with open("wizard_inventory.txt", "w") as inv:
            inv.writelines([])
            return []


# Display enumerated inventory if there is at least one item in inventory.
def show_inventory(inv: list):
    if len(inv) < 1:
        print("Inventory is empty.")
    else:
        for n, item in enumerate(inv, 1):
            print("%d. %s" % (n, item))


# Returns a random unique item when called.
def random_item() -> str:
    with open("wizard_all_items.txt", "r") as items:
        availableItems = list(set(items.read().splitlines()) - set(check_inventory()))
        return availableItems[randint(0, len(availableItems) - 1)]


# Add entered item into inventory.
def add_item(item: str):
    with open("wizard_inventory.txt", "a") as inv:
        return inv.write(item)


# Remove item from inventory based on index.
def drop_item(index: int, items: list):
    with open("wizard_inventory.txt", "w") as inv:
        print("You dropped %s" % items[index])
        inv.writelines([item + "\n" for n, item in enumerate(items) if n != index])


# Walk forward presents player with a random item they can pick up if their inventory is not full(max=4).
def walk(item):
    print("While walking down a path, you see %s." % item)
    if input("Do you want to grab it? (y/n): ").lower() == "y":
        if len(check_inventory()) < 4:
            add_item(item + "\n")
            print("You picked up %s." % item)
        else:
            print("You can't carry any more items. Drop something first.")


# Logic for user interactions.
def game_logic():
    while True:
        command = input("\nCommand: ").lower()
        if command == "walk":
            walk(random_item())
        elif command == "show":
            show_inventory(check_inventory())
        elif command == "drop":
            inv = check_inventory()
            if len(inv) < 1:
                print("Inventory is empty.")
                continue
            drop_item((get_int("Number: ", 1, len(inv)) - 1), check_inventory())
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid Command.")


def main():
    header()
    command_menu()
    game_logic()


if __name__ == "__main__":
    main()
