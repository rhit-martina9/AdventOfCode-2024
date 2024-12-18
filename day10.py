input = []

with open("day10.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])
        input[-1] = [int(x) for x in input[-1]]

def get_positions():
    pos_map = {i:[] for i in range(10)}
    for i in range(len(input)):
        for j in range(len(input[i])):
            pos_map[int(input[i][j])].append((i,j))
    return pos_map

def get_reachable_heads(pos,score):
    if pos[0] < 0 or pos[0] >= len(input) or pos[1] < 0 or pos[1] >= len(input[0]):
        return set()
    if input[pos[0]][pos[1]] != score:
        return set()
    if score == 9:
        return {pos}
    out = set()
    for move in [(0,1),(1,0),(0,-1),(-1,0)]:
        out = out.union(get_reachable_heads((pos[0]+move[0],pos[1]+move[1]),score+1))
    return out

def part_one():
    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                total += len(get_reachable_heads((i,j),0))
    return total

def get_paths_to_heads(pos,score):
    if pos[0] < 0 or pos[0] >= len(input) or pos[1] < 0 or pos[1] >= len(input[0]):
        return 0
    if input[pos[0]][pos[1]] != score:
        return 0
    if score == 9:
        return 1
    out = 0
    for move in [(0,1),(1,0),(0,-1),(-1,0)]:
        out += get_paths_to_heads((pos[0]+move[0],pos[1]+move[1]),score+1)
    return out

def part_two():
    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                total += get_paths_to_heads((i,j),0)
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    