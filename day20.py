input = []

with open("day20.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])

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

def make_dist_path(path):
    out = {}
    for i in range(len(path)):
        out[path[i]] = len(path)-i
    return out

def get_walls_in_range(center, steps):
    spaces = set()
    openSet = [center]
    seen = set()
    while openSet != []:
        current = openSet.pop()
        seen.add(current)
        for dir in dirs:
            neighbor = (dir[0] + current[0], dir[1] + current[1])
            if neighbor in seen:
                continue
            if neighbor[0] < 0 or neighbor[0] >= len(input) or neighbor[1] < 0 or neighbor[1] >= len(input[0]):
                continue
            dist = abs(neighbor[0]-center[0]) + abs(neighbor[1]-center[1])
            if dist > steps:
                continue
            if input[neighbor[0]][neighbor[1]] != "#" and dist > 1:
                spaces.add(neighbor)
            openSet.append(neighbor)
    return spaces

def part_one():
    start = find_space("S")
    end = find_space("E")
    path = a_star(start,end,input) + [end]
    dist_path = make_dist_path(path)
    total = 0
    for step in path:
        shortcuts = get_walls_in_range(step,2)
        for cut in shortcuts:
            saved_time = dist_path[step] - dist_path[cut] - 2
            if saved_time >= 100:
                total += 1
    return total

def part_two():
    start = find_space("S")
    end = find_space("E")
    path = a_star(start,end,input) + [end]
    dist_path = make_dist_path(path)
    total = 0
    for step in path:
        shortcuts = get_walls_in_range(step,20)
        for cut in shortcuts:
            dist = abs(step[0]-cut[0]) + abs(step[1]-cut[1])
            saved_time = dist_path[step] - dist_path[cut] - dist
            if saved_time >= 100:
                total += 1
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    