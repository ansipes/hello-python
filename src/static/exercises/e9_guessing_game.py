import random

floor = 1
ceiling = 9

g = []
x = random.randint(floor, ceiling)


def warnIfOutOfRange(n, floor, ceiling):
    if (n < floor):
        print(f"Your guess is lower than the floor, which is {floor}")
        return

    if (n > ceiling):
        print(f"Your guess is higher than the ceiling, which is {ceiling}")
        return


def warnIfDuplicateGuess(n, g):
    if (n in g):
        print("You have already guessed this number.")

    g.append(n)


def giveHint(n, x):
    if (n > x):
        print("Your guess is too high.")
        return

    if (n < x):
        print("Your guess is too low.")
        return


def summary(x, g):
    print("")
    print(f"The random number was: {x}")
    print(f"You guessed {len(g)} time{('', 's')[len(g) > 1]}.")
    print(f"Here are you guesses:")
    print(g)


print(
    f"I've picked a random number between {floor} and {ceiling}. Can you guess it?")
while True:
    i = input("Guess a number: ")
    if (i == "exit"):
        print("You lose!")
        break

    n = int(i)

    warnIfOutOfRange(n, floor, ceiling)

    warnIfDuplicateGuess(n, g)

    if (n == x):
        print("You win!")
        break

    giveHint(n, x)

summary(x, g)
