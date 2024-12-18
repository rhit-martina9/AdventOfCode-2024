input = []

with open("day11.txt") as file:
    for line in file:
        line = line.replace("\n","")
        input = line.split(" ")

def blink(stones):
    out = {1:0}
    for stone in stones:
        if stone == 0:
            out[1] += stones[stone]
        elif len(str(stone)) % 2 == 1:
            big = stone*2024
            out[big] = out.get(big,0) + stones[stone]
        else:
            rock = str(stone)
            split = int(len(rock)/2)

            front = int(rock[:split])
            out[front] = out.get(front,0) + stones[stone]
            
            back = int(rock[split:])
            out[back] = out.get(back,0) + stones[stone]
    return out

def get_stones_count(state):
    total = 0
    for s in state:
        total += state[s]
    return total

def part_one():
    state = {int(x):1 for x in input}
    for _ in range(25):
        state = blink(state)
    return get_stones_count(state)

def part_two():
    state = {int(x):1 for x in input}
    for _ in range(75):
        state = blink(state)
    return get_stones_count(state)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    