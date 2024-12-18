import re
input = ""

with open("day3.txt") as file:
    for line in file:
        input += line

def part_one():
    total = 0
    for mul in re.findall("mul\(\d+,\d+\)",input):
        nums = mul[4:-1].split(",")
        total += int(nums[0])*int(nums[1])
    return total

def part_two():
    total = 0
    new_input = input.split("do()")
    for str in new_input:
        if str.find("don't()") > -1:
            str = str[:str.find("don't()")]
        for mul in re.findall("mul\(\d+,\d+\)",str):
            nums = mul[4:-1].split(",")
            total += int(nums[0])*int(nums[1])
    return total

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    