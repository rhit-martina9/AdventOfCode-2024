connections = {}
input = []

with open("day23.txt") as file:
    for line in file:
        line = line.replace("\n","")
        pair = line.split("-")
        input.append(pair)
        if pair[0] not in connections:
            connections[pair[0]] = set()
        connections[pair[0]].add(pair[1])

        if pair[1] not in connections:
            connections[pair[1]] = set()
        connections[pair[1]].add(pair[0])

def find_3_groups():
    out = set()
    for connection in input:
        same = connections[connection[0]].intersection(connections[connection[1]])
        for value in same:
            out.add(','.join(sorted([connection[0],connection[1],value])))
    return list(out)

def part_one():
    count = 0
    for group in find_3_groups():
        group = group.split(",")
        if group[0][0] == "t" or group[1][0] == "t" or group[2][0] == "t":
            count += 1
    return count

def find_k_clique(k):
    possible_inputs = 0
    out = set()
    for connection in input:
        same = connections[connection[0]].intersection(connections[connection[1]])
        for value in same:
            to_add = sorted([connection[0],connection[1],value])
            out.add(','.join(to_add))
    return list(out)

def is_clique(list):
    if len(list) < 2:
        return True
    for i in list[1:]:
        if i not in connections[list[0]]:
            return False
    return is_clique(list[1:])

def get_k_clique(k,clique,to_check,checked):
    if len(clique) + len(to_check) + len(checked) < k:
        return []
    if len(to_check) == 0 and len(checked) == 0:
        if len(clique) == k:
            return clique
        else:
            return []
    
    while len(to_check) > 0:
        node = to_check.pop()
        out = get_k_clique(k,
                            clique.union([node]), 
                            to_check.intersection(connections[node]),
                            checked.intersection(connections[node]))
        if out != []:
            return out
        checked = checked.union([node])
    return []
    
def part_two():
    max_k = max(len(connections[key]) for key in connections)
    nodes = set(connections.keys())
    for k in range(max_k,0,-1):
        k_clique = get_k_clique(k,set(),nodes,set())
        if k_clique != []:
            return ','.join(sorted(k_clique))
    return "Unknown"

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    