registers = {}
processes = []

with open("day24.txt") as file:
    seen_break = False
    for line in file:
        line = line.replace("\n","")
        if seen_break:
            segment = line.split(" ")
            processes.append((segment[1],segment[0],segment[2],segment[4]))
        elif line == "":
            seen_break = True
        else:
            pair = line.split(": ")
            registers[pair[0]] = int(pair[1])

def evaluate(inst, r0, r1):
    if inst == "AND":
        return r0 & r1
    elif inst == "OR":
        return r0 | r1
    elif inst == "XOR":
        return r0 ^ r1

def get_long_wire(source, key):
    wire = {k:v for k,v in source.items() if k[0] == key}
    wire = dict(sorted(wire.items(),reverse=True))
    out = 0
    for cell in wire:
        out = out * 2 + wire[cell]
    return out
def get_long_wire_str(source, key):
    wire = {k:v for k,v in source.items() if k[0] == key}
    wire = dict(sorted(wire.items(),reverse=True))
    out = ""
    for cell in wire:
        out += str(wire[cell])
    return out

def run_processes(old_processes):
    values = {x:registers[x] for x in registers}
    procs = [x for x in old_processes]
    count = len(procs)
    while procs != [] and count > 0:
        proc = procs.pop(0)
        if proc[1] in values and proc[2] in values:
            values[proc[3]] = evaluate(proc[0],values[proc[1]],values[proc[2]])
            count = len(procs)
        else:
            procs.append(proc)
            count -= 1
    return values, get_long_wire(values,"z")

def part_one():
    return run_processes(processes)

outputs = {v[3]:v for v in processes}
def find_origins(wire: str) -> set[str]:
    if wire[0] in ["x", "y"]:
        return set()
    if wire not in outputs:
        return {wire}
    
    process = outputs[wire]
    return find_origins(process[1]).union(find_origins(process[2])).union({wire})

def get_wrong_pos(expected,result):
    out = []
    expected_bin = str(bin(expected))[2:]
    result_bin = str(bin(result))[2:]
    for i in range(len(expected_bin)):
        if expected_bin[i] != result_bin[i]:
            out.append(len(expected_bin)-1-i)
    return sorted(out)

def part_two_ends(values, eval_result):
    # print(get_long_wire_str(registers,"x"))
    # print(get_long_wire_str(registers,"y"))
    expected_z = get_long_wire(registers,"x") + get_long_wire(registers,"y")
    print("want:",str(bin(expected_z)[2:]))
    print("have:",str(bin(eval_result)[2:]))
    wrong_pos = get_wrong_pos(expected_z,eval_result)
    print(wrong_pos)
    
    for val in wrong_pos:
        if val < 10:
            val = "z0" + str(val)
        else:
            val = "z" + str(val)
        print(val, values[val], outputs[val])

    print()
    print('dkk', values['dkk'], outputs['dkk'])
    print('pbd', values['pbd'], outputs['pbd'])
    print()
    print('cpv', values['cpv'], outputs['cpv'])
    print('fwr', values['fwr'], outputs['fwr'])
    return "Unknown"

def get_pairs(count):
    out = []
    for i in range(count):
        for j in range(i+1,count):
            out.append([i,j])
    return out

def sets_are_disjoint(pairs: list[list]):
    for i in range(len(pairs)):
        for j in range(i+1,len(pairs)):
            if not set(pairs[i]).isdisjoint(set(pairs[j])):
                return False
    return True

