import re
import numpy as np
registers = []
instructions = []

with open("day17.txt") as file:
    seen_break = False
    for line in file:
        line = line.replace("\n","")
        if line == "":
            seen_break = True
        elif seen_break:
            instructions = [*re.sub("\D","",line)]
            instructions = [int(x) for x in instructions]
        else:
            registers.append(int(re.findall("\d+",line)[0]))

def get_combo_operand(operand, regs):
    if operand < 4:
        return operand
    return regs[operand-4]

def perform_operation(opcode, operand, regs):
    out = ""
    jump = -1
    if opcode == 0:
        regs[0] = regs[0] >> get_combo_operand(operand,regs)
    elif opcode == 1:
        regs[1] = regs[1] ^ operand
    elif opcode == 2:
        regs[1] = get_combo_operand(operand,regs) & 7
    elif opcode == 3:
        if regs[0] != 0:
            jump = operand
    elif opcode == 4:
        regs[1] = regs[1] ^ regs[2]
    elif opcode == 5:
        out = get_combo_operand(operand,regs) & 7
    elif opcode == 6:
        regs[1] = regs[0] >> get_combo_operand(operand,regs)
    elif opcode == 7:
        regs[2] = regs[0] >> get_combo_operand(operand,regs)
    return regs, out, jump

def run_instructions(A=None):
    out = ""
    regs = [reg for reg in registers]
    if A != None:
        regs = [A,0,0] 
    ip = 0
    while ip < len(instructions)-1:
        regs,output,jump = perform_operation(instructions[ip],instructions[ip+1],regs)
        if output != "":
            out += str(output) + ","
        if jump != -1:
            ip = jump
        else:
            ip += 2
    return out[:-1]

def part_one():
    return run_instructions()

def get_out(value,A,b0):
    return list(filter(lambda v: int(run_instructions(v+A*8)[0]) == value,range(b0,8)))

def part_two():
    out = [0]
    for inst in instructions[::-1]:
        new_out = []
        for num in out:
            for n in get_out(inst,num, 1 if out[0] == 0 else 0):
                new_out.append(num*8 + n)
        out = new_out
    return min(out)

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    