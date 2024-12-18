input = []

with open("day4.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])

def getDir(x,y,count,dir):
    out = input[x][y]
    for i in range(1,count):
        x1 = x+i*dir[0]
        y1 = y+i*dir[1]
        if x1 < 0 or x1 > len(input)-1 or y1 < 0 or y1 > len(input[0])-1:
            return ''
        out += input[x1][y1]
    return out

def part_one():
    total = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != 'X':
                pass
            for dirI in range(3):
                for dirJ in range(3):
                    if getDir(i,j,4,[dirI-1,dirJ-1]) == 'XMAS':
                        total += 1
    return total

def part_two():
    total = 0
    for i in range(1,len(input)-1):
        for j in range(1,len(input)-1):
            if input[i][j] != 'A':
                continue
            if getDir(i-1,j-1,3,[1,1]) in ['MAS','SAM'] and getDir(i-1,j+1,3,[1,-1]) in ['MAS','SAM']:
                total += 1
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    