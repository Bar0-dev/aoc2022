import numpy as np
trees = open('forest.txt').read().split()
visibleTrees = 0
scenicScoreMax = 0
def findMax(arr):
    if arr.size:
        return np.max(arr)
    return -1
def splitLine(l):
    arr = []
    for tree in l:
        arr.append(int(tree))
    return arr
def getDistance(tree, arr):
    if len(arr):
        indecies = []
        for i in range(tree, findMax(arr)+1):
            found = np.where(arr == i)
            if len(found[0]):
                indecies.append(found[0][0])
        if len(indecies):
            indecies.sort()
            return indecies[0]+1
        else:
            return arr.size
    return 1
trees = np.array([splitLine(line) for line in trees])
for y, line in enumerate(trees):
    for x, tree in enumerate(line):      
        left = trees[y:y+1,:x].flatten()
        leftMax = findMax(left)
        top = trees[:y, x:x+1].flatten()
        topMax = findMax(top)
        bottom = trees[y+1:, x:x+1].flatten()
        bottomMax = findMax(bottom)
        right = trees[y:y+1,x+1:].flatten()
        rightMax = findMax(right)
        if leftMax < tree or topMax < tree or bottomMax < tree or rightMax < tree:
            visibleTrees += 1
        left = np.flip(left)
        top = np.flip(top)
        scenicScore = getDistance(tree, left) * getDistance(tree, top) * getDistance(tree, right) * getDistance(tree, bottom)
        if scenicScore > scenicScoreMax:
            scenicScoreMax = scenicScore

print(visibleTrees, scenicScoreMax)