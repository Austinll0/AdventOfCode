import time;
class hashMap:
    def __init__(self,size):
        self.size = size;
        self.map = [];
        for i in range(size):
            self.map.append([]);
    def __contains__(self,item):
        return item in self.map[self.createKey(item)]
    def __iter__(self):
        self.x = 0;
        self.y = 0;

    def createKey(self,item):
        coords = item.getCoords();
        return (coords[0] * coords[1] * coords[2]) % self.size;
    def createKeyByCoords(self,item):
        return item[0] * item[1] * item[2] % self.size;

    def append(self,item):
        self.map[self.createKey(item)].append(item);
        if item.sides == 0:
            return;
        for c in item.getAdjacentCoords():
            adjacent = self.getItemByCoords(c);
            if adjacent:
                item.reduceSides();
                adjacent.reduceSides();
                if adjacent.sides <= 0:
                    self.remove(adjacent);
            if item.sides <= 0:
                self.remove(item);

    def getItemByCoords(self,coords):
        key = self.createKeyByCoords(coords);
        arr = self.map[key];
        for block in arr:
            if block.coords == coords:
                return block
        return;
    def extend(self,items):
        for i in items:
            self.append(i);
    def remove(self,item):
        self.map[self.createKey(item)].remove(item);
    def printAll(self):
        for arr in self.map:
            for block in arr:
                print(block.coords,block.sides);
    def sumAll(self):
        out = 0;
        for arr in self.map:
            for block in arr:
                out += block.sides;
        return out;
    def getMaxPosition(self):
        max = [[0,0],[0,0],[0,0]];
        for arr in self.map:
            for block in arr:
                x = block.coords[0];
                y = block.coords[1];
                z = block.coords[2];
                if x < max[0][0]:
                    max[0][0] = x;
                if x > max[0][1]:
                    max[0][1] = x;
                if y < max[1][0]:
                    max[1][0] = y;
                if y > max[1][1]:
                    max[1][1] = y;
                if z < max[2][0]:
                    max[2][0] = z;
                if z > max[2][1]:
                    max[2][1] = z;
        return max;

class block:
    def __init__(self,line,sides=6):
        self.coords = [];
        if len(line) != 3:
            line =line.split(",");
            for i in line:
                self.coords.append(int(i));
            self.coords = tuple(self.coords);
        else:
            self.coords = tuple(line);
        self.checked = False;
        self.sides = sides;
    def getCoords(self):
        return self.coords;
    def reduceSides(self):
        self.sides -= 1;
    def getAdjacentCoords(self):
        adjacent = [];
        for i in range(3):
            for j in [-1,1]:
                new = [self.coords[0],self.coords[1],self.coords[2]]
                new[i] += j;
                adjacent.append(tuple(new));
        return adjacent

def getNextSearchCoords(Coords):
    adjacent = [];
    for i in range(3):
        for j in [-1, 1]:
            new = [Coords[0],Coords[1],Coords[2]]
            new[i] += j;
            adjacent.append(tuple(new));
    return adjacent

def scanOutside(blockMap):
    maxRange = blockMap.getMaxPosition();
    for arr in maxRange:
        arr[0] -= 1;
        arr[1] += 1;
    start = (maxRange[0][0],maxRange[1][0],maxRange[2][0]);
    queue = [start];
    out = 0;
    while queue:
        search = queue.pop();
        if invalid(maxRange,search):
            continue;
        new = blockMap.getItemByCoords(search);
        if new:
            if new.sides > 0:
                out += 1;
        else:
            blockMap.append(block(search,0));
            queue.extend(getNextSearchCoords(search));
    return out;

def invalid(borders,position):
    for i in range(3):
        lims = borders[i];
        if position[i] < lims[0] or position[i] > lims[1]:
            return True;
    return False

start = time.time()
blockMap = hashMap(5000);
for line in open("day18in.txt"):
    blockMap.append(block(line));
print("Part 1: ",blockMap.sumAll(), "in", time.time()-start,"s" );
start = time.time();
print("Part 2: " , scanOutside(blockMap), "in" , time.time()-start,"s" );
