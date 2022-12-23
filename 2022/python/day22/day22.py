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

blockMap = hashMap(5000);
widths = [];
height = -1;
for line in open("day18ex.txt"):
    height += 1;
    start = 0;
    end = len(line)-1;
    for i in range(end):
        if line[i] == "#":
            blockMap.append([i,height]);
        elif line[i] == " ":
            start += 1;
    widths.append([start,end]);
for i in range(height):
    start = 0;
    end = height-1;
    for w in widths:
        if w[0] == i 

