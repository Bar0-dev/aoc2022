message = open('test.txt','r').read()
cBuff = []
toProcessBeforeMsg, uniqueCs = 0, 4
for i in range(0,2):
    print(uniqueCs)
    for index, c in enumerate(message):

        if index > (uniqueCs-1):
            cBuff = message[index-(uniqueCs-1):index]
            if(uniqueCs == 14):
                print(True if len(cBuff) == len(set(cBuff)) else False)
            if c not in cBuff and len(cBuff) == len(set(cBuff)):
                if not toProcessBeforeMsg:
                    toProcessBeforeMsg = index + 1
                    print(cBuff+c, toProcessBeforeMsg)
    uniqueCs = 14