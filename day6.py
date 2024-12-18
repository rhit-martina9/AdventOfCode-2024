input = []

with open("day6.txt") as file:
    for i,line in enumerate(file):
        line = line.replace("\n","")
        if line.find('^') > -1:
            start = (i, line.find('^'))
        line = line.replace("^",".")
        input.append([*line])

def traverse(grid,start_pos,start_dir):
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    dir = start_dir
    current = (start_pos[0],start_pos[1])
    visited = set()
    visited_w_dir = set()
    while True:
        if (dir,current[0],current[1]) in visited_w_dir:
            return -1,-1
        else:
            visited_w_dir.add((dir,current[0],current[1]) )
        visited.add(current)
        next = (current[0]+dirs[dir][0],current[1]+dirs[dir][1])
        if next[0] < 0 or next[0] >= len(grid) or next[1] < 0 or next[1] >= len(grid[0]):
            break
        if grid[next[0]][next[1]] == ".":
            current = next
        elif grid[next[0]][next[1]] == '#':
            dir = (dir+1)%4
        else:
            print("ERROR")
            exit(0)

    # out = [[a for a in b] for b in input]
    # for pos in visited:
    #     out[pos[0]][pos[1]] = 'X'
    # out[start[0]][start[1]] = 'Y'
    # for x in out:
    #     print(''.join(x))
    return visited, len(visited)

def part_one():
    return traverse(input,start,0)

def part_two(v):
    count = 0
    grid = [[a for a in b] for b in input]
    for i in range(len(v)-1):
        grid[v[i+1][0]][v[i+1][1]] = "#"
        _,p1_ans = traverse(grid,start,0)
        if p1_ans == -1:
            count += 1
        grid[v[i+1][0]][v[i+1][1]] = "."
    return count

p1_visited,p1_ans = part_one()
print("Answer to part 1:", p1_ans)
print("Answer to part 2:", part_two(list(p1_visited)))
    