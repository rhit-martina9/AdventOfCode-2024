input = []

with open("day12.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([*line])

def get_garden_spaces(garden,x0,y0):
    to_see = {(x0,y0)}
    spots = set()
    while len(to_see) > 0:
        current = to_see.pop()
        to_add = {(current[0]+dir[0],current[1]+dir[1]) for dir in [(0,1),(1,0),(0,-1),(-1,0)]}
        to_add = to_add.intersection(garden)
        to_add = to_add.difference(spots)
        to_add = filter(lambda x: x[0] >= 0 and x[0] < len(input) and x[1] >= 0 and x[1] < len(input[0]), to_add)
        to_add = filter(lambda x: input[x[0]][x[1]] == input[x0][y0], to_add)
        to_see = to_see.union(set(to_add))
        spots.add(current)
    return spots

def get_perimeter(plot):
    lines = []
    for space in plot:
        lines.append((space[0]+.5,space[1]))
        lines.append((space[0]-.5,space[1]))
        lines.append((space[0],space[1]+.5))
        lines.append((space[0],space[1]-.5))
    return list(filter(lambda v: lines.count(v) == 1,lines))

def part_one():
    total = 0
    data = []
    positions = {(i,j) for i in range(len(input)) for j in range(len(input[0]))}
    while len(positions) > 0:
        i,j = positions.pop()
        plants = get_garden_spaces(positions,i,j)
        data.append((len(plants),get_perimeter(plants),input[i][j])) # area_val, perimeter edges, plant
        total += len(plants)*len(data[-1][1])
        positions = positions.difference(plants)
    return data,total

def count_corners(sides,plant):
    count = 0
    for i in range(len(sides)):
        for j in range(i+1,len(sides)):
            if abs(sides[i][0]-sides[j][0]) == 0.5 and abs(sides[i][1]-sides[j][1]) == 0.5:
                if (sides[i][0]*2)%2 == 0: # Side I is vertical
                    x,y = sides[i],sides[j]
                else:
                    x,y = sides[j],sides[i]
                if input[x[0]][y[1]] == plant: # interior corner
                    count += 1
                elif input[int(2*y[0]-x[0])][int(2*x[1]-y[1])] == plant: # exterior corner
                    count += 1
    return count

def part_two(plots):
    total = 0
    for p in plots:
        total += p[0]*count_corners(p[1],p[2])
    return total

data,part_one_ans = part_one()
print("Answer to part 1:", part_one_ans)
print("Answer to part 2:", part_two(data))
    