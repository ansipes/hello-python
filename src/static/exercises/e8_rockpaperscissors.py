moves = {
    "rock": ["crushes", "scissors"],
    "scissors": ["cuts", "paper"],
    "paper": ["covers", "rock"]
}


def getMove(name):
    move = input(f"{name}, enter one of the following (rock|paper|scissors): ")
    if move in moves:
        return move
    else:
        print("You did not enter a valid move.")
        return getMove(name)


def determineWinner(p1, p2):
    if (p1 == p2):
        print("Tie.")
    elif (moves[p1][1] == p2):
        print(f"Player One wins. ({p1} {moves[p1][0]} {p2})")
    elif (moves[p2][1] == p1):
        print(f"Player Two wins. ({p2} {moves[p2][0]} {p1})")
    else:
        print("Oops, something went wrong.")


print("Welcome to Rock, Paper, Scissors!")

while True:
    p1 = getMove("Player One")
    p2 = getMove("Player Two")

    determineWinner(p1, p2)

    if input("Would you like to play again? (y|N)") != "y":
        break

print("Thanks for playing! Goodbye.")
