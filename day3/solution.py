def letToScore(let):
    n = ord(let)
    if(n<91):
        return n-38
    if(n>96):
        return n-96
f = open("rucksacks.txt", "r")
rucksacks = f.read().split('\n')
groups, group = [], []
member, score1, score2 = 0, 0, 0
for rucksack in rucksacks:
    l = len(rucksack)
    comp1, comp2 = rucksack[0:int(l/2)], rucksack[int(l/2):l]
    for l in comp1:
        if(l in comp2):
            score1 += letToScore(l)
            break
    group.append(rucksack)
    member += 1
    if(member > 2):
        member = 0
        groups.append(group)
        group = []
for grp in groups:
    for l in grp[0]:
        if(l in grp[1] and l in grp[2]):
            score2 += letToScore(l)
            break
print(score1, score2)