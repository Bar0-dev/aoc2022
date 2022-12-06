stacks = open("stacks.txt", "r").read()
procedures = open("procedure.txt").read()
def parseStacks(stacksStr):
    lines = stacksStr.split('\n')[:-1]
    l_lines = len(lines)+1
    stacks = [[]*l_lines for i in range(l_lines)]
    for line in lines:
        for index, c in enumerate(line):
            if c == '[':
                stacks[int(index/((len(lines[0])+1)/9))].append(line[index+1])
    return stacks
stacksBy9000 = parseStacks(stacks)
stacksBy9001 = parseStacks(stacks)
for procedure in procedures.split('\n'):
    procedureArr = []
    for c in procedure:
        if c.isnumeric():
            procedureArr.append(int(c))
    if len(procedureArr) > 3:
        tens = procedureArr.pop(0)
        procedureArr[0] += tens*10
    toMove9000 = procedureArr[0]
    toMove9001 = procedureArr[0]
    while toMove9000>0:
        container = stacksBy9000[procedureArr[1]-1].pop(0)
        stacksBy9000[procedureArr[2]-1].insert(0,container)
        toMove9000 -= 1
    containersToMove = []
    for i in range(0, toMove9001):
        containersToMove.append(stacksBy9001[procedureArr[1]-1].pop(0))
    stacksBy9001[procedureArr[2]-1] = containersToMove + stacksBy9001[procedureArr[2]-1]
output9000 = ""
output9001 = ""
for stack in stacksBy9000:
    output9000 += stack[0]
for stack in stacksBy9001:
    output9001 += stack[0]

print(output9000, output9001)