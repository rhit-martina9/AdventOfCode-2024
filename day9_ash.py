def findFreeSpace(line, size, index):
    i = 1
    while i < index:
        if line[i] >= size:
            return i
        i += 2
    return -1

fileNums = []
line = []

def moveFile(index):
    global fileNums, line
    # print('moving file of length', line[index], 'index', index)
    ind = findFreeSpace(line, line[index], index)
    size = line[ind]
    if ind != -1:
        line = line[:ind] + [0, line[index], line[ind]-line[index]] + line[ind+1:index-1] + [line[index-1]+line[index]+line[index+1],0, 0] + line[index+2:]
        val = fileNums[int(index/2)]
        fileNums[int(index/2)] = 0
        fileNums = fileNums[:int(ind/2+1)] + [val] + fileNums[int(ind/2+1):]
        # print('moved to', ind, 'of length', size)
        # print(line)
        # print(fileNums)
        return 2
    return 0

with open('day9.txt') as file:
    line = list(map(lambda x: int(x), file.readline().strip())) + [0]
    # print(line)
    for i in range(int(len(line)/2)):
        fileNums += [i]
    # print(fileNums)
    i = len(line) - 2
    if i %2 == 1:
        i -= 1
    while i > 0:
        i += moveFile(i)
        i -= 2
    checksum = 0
    realIn = 0
    for i in range(len(line)):
        if i % 2 == 0:
            for ind in range(line[i]):
                checksum += realIn*fileNums[int(i/2)]
                realIn += 1
        else:
            for ind in range(line[i]):
                realIn += 1
    # print(line)
    # print(fileNums)
    print(checksum)