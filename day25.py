locks = []
keys = []

with open("day25.txt") as file:
    i = 0
    check = True
    for line in file:
        line = line.replace("\n","")
        if line == "":
            check = True
        else:
            if check:
                lock = True if line[0] == "#" else False
                if lock:
                    locks.append([])
                else:
                    keys.append([])
                check = False

            if lock:
                locks[-1].append([*line])
            else:
                keys[-1].append([*line])

def convert_locks():
    out = []
    for lock in locks:
        lock_heights = [0 for _ in range(len(lock[0]))]
        for i in range(1,len(lock)):
            for j in range(len(lock[0])):
                if lock[i][j] == "#":
                    lock_heights[j] += 1
        out.append(lock_heights)
    return out

def convert_keys():
    out = []
    for key in keys:
        key_heights = [0 for _ in range(len(key[0]))]
        for i in range(len(key)-1):
            for j in range(len(key[0])):
                if key[i][j] == "#":
                    key_heights[j] += 1
        out.append(key_heights)
    return out

def check_fit(lock,key):
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True

def part_one():
    locks = convert_locks()
    keys = convert_keys()
    count = 0
    for lock in locks:
        for key in keys:
            if check_fit(lock,key):
                count += 1
    return count

def part_two():
    return "Unknown"

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    