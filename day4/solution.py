f = open("sections.txt", "r")
pairs = f.read().split('\n')
fullOverlapPairs = 0
overlapPairs = 0
for pair in pairs:
    [[idS1, idE1],[idS2, idE2]]= [map(int,elf.split('-')) for elf in pair.split(',')]
    if((idS1>=idS2 and idE1<=idE2) or (idS2>=idS1 and idE2<=idE1)):
        fullOverlapPairs += 1
    if((idE1 >= idS2 and idS1 <=idS2) or (idS2 <= idS1 and idE2 >= idS1)):
        overlapPairs += 1
print(fullOverlapPairs)
print(overlapPairs)