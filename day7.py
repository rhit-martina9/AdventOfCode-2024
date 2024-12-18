input = []

with open("day7.txt") as file:
    for line in file:
        line = line.replace("\n","")
        info = line.split(": ")
        input.append((int(info[0]),[int(x) for x in info[1].split(" ")]))

def can_be_calculated(result,line):
    if len(line) == 1:
        return result == line[0]
    num1,num2 = line[0],line[1]
    if can_be_calculated(result,[num1+num2]+line[2:]):
        return True
    return can_be_calculated(result,[num1*num2]+line[2:])

def part_one():
    total = 0
    for line in input:
        if can_be_calculated(line[0],line[1]):
            total += line[0]
    return total

def can_be_calculated2(result,line):
    if len(line) == 1:
        return result == line[0]
    num1,num2 = line[0],line[1]
    if can_be_calculated2(result,[num1+num2]+line[2:]):
        return True
    if can_be_calculated2(result,[num1*num2]+line[2:]):
        return True
    return can_be_calculated2(result,[int(str(num1)+str(num2))]+line[2:])

def part_two():
    total = 0
    for line in input:
        if can_be_calculated2(line[0],line[1]):
            total += line[0]
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    