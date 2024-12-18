import re
from sympy import symbols
from sympy.matrices import Matrix
input = []

with open("day13.txt") as file:
    i = 0
    for line in file:
        line = line.replace("\n","")
        if i == 0:
            x = re.findall("[XY]\+(\d+)",line)
            input.append([(int(x[0]),int(x[1]))])
        elif i == 1:
            x = re.findall("[XY]\+(\d+)",line)
            input[-1].append((int(x[0]),int(x[1])))
        elif i == 2:
            x = re.findall("[XY]=(\d+)",line)
            input[-1].append((int(x[0]),int(x[1])))
        i = (i+1)%4
    
def part_one():
    total = 0
    for claw in input:
        a,b,prize = claw
        A = Matrix([[a[0],b[0]],[a[1],b[1]]])
        B = Matrix([prize[0],prize[1]])
        ans = A.solve(B)
        if int(ans[0]) == ans[0] and int(ans[1]) == ans[1]:
            total += int(ans[0]*3+ans[1])
    return total

def part_two():
    total = 0
    for claw in input:
        a,b,prize = claw
        A = Matrix([[a[0],b[0]],[a[1],b[1]]])
        B = Matrix([prize[0]+10000000000000,prize[1]+10000000000000])
        ans = A.solve(B)
        if int(ans[0]) == ans[0] and int(ans[1]) == ans[1]:
            total += int(ans[0]*3+ans[1])
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    