def swap_brute_force(swaps, expected):
    pairs = get_pairs(len(swaps))
    pairs = [(swaps[i[0]],swaps[i[1]]) for i in pairs]
    new_processes = [list(x) for x in processes]
    for i in range(len(pairs)):
        print(i)
        new_processes[pairs[i][0]][3], new_processes[pairs[i][1]][3] = new_processes[pairs[i][1]][3], new_processes[pairs[i][0]][3]
        for j in range(i+1,len(pairs)):
            if pairs[i][0] == pairs[j][0]:
                continue
            if not sets_are_disjoint([pairs[i],pairs[j]]):
                continue
            new_processes[pairs[j][0]][3], new_processes[pairs[j][1]][3] = new_processes[pairs[j][1]][3], new_processes[pairs[j][0]][3]
            for k in range(j+1,len(pairs)):
                if pairs[j][0] == pairs[k][0]:
                    continue
                if not sets_are_disjoint([pairs[i],pairs[j],pairs[k]]):
                    continue
                new_processes[pairs[k][0]][3], new_processes[pairs[k][1]][3] = new_processes[pairs[k][1]][3], new_processes[pairs[k][0]][3]
                for l in range(k+1,len(pairs)):
                    if pairs[k][0] == pairs[l][0]:
                        continue
                    if not sets_are_disjoint([pairs[i],pairs[j],pairs[k],pairs[l]]):
                        continue
                    new_processes[pairs[l][0]][3], new_processes[pairs[l][1]] = new_processes[pairs[l][1]][3], new_processes[pairs[l][0]]
                    if expected == run_processes(new_processes):
                        return ','.join(sorted([new_processes[pairs[i][0]][3], new_processes[pairs[i][1]][3], new_processes[pairs[j][0]][3], new_processes[pairs[j][1]][3], 
                                    new_processes[pairs[k][0]][3], new_processes[pairs[k][1]][3], new_processes[pairs[l][0]][3], new_processes[pairs[l][1]][3]]))
                    new_processes[pairs[l][0]][3], new_processes[pairs[l][1]][3] = new_processes[pairs[l][1]][3], new_processes[pairs[l][0]][3]
                new_processes[pairs[k][0]][3], new_processes[pairs[k][1]][3] = new_processes[pairs[k][1]][3], new_processes[pairs[k][0]][3]
            new_processes[pairs[j][0]][3], new_processes[pairs[j][1]][3] = new_processes[pairs[j][1]][3], new_processes[pairs[j][0]][3]
        new_processes[pairs[i][0]][3], new_processes[pairs[i][1]][3] = new_processes[pairs[i][1]][3], new_processes[pairs[i][0]][3]
    return -1

def part_two_brute_force():
    expected_z = get_long_wire(registers,"x") & get_long_wire(registers,"y")
    return swap_brute_force(processes,expected_z)

def part_two(values, eval_result):
    # print(get_long_wire_str(registers,"x"))
    # print(get_long_wire_str(registers,"y"))
    expected_z = get_long_wire(registers,"x") + get_long_wire(registers,"y")
    print("want:",str(bin(expected_z)[2:]))
    print("have:",str(bin(eval_result)[2:]))
    wrong_pos = get_wrong_pos(expected_z,eval_result)
    print(wrong_pos)
    outputs = {v[3]:v for v in processes}
    outputs = dict(sorted(outputs.items()))

    possible_wrong = set()
    correct = set()
    for pos in range(len(str(bin(expected_z)))-2):
        if pos < 10:
            str_pos = "z0" + str(pos)
        else:
            str_pos = "z" + str(pos)
        # print(str_pos)
        # print(find_origins(str_pos),"\n")
        if pos in wrong_pos:
            possible_wrong = possible_wrong.union(find_origins(str_pos).difference(correct,set([str_pos])))
        else:
            correct = correct.union(find_origins(str_pos))
    for c in correct:
        possible_wrong = possible_wrong.difference(find_origins(c))
    possible_wrong = list(map(lambda x:processes.index(outputs[x]), possible_wrong))
    print(possible_wrong)
    print([processes[x] for x in possible_wrong])
    return swap_brute_force(possible_wrong,expected_z)

values, part_one_ans = part_one()
print("Answer to part 1:", part_one_ans)
print("Answer to part 2:", part_two(part_one_ans))