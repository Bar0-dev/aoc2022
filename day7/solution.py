commandsRaw = open('filesystem.txt').read().split('\n')
filesystem = {'/':0}
location = []
sizeSum = 0
condition1= 100000
minReqMem = 30000000
deviceMem = 70000000

def createFolder(name, path, size):
    return {name: 'name', 'path': path, 'size': size }

def updateLocation(line, loc):
    if('..' in line):
        loc.pop(-1)
    elif('/' in line):
        loc.clear()
        loc = ['/']
    else:
        loc.append(line[5:]+'/')
    return loc

def filterFilesystem(filesystem):
    for index, path in enumerate(filesystem):
        if(path not in filesystem[index-1]):
            finalPath = path

def updateDownToRoot(filesystem, path, value):
    pathElements = path.split('/')[1:-1]
    localPath = '/'
    for element in pathElements:
        filesystem[localPath] += value
        localPath += element + '/'

getDirContent = False
for line in commandsRaw:
    if '$' in line:
        if 'cd' in line:
            location = updateLocation(line, location)
            getDirContent = False
            continue
        if 'ls' in line:
            getDirContent = True
            continue
    if getDirContent:
        if 'dir' in line:
            dirName = line.split(' ')[0]
            filesystem = filesystem | {"".join(location)+line.split(' ')[1]+'/' : 0}
        else:
            filesystem["".join(location)] += int(line.split(' ')[0])
for path, size in filesystem.items():
    if size:
        updateDownToRoot(filesystem, path, size)
for size in filesystem.values():
    if size < condition1:
        sizeSum += size
print(sizeSum)
memToFree = minReqMem-(deviceMem - filesystem['/'])
match = memToFree
for i in range(memToFree, minReqMem):
    if(match in filesystem.values()):
        print(match)
        break
    match += 1