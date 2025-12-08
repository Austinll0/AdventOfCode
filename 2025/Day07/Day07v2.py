
#### DOES NOT WORK :((((



from queue import PriorityQueue

class splitter:
    def getChildren(self,splitters):
        for s in splitters:
            if s.x == self.x - 1 or s.x == self.x + 1:
                self.children.append(s)
                if len(self.children) >= 2: break;
    def weight(self):
        return self.y*100 + self.x
    def __init__(self,x,y):
       self.children = []
       self.x = x
       self.y = y
    def __str__(self):
        return str([self.x,self.y])

def priorityAdd(s,i):
    for k in range(len(s)):
        c = s[k].weight();
        c2 = i.weight();
        if c2 > c:
            s.insert(k,i)
            return
    s.append(i)

def simulate(start):
    splitters = [start]
    splits = 0;
    while splitters:
        s = splitters.pop()
        splits += 1
        for c in s.children:
            if c not in splitters: priorityAdd(splitters,c)
    return splits

splitters = [];
start = 0;
with open("Day07in.txt","r") as f:
    cha = f.read(1)
    x,y = -1,0
    while cha:
        x += 1
        if cha == '^': splitters.append(splitter(x,y))
        elif cha == 'S': start = [x,y]
        elif cha == '\n': x = -1; y += 1;
        cha = f.read(1)
for s in splitters:
    if s.x == start[0]:
        start = s;
        splitters.remove(s)
        break;
start.getChildren(splitters)
while splitters:
    s = splitters.pop(0)
    s.getChildren(splitters)

print(simulate(start))
print(start.children)
