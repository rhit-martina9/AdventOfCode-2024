registers = {}
processes = []
import re

with open("day24.txt") as file:
    seen_break = False
    for line in file:
        line = line.replace("\n","")
        if seen_break:
            segment = line.split(" ")
            if segment[0] < segment[2]:
                processes.append((segment[1],segment[0],segment[2],segment[4]))
            else:
                processes.append((segment[1],segment[2],segment[0],segment[4]))
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

def run_processes(registers,old_processes):
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
    return get_long_wire(values,"z")

def part_one():
    return run_processes(registers,processes)

def get_z_strs():
    zs = []
    for i in range(sum(1 if v[0] == "z" else 0 for v in outputs.keys())):
        if i < 10:
            zs.append("z0" + str(i))
        else:
            zs.append("z" + str(i))
    return zs

outputs = {v[3]:v for v in processes}
outputs = dict(sorted(outputs.items()))
def find_origins(wire: str, outputs, include_regs = True, seen=set()) -> set[str]:
    if wire[0] in ["x", "y"] and not include_regs:
        return set()
    if wire not in outputs:
        return {wire}
    if wire in seen:
        return set()
    
    process = outputs[wire]
    return find_origins(process[1],outputs,include_regs, seen.union({wire})).union(find_origins(process[2],outputs,include_regs, seen.union({wire}))).union({wire})

def get_definition(z,outs=outputs,seen=set()):
    if z not in outs:
        return z
    if z in seen:
        return ''
    line = outs[z]
    left = get_definition(line[1],outs,seen.union([z]))
    right = get_definition(line[2],outs,seen.union([z]))
    if right < left:
        return "(" + line[0] + " " + right + " " + left + ")"
    return "(" + line[0] + " " + left + " " + right + ")"

def shorten(s, replacements):
    check = True
    while check:
        check = False
        for exp in replacements:
            if exp in s:
                s = s.replace(exp,replacements[exp])
                check = True
    return s

def find_swaps(wrongs):
    out = []
    fixed = []
    out_processes = {x:outputs[x] for x in outputs}
    wrong_keys = list(wrongs.keys())
    for i in range(len(wrongs)):
        wi = wrong_keys[i]
        if wi in fixed:
            continue
        done = False
        for j in range(i+1,len(wrongs)):
            if done:
                break
            wj = wrong_keys[j]
            if wj in fixed:
                continue
            for val1 in wrongs[wi]:
                if done:
                    break
                for val2 in wrongs[wj]:
                    out_processes[val1], out_processes[val2] = out_processes[val2], out_processes[val1]
                    new_wrongs = get_wrongs(out_processes)
                    if wi not in new_wrongs and wj not in new_wrongs:
                        out.append(val1)
                        out.append(val2)
                        fixed.append(wj)
                        done = True
                        break
                    out_processes[val1], out_processes[val2] = out_processes[val2], out_processes[val1]
    if len(out) < len(wrong_keys):
        return "Adder with 2 wrongs"
    return ','.join(sorted(out))

def get_wrongs(outputs):
    exps = {}
    possible_wrongs = {}
    adder_pattern = ["\(XOR \(OR \(AND \w+ \w+\) \(AND x"," y","\)\) \(XOR x"," y","\)\)"]
    for z in range(len(zs)):
        pattern = adder_pattern[0] + zs[z-1][1:] + adder_pattern[1] + zs[z-1][1:] + adder_pattern[2] + zs[z][1:] + adder_pattern[3] + zs[z][1:] + adder_pattern[4]
        s = "" if z < 1 else shorten(get_definition(zs[z],outputs),exps[z-1])
        if z > 1 and z < len(zs)-1 and re.match(pattern, s) == None:
            possible_wrongs[z] = sorted(find_origins(zs[z],outputs,False).difference(find_origins(zs[z-1],outputs),find_origins(zs[z-2],outputs)),reverse=True)

        exps[z] = {}
        if z > 0:
            exps[z].update(exps[z-1])
        for a in find_origins(zs[z],outputs,False):
            if a not in exps:
                exp = outputs[a]
                exps[z]["(" + exp[0] + " " + exp[1] + " " + exp[2] + ")"] = a
                exps[z]["(" + exp[0] + " " + exp[2] + " " + exp[1] + ")"] = a
    return possible_wrongs

zs = get_z_strs()
def part_two():
    possible_wrongs = get_wrongs(outputs)
    return find_swaps(possible_wrongs)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())