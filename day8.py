input = []

with open("day8.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])

def get_positions():
    positions = {}
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != ".":
                if input[i][j] not in positions:
                    positions[input[i][j]] = []
                positions[input[i][j]].append((i,j))
    for pos in positions:
        if len(positions[pos]) == 1:
            positions.pop(pos)
    return positions

def in_range(p):
    return p[0] >= 0 and p[1] >= 0 and p[0] < len(input) and p[1] < len(input[0])

def get_extension(pos,dir,n):
    out = []
    for _ in range(n):
        pos = (pos[0]+dir[0],pos[1]+dir[1])
        if not in_range(pos):
            break
        out.append(pos)
    return out

def find_antinodes(n):
    positions = get_positions()
    antinodes = set()
    for symbol in positions:
        pos = positions[symbol]
        for i in range(len(pos)):
            for j in range(i+1,len(pos)):
                dx,dy = pos[j][0]-pos[i][0],pos[j][1]-pos[i][1]
                for x in get_extension(pos[i],(-dx,-dy),n):
                    antinodes.add(x)
                for x in get_extension(pos[j],(dx,dy),n):
                    antinodes.add(x)
    return positions,antinodes

def part_one():
    positions,antinodes = find_antinodes(1)
    return len(antinodes)

def part_two():
    positions,antinodes = find_antinodes(len(input))
    for symbol in positions:
        for x in positions[symbol]:
            antinodes.add(x)
    return len(antinodes)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())    