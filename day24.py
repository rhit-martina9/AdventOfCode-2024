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
        out = out *2 + wire[cell]
    return out
def get_long_wire_str(source, key):
    wire = {k:v for k,v in source.items() if k[0] == key}
    wire = dict(sorted(wire.items(),reverse=True))
    out = ""
    for cell in wire:
        out += str(wire[cell])
    return out

def part_one():
    values = {x:registers[x] for x in registers}
    procs = [x for x in processes]
    while procs != []:
        proc = procs.pop(0)
        if proc[1] in values and proc[2] in values:
            values[proc[3]] = evaluate(proc[0],values[proc[1]],values[proc[2]])
        else:
            procs.append(proc)
    return values, get_long_wire(values,"z")

outputs = list(map(lambda v: v[3],processes))
def find_origins(wire: str) -> set[str]: 
    if wire not in outputs:
        return {wire}
    
    process = processes[outputs.index(wire)]
    return find_origins(process[1]).union(find_origins(process[2])).union({wire})

def get_wrong_pos(expected,result):
    out = []
    expected_bin = str(bin(expected))[2:]
    result_bin = str(bin(result))[2:]
    for i in range(len(expected_bin)):
        if expected_bin[i] != result_bin[i]:
            out.append(len(expected_bin)-1-i)
    return sorted(out)

def get_process_from_output(wire):
    return processes[outputs.index(wire)]

def part_two(values, eval_result):
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
        print(val, values[val], get_process_from_output(val))

    print()
    print('dkk', values['dkk'], get_process_from_output('dkk'))
    print('pbd', values['pbd'], get_process_from_output('pbd'))
    print()
    print('cpv', values['cpv'], get_process_from_output('cpv'))
    print('fwr', values['fwr'], get_process_from_output('fwr'))
    return "Unknown"

values, part_one_ans = part_one()
print("Answer to part 1:", part_one_ans)
# print("Answer to part 2:", part_two(values, part_one_ans))
    