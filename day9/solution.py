import numpy as np
moves = open('moves.txt', 'r').read().split('\n')
test = open('test.txt', 'w')
dir2uv = {'U':[0,1], 'R':[1,0], 'D':[0,-1], 'L':[-1,0]}
knots = 10
rope = np.zeros((knots, 4))
tailPositions = []
def moveRope(dir, amnt, rope, tailPositions):
    for i in range(0, amnt):
        for index, knot in enumerate(rope):
            h = knot[:2]
            t = knot[2:]
            if not index:
                h = h + dir2uv[dir]
            else:
                h = rope[index-1,2:]
            htVector = h-t
            if np.max(htVector) > 1 or np.min(htVector) < -1 or abs(htVector[0]*htVector[1]) > 1:
                angle = np.arctan2(htVector[1], htVector[0])*180/np.pi
                if int(angle) in [-90, 0, 90, 180]:
                    t = t+dir2uv[dir]
                elif angle > 90:
                    t = t+[-1,1]
                elif angle > 0:
                    t = t+[1,1]
                elif angle < -90:
                    t = t+[-1, -1]
                elif angle < 0:
                    t = t+[1,-1]
                if index==rope.shape[0]-1:
                    tailPositions.append('{} {}\n'.format(t[0],t[1]))
            rope[index] = np.append(h, t)
    return rope
for move in moves:
    [dir, amnt] = move.split(' ')
    rope = moveRope(dir, int(amnt), rope, tailPositions)
print(len(set(tailPositions)))