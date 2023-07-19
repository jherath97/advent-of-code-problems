from customQuicksort import quicksort

def getElvesFromInputFile():
    with open('2022\day1\input.txt', 'r') as file:
        lines = file.readlines()

    elves = []

    currentElf = 0
    currentElfRunningSum = 0
    for i in range(len(lines)):
        strVal = lines[i]
        
        if strVal != '\n':
            currentElfRunningSum += int(strVal.rstrip())
        else:
            elves.append([currentElf, currentElfRunningSum])
            currentElf += 1
            currentElfRunningSum = 0

    return elves

def getLargestElvesCalories(elves, count):
    length = len(elves)

    quicksort(elves, 0, length-1)
    
    sum = 0
    for i in range(length-1, length-count-1, -1):
        sum += elves[i][1]
    
    return sum