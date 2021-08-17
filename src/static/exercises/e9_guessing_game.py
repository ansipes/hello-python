import random

floor = 1
ceiling = 9

g = []
x = random.randint(floor, ceiling)


def warnIfOutOfRange(n):
    if (n > ceiling):
        print(f"Your guess is higher than the ceiling, which is {ceiling}")
        return

    if (n < floor):
        print(f"Your guess is lower than the floor, which is {floor}")
        return


def warnIfDuplicateGuess(n):
    if (n in g):
        print("You have already guessed this number.")

    g.append(n)


def giveHint(n):
    if (n > x):
        print("Your guess is too high.")
        return

    if (n < x):
        print("Your guess is too low.")
        return


def summary():
    print(f"The random number was: {x}")
    print(f"You guess {len(g)} times.")
    print(f"Here are you guesses:")
    print(g)


print("I've picked a random number between 1 and 9. Can you guess it?")
while True:
    i = input("Guess a number: ")
    if (i == "exit"):
        print("You lose!")
        break

    n = int(i)

    warnIfOutOfRange(n)

    warnIfDuplicateGuess(n)

    if (n == x):
        print("You win!")
        break

    giveHint(n)

summary()
