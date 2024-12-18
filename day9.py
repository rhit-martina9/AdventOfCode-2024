with open("day9.txt") as file:
    input = file.readline()

def get_input():
    files = []
    empty = []
    pos = 0
    is_file = True
    for char in input:
        step = int(char)
        if step > 0:
            if is_file:
                files.append([pos+x for x in range(step)])
            else:
                empty.append([pos+x for x in range(step)])
            pos += step
        is_file = not is_file
    return files,empty

def move_files(old_files,old_empty):
    files = [[pos for pos in file] for file in old_files]
    empty = [[pos for pos in spot] for spot in old_empty]
    for i in range(len(files)-1,-1,-1):
        for j in range(len(files[i])-1,-1,-1):
            if empty[0] == []:
                empty = empty[1:]
            if files[i][j] < empty[0][0]:
                break
            files[i][j] = empty[0][0]
            empty[0] = empty[0][1:]
    return files

def get_checksum(files):
    total = 0
    for i in range(len(files)):
        for pos in files[i]:
            total += pos*i
    return total

def part_one():
    files, empty = get_input()
    moved_files = move_files(files,empty)
    return get_checksum(moved_files)

def move_blocks(old_files,old_empty):
    files = [[pos for pos in file] for file in old_files]
    empty = [[pos for pos in spot] for spot in old_empty]
    for i in range(len(files)-1,-1,-1):
        empty = list(filter(lambda v: v!=[],empty))
        if files[i][0] < empty[0][0]:
            break
        for j in range(len(empty)):
            if empty[j][0] < files[i][0] and len(files[i]) <= len(empty[j]):
                files[i] = empty[j][:len(files[i])]
                empty[j] = empty[j][len(files[i]):]
                break
    return files

def part_two():
    files, empty = get_input()
    moved_files = move_blocks(files,empty)
    return get_checksum(moved_files)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    