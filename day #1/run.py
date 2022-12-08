import sys

def print_hi():
    elfId = 1;
    elfMaxId = 1;
    with open(sys.argv[1]) as f:
        allCalories = list(f.read().splitlines())
    print(allCalories)

    overallMax = 0
    maxCalories = 0;
    overallMaxesArr = [];
    for caloriesIndex, cal in enumerate(allCalories):
        if allCalories[caloriesIndex] == '':
            if maxCalories > overallMax:
                overallMax = maxCalories
                elfMaxId = elfId

            print('elfId = ', elfId, ' maxCalories = ', maxCalories, 'elfMaxId = ', elfMaxId, 'current overall = ', overallMax);
            elfId += 1
            overallMaxesArr.append(maxCalories)
            maxCalories = 0
        else:
            maxCalories += int(allCalories[caloriesIndex])

    print('elfMaxId = ', elfMaxId)
    overallMaxesArr = sorted(list(set(overallMaxesArr)))
    print('overallMax = ', overallMaxesArr)
    print('overallMax = ', overallMaxesArr[-1] + overallMaxesArr[-2] + overallMaxesArr[-3])


if __name__ == '__main__':
    print_hi()


