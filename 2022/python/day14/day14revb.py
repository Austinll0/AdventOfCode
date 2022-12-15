import time;

class hashMap:
    def __init__(self,size):
        self.size = size;
        self.map = [];
        for i in range(size):
            self.map.append([]);
    def __contains__(self,item):
        return item in self.map[self.createKey(item)]
    def createKey(self,item):
        return (item[0] * item[1]) % self.size;
    def append(self,item):
        self.map[self.createKey(item)].append(item);
    def extend(self,items):
        for i in items:
            self.append(i);
    def getMaxY(self):
        max = 0;
        for a in self.map:
            for i in a:
                if i[1] > max:
                    max = i[1];
        return max;
def pour(points, pos,yMax):
    while True:
        if pos[1] > yMax:
            return;
        new = [pos[0],pos[1]+1];
        if tuple(new) in points:
            new = [pos[0]-1,pos[1]+1];
            if tuple(new) in points:
                new[0] = new[0]+2;
                if tuple(new) in points:
                    return pos;
                else:
                    pos[0] = pos[0] + 1;
                    continue;
            else:
                pos[0] = pos[0] -1;
                continue;
        else:
            pos[1] += 1;

def BFSpour(plist, pos,yMax):
    yMax = yMax + 2
    out = 0;
    sandqueue = [pos];
    while sandqueue:
        active = sandqueue.pop(0);
        out += 1;
        if active[1] == yMax -1:
            continue;
        for i in range(-1,2):
            new = (active[0]+i,active[1]+1);
            if new in sandqueue or new in plist:
                continue;
            sandqueue.append(new);

    return out;
def points(line):
    points = [i.strip().split(",") for i in line.split("->")]
    out = [];
    for i in range(len(points)-1):
        xp = [int(points[i][0]),int(points[i+1][0])];
        yp = [int(points[i][1]),int(points[i+1][1])];
        xmin = min(xp)
        xmax = max(xp)+1;
        ymin = min(yp);
        ymax = max(yp)+1;
        for x in range(xmin,xmax):
            for y in range(ymin,ymax):
                out.append([x,y]);
    out = [tuple(i) for i in out]
    return out;

start = time.time();

plist = hashMap(5000);
for line in open("day14in.txt"):
    plist.extend(points(line));
yMax = plist.getMaxY();
P1 = 0;
new = pour(plist,[500,0],yMax);
while new:
    plist.append(tuple(new));
    new = pour(plist,[500,0],yMax);
    P1 += 1;
print("Part 1:" ,P1,"in", time.time() - start, "S");

start = time.time();
plist = hashMap(5000);
for line in open("day14in.txt"):
    plist.extend(points(line));

    
print("Part 2:", BFSpour(plist,(500,0),yMax), "in", time.time() - start, "S");
