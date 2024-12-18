input = []
import re
import time
import pygame

X,Y = 103,101
# X,Y = 7,11
with open("day14.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input.append([int(x) for x in re.findall("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)",line)[0]])
        input[-1] = [(input[-1][1],input[-1][0]),(input[-1][3],input[-1][2])]
# print(input)

def move(bots):
    return [[((bot[0][0]+bot[1][0])%X,(bot[0][1]+bot[1][1])%Y),bot[1]] for bot in bots]

def coordinate_score(bots):
    split_x,split_y = int((X-1)/2),int((Y-1)/2)
    q1 = len(list(filter(lambda v: v[0][0] < split_x and v[0][1] < split_y ,bots)))
    q2 = len(list(filter(lambda v: v[0][0] > split_x and v[0][1] < split_y ,bots)))
    q3 = len(list(filter(lambda v: v[0][0] < split_x and v[0][1] > split_y ,bots)))
    q4 = len(list(filter(lambda v: v[0][0] > split_x and v[0][1] > split_y ,bots)))
    return q1*q2*q3*q4

def get_positions(bots):
    out = [[0 for _ in range(Y)] for _ in range(X)]
    for bot in bots:
        out[bot[0][0]][bot[0][1]] = 1
    return out

def print_grid(bots):
    for line in get_positions(bots):
        print(''.join(['X' if x == 1 else '.' for x in line]))
    print()

def part_one():
    bots = [bot for bot in input]
    for _ in range(100):
        bots = move(bots)
        # print(bots)
    return coordinate_score(bots)

def part_two():
    bots = [bot for bot in input]
    # for i in range(7790):
    #     bots = move(bots)
    # print_grid(bots)

    for i in range(13):
        bots = move(bots)
    # # for i in range(215):
    # #     bots = move(bots)
    for k in range(100):
        print_grid(bots)
        print(i+101*k+1)
        for j in range(101):
            bots = move(bots)
        time.sleep(1)
    return 0

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    