message = open('/home/bartosz/projects/aoc2022/day6/message.txt','r').read()
cBuff = []
toProcessBeforeMsg = 0
uniqueCs = [4, 14]
for uniqC in uniqueCs:
    for index, c in enumerate(message):
        if index > (uniqC-1):
            cBuff = message[index-(uniqC-1):index]
            if c not in cBuff and len(cBuff) == len(set(cBuff)):
                if not toProcessBeforeMsg:
                    toProcessBeforeMsg = index + 1
                    print(cBuff+c, toProcessBeforeMsg)
    toProcessBeforeMsg=0