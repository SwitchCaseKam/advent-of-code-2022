import sys


def print_hi():
    with open(sys.argv[1]) as f:
        treesGrid = list(f.read().splitlines())
    visibleTreesNumber = 2 * len(treesGrid) + 2 * len(treesGrid[0]) - 4

    for i, treeRow in enumerate(treesGrid):
        if (i != 0) and (i != len(treesGrid) - 1):
            for l, singleTree in enumerate(treeRow):
                if (l != 0) and (l != len(treesGrid) - 1):
                    left = treeRow[0:l]
                    right = treeRow[l+1:]
                    top = ''.join([treesGrid[z][l] for z in range(0, i)])
                    bottom = ''.join([treesGrid[z][l] for z in range(i+1, len(treesGrid))])
                    if all(int(i) < int(singleTree) for i in left) or all(int(i) < int(singleTree) for i in right) or \
                            all(int(i) < int(singleTree) for i in top) or all(int(i) < int(singleTree) for i in bottom):
                        visibleTreesNumber += 1
    print(visibleTreesNumber)


if __name__ == '__main__':
    print_hi()
