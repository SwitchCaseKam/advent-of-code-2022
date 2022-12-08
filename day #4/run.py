import sys

def print_hi():

    with open(sys.argv[1]) as f:
        areasPairs = list(f.read().splitlines())

    numOfPairs = 0
    overlapCounter = 0
    for areasPair in areasPairs:
        pair = areasPair.split(',')
        pair1 = pair[0]
        pair1Down = int(pair1.split('-')[0])
        pair1Up = int(pair1.split('-')[1])

        pair1Range = [*range(pair1Down, pair1Up+1)]
        pair2 = pair[1]
        pair2Down = int(pair2.split('-')[0])
        pair2Up = int(pair2.split('-')[1])
        pair2Range = [*range(pair2Down, pair2Up+1)]

        if set(pair1Range).issubset(pair2Range) or set(pair2Range).issubset(pair1Range):
            numOfPairs += 1
        if set(pair1Range).intersection(pair2Range):
            overlapCounter += 1
    print(numOfPairs)
    print(overlapCounter)

if __name__ == '__main__':
    print_hi()


