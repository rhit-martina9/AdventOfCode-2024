input = []

with open("day20.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])

def make_shortcut(posX,posY):
    if input[posX][posY] != "#":
        return None
    walls = sum(1 if input[dir[0]+posX][dir[1]+posY] == "#" else 0 for dir in dirs)
    if walls != 2:
        return None
    grid = [[x for x in line] for line in input]
    grid[posX][posY] = "."
    return grid

def reconstruct(cameFrom, current):
    path = []
    while current in cameFrom:
        current = cameFrom[current]
        if current not in path:
            path = [current] + path
    return path

dirs = [(0,1), (1,0),(0,-1),(-1,0)]
def a_star(start, goal, grid):
    openSet = [start]
    dist = lambda v: abs(goal[0] - v[0]) + abs(goal[1] - v[1])
    cameFrom = {}
    gScore = {start: 0}
    fScore = {start: dist(start)}

    while len(openSet) > 0:
        openSet = sorted(openSet, key=lambda v: fScore[v])
        current = openSet.pop(0)
        if current[0] == goal[0] and current[1] == goal[1]:
            return reconstruct(cameFrom, current)
        
        for dir in dirs:
            neighbor = (current[0]+dir[0],current[1]+dir[1])
            if grid[neighbor[0]][neighbor[1]] == "#":
                continue
            tentative_gScore = gScore[current] + 1
            if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + dist(neighbor)
                if neighbor not in openSet:
                    openSet.append(neighbor)
    return -1

def find_space(value):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == value:
                return (i,j)
    return -1

def part_one():
    start = find_space("S")
    end = find_space("E")
    og_score = len(a_star(start,end,input))
    short = []
    for i in range(1,len(input)-1):
        for j in range(1,len(input)-1):
            new_grid = make_shortcut(i,j)
            if new_grid == None:
                continue
            new_score = len(a_star(start,end,new_grid))
            if new_score <= og_score - 100:
                short.append((i,j))
    return len(short)

def part_two():
    return "Unknown"

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    