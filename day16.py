input = []

with open("day16.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])

dirs = [(0,1), (1,0),(0,-1),(-1,0)]

def reconstruct(cameFrom, current):
    path = []
    while current in cameFrom:
        current = cameFrom[current]
        if current not in path:
            path = [current] + path
    return path

def a_star(start,goal):
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
            if input[neighbor[0]][neighbor[1]] == "#":
                continue
            tentative_gScore = gScore[current]
            if current in cameFrom:
                if cameFrom[current][0] == current[0]-dir[0] and cameFrom[current][1] == current[1]-dir[1]:
                    tentative_gScore += 1
                else:
                    tentative_gScore += 1001
            else:
                if dir == (0,1):
                    tentative_gScore += 1
                else:
                    tentative_gScore += 1001
            if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + dist(neighbor)
                if neighbor not in openSet:
                    openSet.append(neighbor)
    return -1

def find_square(value):
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == value:
                return (i,j)
    return -1

def score(path):
    total = 1
    dir = (0,1)
    for i in range(1,len(path)):
        new_dir = (path[i][0]-path[i-1][0], path[i][1]-path[i-1][1])
        if new_dir == dir:
            total += 1
        else:
            total += 1001
            dir = new_dir
    return total

def part_one():
    S_spot = find_square('S')
    E_spot = find_square('E')
    path = a_star(S_spot,E_spot)
    return path, score(path)

def find_path(current, goal, visited, turns, moves):
    if current == goal:
        return [visited]
    if turns < 0 or moves < 0 or current == goal:
        return []
    
    out = []
    for dir in dirs:
        neighbor = (current[0]+dir[0],current[1]+dir[1])
        if input[neighbor[0]][neighbor[1]] == "#":
            continue
        if neighbor in visited:
            continue

        if visited != []:
            if visited[-1][0] == current[0]-dir[0] and visited[-1][1] == current[1]-dir[1]:
                turn = 0
            else:
                turn = 1
        else: 
            if dir == (0,1):
                turn = 0
            else:
                turn = 1
        out += find_path(neighbor, goal, visited + [(current)], turns - turn, moves - 1)
    return out

def part_two(path, score):
    S_spot = find_square('S')
    E_spot = find_square('E')
    paths = find_path(S_spot, E_spot, [], int((score - score % 1000)/1000), score % 1000)
    spaces = {E_spot}
    for path in paths:
        for space in path:
            spaces.add(space)
    return len(spaces)

best_path, part_one_ans = part_one()
print("Answer to part 1:", part_one_ans)
print(len(best_path))
print("Answer to part 2:", part_two(best_path, part_one_ans))
    