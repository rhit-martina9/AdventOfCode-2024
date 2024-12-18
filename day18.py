input = []

X, fallen = 70, 1024
# X, fallen = 6, 12
with open("day18.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = line.split(",")
        input.append((int(pair[1]),int(pair[0])))

def make_grid(count):
    grid = [['' for _ in range(X+1)] for _ in range(X+1)]
    for i in range(count):
        space = input[i]
        grid[space[0]][space[1]] = "#"
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
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] > X or neighbor[1] > X:
                continue
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

def part_one():
    grid = make_grid(fallen)
    return len(a_star((0,0),(X,X),grid))

def part_two():
    i = fallen+1
    grid = make_grid(i)
    while a_star((0,0),(X,X),grid) != -1:
        i += 1
        # grid[input[i][0]][input[i][1]] = "#"
        grid = make_grid(i)
    return (input[i-1][1],input[i-1][0])

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    