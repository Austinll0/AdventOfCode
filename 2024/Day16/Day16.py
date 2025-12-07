import time;
import copy;
class priorityQueue:
    def __init__(self):
        self.list = [];
    def pop(self):
        return self.list.pop(0)
    def add(self,item):
        if len(self.list) == 0:
            self.list.append(item)
            return;
        for i in range(len(self.list)):
            if self.list[i][1] > item[1]:
                self.list.insert(i,item)
                return;
        self.list.append(item)
class node:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
        self.a = [-1,-1,-1,-1];#N,E,S,W
        self.v = False;
    def __str__(self):
        return str(self.x) + "," + str(self.y)

def addAdjacents(nodes):
    for i,n1 in enumerate(nodes):
        for n2 in nodes[i+1:]:
            if n1.x - n2.x == 1 and n1.y == n2.y:
                n1.a[3] = n2
                n2.a[1] = n1
            elif n1.x - n2.x == -1 and n1.y == n2.y:
                n1.a[1] = n2
                n2.a[3] = n1
            elif n1.y - n2.y == 1 and n1.x == n2.x:
                n1.a[0] = n2
                n2.a[2] = n1
            elif n1.y - n2.y == -1 and n1.x == n2.x:
                n1.a[2] = n2
                n2.a[0] = n1
part1 = 0;

nodes = []
queue = priorityQueue();
start = -1;
goal = -1;
with open("Day16in.txt") as f:
    text = f.read().strip().split("\n")
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == '#':
                continue;
            if text[i][j] == '.':
                nodes.append(node(j,i))
                continue;
            if text[i][j] == 'E':
                goal = node(j,i)
                nodes.append(goal)
                continue;
            if text[i][j] == 'S':
                start = node(j,i);
                nodes.append(start)
                queue.add([start,0,1,[start]])
                continue;

addAdjacents(nodes)  

while queue.list:
    active = queue.pop()
    current = active[0];
    score = active[1];
    if current == goal:
        part1 = score;
        for v in active[3]:
            print(v)
        break;
    direction = active[2];
    visited =copy.copy( active[3])
    for i in range(4):
        if current.a[i] == -1:
            continue
        if current.a[i] in visited:
            continue

        nv = visited;
        nv.append(current.a[i])
        if direction == i:
            queue.add([current.a[i],score + 1,i,nv])
        else:
            queue.add([current.a[i],score + 1001,i,nv])
print(part1)
queue.add([start,0,1,[start]])
things = [];
while queue.list:
    active = queue.pop()
    current = active[0];
    score = active[1];
    direction = active[2];
    visited =copy.copy( active[3])
    if current == goal:
        if score == part1:
            things.extend(visited)
    for i in range(4):
        if current.a[i] == -1:
            continue
        if current.a[i] in visited:
            continue

        nv = visited;
        nv.append(current.a[i])
        if direction == i:
            queue.add([current.a[i],score + 1,i,nv])
        else:
            queue.add([current.a[i],score + 1001,i,nv])
