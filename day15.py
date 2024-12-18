grid = []
moves = []

with open("day15.txt") as file:
    at_moves = False
    for line in file:
        line = line.replace("\n","")
        if at_moves:
            moves += [*line]
        elif line == "":
            at_moves = True
        else:
            grid.append([*line])

def get_location(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == "@":
                return (i,j)

def do_move(old_state, move, loc):
    dir = get_dir(move)
    state = [[x for x in line] for line in old_state]
    if state[loc[0]+dir[0]][loc[1]+dir[1]] == "#":
        return state, loc
    if state[loc[0]+dir[0]][loc[1]+dir[1]] == ".":
        state[loc[0]+dir[0]][loc[1]+dir[1]] = state[loc[0]][loc[1]]
        state[loc[0]][loc[1]] = "."
        return state, (loc[0]+dir[0],loc[1]+dir[1])
    
    state,_ = do_move(state, move, (loc[0]+dir[0],loc[1]+dir[1]))
    
    if state[loc[0]+dir[0]][loc[1]+dir[1]] == ".":
        state[loc[0]+dir[0]][loc[1]+dir[1]] = state[loc[0]][loc[1]]
        state[loc[0]][loc[1]] = "."
        return state, (loc[0]+dir[0],loc[1]+dir[1])
    else:
        return state, loc

def get_gps_sum(state):
    total = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 'O':
                total += 100*i+j
    return total

def get_gps_sum2(state):
    total = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '[':
                total += 100*i+j
    return total

def get_dir(move):
    if move == "^":
        return (-1,0)
    elif move == ">":
        return (0,1)
    elif move == "v":
        return (1,0)
    elif move == "<":
        return (0,-1)

def part_one():
    state = [[x for x in line] for line in grid]
    loc = get_location(state)
    for move in moves:
        state,loc = do_move(state,move,loc)
    return get_gps_sum(state)

def rock_move(old_state, move, loc):
    state = [[x for x in line] for line in old_state]
    if move == "<":
        state, _ = do_move2(state, move, loc)
        if state[loc[0]][loc[1]] == '.':
            state[loc[0]][loc[1]] = ']'
            state[loc[0]][loc[1]+1] = '.'
        return state
    elif move == ">":
        state, _ = do_move2(state, move, (loc[0],loc[1]+1))
        if state[loc[0]][loc[1]+1] == '.':
            state[loc[0]][loc[1]+1] = '['
            state[loc[0]][loc[1]] = '.'
        return state

    state1, _ = do_move2(state, move, loc)
    if state1[loc[0]][loc[1]] == ".":
        state2, _ = do_move2(state1, move, (loc[0],loc[1]+1))
        if state2[loc[0]][loc[1]+1] == '.':
            return state2
    return state


def do_move2(old_state, move, loc):
    dir = get_dir(move)
    state = [[x for x in line] for line in old_state]
    if state[loc[0]+dir[0]][loc[1]+dir[1]] == "#":
        return state, loc
    elif state[loc[0]+dir[0]][loc[1]+dir[1]] == ".":
        state[loc[0]+dir[0]][loc[1]+dir[1]] = state[loc[0]][loc[1]]
        state[loc[0]][loc[1]] = "."
        return state, (loc[0]+dir[0],loc[1]+dir[1])
    elif state[loc[0]+dir[0]][loc[1]+dir[1]] == "[":
        state = rock_move(state, move, (loc[0]+dir[0],loc[1]+dir[1]))
    else:
        state = rock_move(state, move, (loc[0]+dir[0],loc[1]+dir[1]-1))
    
    if state[loc[0]+dir[0]][loc[1]+dir[1]] == ".":
        state[loc[0]+dir[0]][loc[1]+dir[1]] = state[loc[0]][loc[1]]
        state[loc[0]][loc[1]] = "."
        return state, (loc[0]+dir[0],loc[1]+dir[1])
    else:
        return state, loc

def new_grid(g):
    out = []
    for i in range(len(g)):
        out.append([])
        for j in range(len(g[0])):
            if g[i][j] == "#":
                out[-1].append("#")
                out[-1].append("#")
            if g[i][j] == "O":
                out[-1].append("[")
                out[-1].append("]")
            if g[i][j] == ".":
                out[-1].append(".")
                out[-1].append(".")
            if g[i][j] == "@":
                out[-1].append("@")
                out[-1].append(".")
    return out

def part_two():
    state = new_grid(grid)
    loc = get_location(state)
    for move in moves:
        state,loc = do_move2(state,move,loc)
    return get_gps_sum2(state)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    