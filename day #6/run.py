import sys

def print_hi():

    with open(sys.argv[1]) as f:
        communicationSequence = list(f.read().splitlines())[0]
        # communicationSequence = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

    characterIndex = 0
    for charIndex, char in enumerate(communicationSequence):
        subSequenceList = list(communicationSequence[charIndex:charIndex+14])
        subSequenceSet = set(communicationSequence[charIndex:charIndex+14])
        if len(subSequenceList) == len(subSequenceSet):
            print(charIndex+14)
            break


if __name__ == '__main__':
    print_hi()


