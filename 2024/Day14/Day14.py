import re
import time
import itertools

part1 = 1
H = 103
W = 101
turns = 100
quads = [0,0,0,0]

with open("Day14in.txt") as f:
    line = f.readline().strip()
    while line:
        match = re.match("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)",line)
        x = int(match.group(1))
        y =  int(match.group(2))
        dx = int(match.group(3))
        dy = int(match.group(4))
        x = x + turns * dx
        y = y + turns * dy
        x = x % W
        y = y % H
        q = 0
        if x > (W-1)/2:
            q +=1;
        elif x == (W-1)/2:
            line = f.readline().strip()
            continue
        if y > (H-1)/2:
            q +=2;
        elif y == (H-1)/2:
            line = f.readline().strip()
            continue
            print(x,y)
        quads[q] += 1
        line = f.readline().strip()
for q in quads:
    part1 *= q
print(part1)


class robot:
    def __init__(self,line):
        match = re.match("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)",line)
        self.x = int(match.group(1))
        self.y =  int(match.group(2))
        self.dx = int(match.group(3))
        self.dy = int(match.group(4))
    def update(self):
        self.x += self.dx
        self.y += self.dy 
        self.x = self.x % W
        self.y = self.y % H
    def position(self):
        return ((self.x,self.y))
def botPrint(bots):
    for i in range(W):
        out = "";
        for j in range(H):
            pos = 0;
            yes = False
            for b in bots:
                if b.position() == (i,j):
                    out += "."
                    yes = True
                    break;
            if not yes:
                out += " "
        print(out)
def hasCross(bots):
    for i,b in enumerate(bots):
        dirs = [0,0,0,0]
        for c in bots[i+1:]:
            pos1 = b.position()
            pos2 = c.position()
            if pos1[0] - pos2[0] == -1 and pos1[1] == pos2[1]:
                dirs[0] = 1;
            elif pos1[0] - pos2[0] == 1 and pos1[1] == pos2[1]:
                dirs[1] = 1;
            elif pos1[1] - pos2[1] == -1 and pos1[0] == pos2[0]:
                dirs[2] = 1;
            elif pos1[1] - pos2[1] == 1 and pos1[0] == pos2[0]:
                dirs[3] = 1;
        nvm = False
        for d in dirs:
            if d == 0:
                nvm = True
        
        if nvm:
            continue
        return True 
    return False
        



bots = []
with open("Day14in.txt") as f:
    line = f.readline().strip()
    while line:
        bots.append(robot(line))
        line = f.readline().strip()
i = 1;
while True:
    for b in bots:
        b.update()
    if hasCross(bots):
        print(i)
        botPrint(bots)
    i = i + 1
