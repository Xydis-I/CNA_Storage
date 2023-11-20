# Assignment 2 - Problem 1

def header():
    print("Prime Number Checker")


# Add all factors of inputted number to list, if there's only 2 its Prime, more than that and it's not prime.
def prime_checker():
    factors = []
    num = get_int("\nPlease enter an integer between 1 and 5000: ", 1, 5000)
    for x in range(1, num + 1):
        if num % x == 0:
            factors.append(x)
    if len(factors) > 2:
        print("%d is NOT a prime number.\nIt has %d factors:" % (num, len(factors)), *factors)
    else:
        print("%d is a prime number." % num)


# Quick little int parse intended to prevent ValueErrors from user inputs that I'll be reusing throughout.
def get_int(prompt: str, start: int = 0, stop: int = 0) -> int:
    while True:
        userInput = input(prompt)
        if userInput.isnumeric():
            if start <= int(userInput) <= stop:
                return int(userInput)
        print("Invalid number. Please try again.")


def main():
    header()
    while True:
        prime_checker()
        if input("\nTry again? (y/n): ").lower() != "y":
            break
    print("\nBye!")


if __name__ == "__main__":
    main()
