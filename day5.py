input1 = {str(i):[] for i in range(10,100)}
input2 = []

with open("day5.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = line.split("|")
        input1[pair[0]].append(pair[1])
with open("day5_2.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = line.split(",")
        input2.append(pair)

def can_be_after(num, values):
    return len([n for n in input1[num] if n in values]) == 0

def get_list_value(lst):
    return int(lst[int((len(lst)-1)/2)])

def is_sorted(line):
    for i in range(1,len(line)):
        if(not can_be_after(line[i], line[:i])):
            return False
    return True

incorrect = []
def part_one():
    total = 0
    for line in input2:
        if is_sorted(line):
            total += get_list_value(line)
        else:
            incorrect.append(line)
    return total

def sort_line(line):
    lst = [x for x in line]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if not can_be_after(lst[j],[lst[i]]):
                lst[i],lst[j] = lst[j],lst[i]
    return lst

def part_two():
    total = 0
    for line in incorrect:
        total += get_list_value(sort_line(line))
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    