def make_file(num):
    file_contents = """input = []

with open("day""" + num + """.txt") as file:
    for line in file:
        line = line.replace("\\n","")
        pair = line.split(" ")

def part_one():
    return "Unknown"

def part_two():
    return "Unknown"

print("Answer to part 1:", part_one())
print("Answer to part 2:", part_two())
    """

    filename = f"day{num}.py"
    f = open(filename, "x")
    f.write(file_contents)
    f.close()

    filename = f"day{num}.txt"
    f = open(filename, "x")
    f.close()

for i in range(3,26):
    make_file(str(i))

