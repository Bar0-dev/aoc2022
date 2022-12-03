shape2score = {"AX" : 1, "BY" : 2, "CZ" : 3}
beats = {"AX" : "CZ", "BY" : "AX", "CZ" : "BY"}
draws = {"A" : "X", "B" : "Y", "C" : "Z"}
XYZ2score = {"X" : 0, "Y" : 3, "Z" : 6}
def dictFind(s, d):
    for key in d.keys():
        if(s in key):
            return d[key]
    return False
f = open("strategy.txt", "r")
score1, score2 = 0, 0
games = f.read().split('\n')
for game in games:
    score1 += dictFind(game[2], shape2score)
    if(game[0] in dictFind(game[2], beats)):
        score1 += 6
    elif(draws[game[0]] == game[2]):
        score1 += 3
    if(game[2] == "X"):
        score2 += shape2score[dictFind(game[0], beats)]
    elif(game[2] == "Z"):
        score2 += shape2score[dictFind(dictFind(game[0], beats), beats)]
    else:
        score2 += dictFind(game[0], shape2score)
    score2 += XYZ2score[game[2]]
print(score1, score2)