input = []

with open("day2.txt") as file:
    for line in file:
        line = line.replace("\n","")
        lst = line.split(" ")
        input.append([int(e) for e in lst])

def isDecreasing(line):
    for i in range(len(line)-1):
        if line[i] <= line[i+1]:
            return False
    return True

def isIncreasing(line):
    for i in range(len(line)-1):
        if line[i] >= line[i+1]:
            return False
    return True

def withinRange(line):
    for i in range(len(line)-1):
        diff = abs(line[i] - line[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

def removeTest(line):
    for i in range(len(line)):
        ln = line[:i] + line[i+1:]
        if (isDecreasing(ln) or isIncreasing(ln)) and withinRange(ln):
            return True
    return False


def part_one():
    count = 0
    for line in input:
        if (isDecreasing(line) or isIncreasing(line)) and withinRange(line):
            count += 1
    return count

def part_two():
    count = 0
    for line in input:
        if (isDecreasing(line) or isIncreasing(line)) and withinRange(line):
            count += 1
        elif removeTest(line):
            count += 1
    return count

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    