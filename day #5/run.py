import sys

def print_hi():

    with open(sys.argv[1]) as f:
        cargo = list(f.read().splitlines())

    cargoParsed = []
    stacksIndexes = []
    stacksDict = {}
    moves = []

    for cargoLine in cargo:
        if '1   ' in cargoLine:
            stacksIndexes = cargoLine.split()
        elif 'move' in cargoLine:
            parsedMove = cargoLine.split()
            moves.append([int(parsedMove[1]), int(parsedMove[3]), int(parsedMove[5])])
        else:
            cargoParsed.append(cargoLine)

    for stackIndex in stacksIndexes:
        stacksDict[int(stackIndex)] = []

    for crate in cargoParsed:
        for index, singleCrate in enumerate(crate.split()):
            if singleCrate != '[.]':
                stacksDict[index+1].insert(0, singleCrate)


    for move in moves:
        movedCrates = stacksDict[move[1]][-move[0]:]
        stacksDict[move[1]] = stacksDict[move[1]][:-move[0]]
        # movedCrates.reverse()
        stacksDict[move[2]].extend(movedCrates)

    message = ''
    for stacksDictKey in stacksDict.keys():
        message += str(stacksDict[stacksDictKey][-1])
    message = message.replace("[", '')
    message = message.replace("]", '')
    print(message)

if __name__ == '__main__':
    print_hi()


