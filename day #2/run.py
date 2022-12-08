import sys

def getPointsFromGame(yourMove, opponentMove):
    if yourMove == 'X':
        if opponentMove == 'A':
            return 1 + 3
        elif opponentMove == 'B':
            return 1 + 0
        elif opponentMove == 'C':
            return 1 + 6
    elif yourMove == 'Y':
        if opponentMove == 'A':
            return 2 + 6
        elif opponentMove == 'B':
            return 2 + 3
        elif opponentMove == 'C':
            return 2 + 0
    elif yourMove == 'Z':
        if opponentMove == 'A':
            return 3 + 0
        elif opponentMove == 'B':
            return 3 + 6
        elif opponentMove == 'C':
            return 3 + 3

def mapAppropriateMove(opponentMove, gameResult):
    # A - rock
    # B - paper
    # C - scissors

    # x - lose
    # y - draw
    # z - win
    if opponentMove == 'A':
        if gameResult == 'X':
            return 3 + 0
        elif gameResult == 'Y':
            return 1 + 3
        elif gameResult == 'Z':
            return 2 + 6
    elif opponentMove == 'B':
        if gameResult == 'X':
            return 1 + 0
        elif gameResult == 'Y':
            return 2 + 3
        elif gameResult == 'Z':
            return 3 + 6
    elif opponentMove == 'C':
        if gameResult == 'X':
            return 2 + 0
        elif gameResult == 'Y':
            return 3 + 3
        elif gameResult == 'Z':
            return 1 + 6

def print_hi():

    with open(sys.argv[1]) as f:
        moves = list(f.read().splitlines())

    totalScore = 0;
    for move in moves:
        movesInRound = move.split(' ')
        print(mapAppropriateMove(movesInRound[0], movesInRound[1]))
        totalScore += mapAppropriateMove(movesInRound[0], movesInRound[1])
    print('totalScore = ', totalScore)

if __name__ == '__main__':
    print_hi()


