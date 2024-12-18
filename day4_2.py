import re
input = ''

with open("day4.txt") as file:
    lineLen = 0
    for line in file:
        line = line.replace("\n","")
        lineLen = len(line)
        input += '000' + line + '000'
    lineLen += 6
    input = '0'*(lineLen*3) + input + '0'*(lineLen*3)

def part_one():
    total = 0
    total += len(re.findall('XMAS',input))
    total += len(re.findall('SAMX',input))
    for i in range(3):
        total += len(re.findall('(?=(X.{'+str(lineLen-i)+'}M.{'+str(lineLen-i)+'}A.{'+str(lineLen-i)+'}S))',input))
        total += len(re.findall('(?=(S.{'+str(lineLen-i)+'}A.{'+str(lineLen-i)+'}M.{'+str(lineLen-i)+'}X))',input))
    return total

def part_two():
    total = 0
    total += len(re.findall('(?=(M.M.{'+str(lineLen-3)+'}.A..{'+str(lineLen-3)+'}S.S))',input))
    total += len(re.findall('(?=(M.S.{'+str(lineLen-3)+'}.A..{'+str(lineLen-3)+'}M.S))',input))
    total += len(re.findall('(?=(S.M.{'+str(lineLen-3)+'}.A..{'+str(lineLen-3)+'}S.M))',input))
    total += len(re.findall('(?=(S.S.{'+str(lineLen-3)+'}.A..{'+str(lineLen-3)+'}M.M))',input))
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    