patterns = []
towels = []
import re

with open("day19.txt") as file:
    isTowels = False
    for line in file:
        line = line.replace("\n","")
        if isTowels:
            towels.append(line)
        elif line == "":
            isTowels = True
        else:
            patterns = sorted(line.split(", "), key=lambda v: (len(v),v))

def check_pattern(towel,patterns):
    pattern = "^(" + "|".join(patterns) + ")+$"
    return re.match(pattern,towel) != None

def shorten(patterns):
    out = []
    for i in range(len(patterns)):
        other_patterns = patterns[:i] + patterns[i+1:]
        pattern = "^(" + "|".join(other_patterns) + ")+$"
        if re.match(pattern,patterns[i]) == None:
            out.append(patterns[i])
    return out


def part_one():
    simple_patterns = shorten(patterns)
    print(simple_patterns)
    possible_towels = []
    for towel in towels:
        if check_pattern(towel,simple_patterns):
            possible_towels.append(towel)
    return possible_towels, len(possible_towels)

impossible_towels = []
pattern_counts = {}

def find_counts(towel,patterns):
    if towel == "":
        return 1
    if towel in impossible_towels:
        return None
    if towel in pattern_counts:
        return pattern_counts[towel]
    
    count = 0
    for pattern in patterns[towel[0]]:
        if towel[:len(pattern)] == pattern:
            pattern_count = find_counts(towel[len(pattern):],patterns)
            if pattern_count != None:
                count += pattern_count
    if count == 0:
        impossible_towels.append(towel)
        return None
    else:
        pattern_counts[towel] = count
        return count

def part_two():
    pattern_groups = {i:list(filter(lambda v: v[0] == i,patterns)) for i in ['r', 'g', 'w', 'b', 'u']}
    count = 0
    for towel in towels:
        towel_count = find_counts(towel,pattern_groups)
        if towel_count != None:
            count += find_counts(towel,pattern_groups)
    return count

possible_towels, part_one_ans = part_one()
print("Answer to part 1:", part_one_ans)
print("Answer to part 2:", part_two())
    