import sys

def print_hi():

    with open(sys.argv[1]) as f:
        rucksacks = list(f.read().splitlines())

    sum = 0
    for rucksack in rucksacks:
        firstHalf = [*rucksack[0:int(len(rucksack)/2)]]
        secondHalf = [*rucksack[int(len(rucksack)/2):int(len(rucksack))]]

        commonChar = list(set(firstHalf).intersection(secondHalf))[0]
        commonCharAscii = ord(commonChar);
        if commonCharAscii >= 97:
            sum += commonCharAscii - 96
        elif commonCharAscii <= 90:
            sum += commonCharAscii - 38

    print(sum)

if __name__ == '__main__':
    print_hi()


