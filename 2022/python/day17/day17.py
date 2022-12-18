import time;
import math;

class hashMap:
    def __init__(self,size):
        self.size = size;
        self.map = [];
        for i in range(size):
            self.map.append([]);
    def __contains__(self,item):
        item = tuple(item);
        return item in self.map[self.createKey(item)]
    def createKey(self,item):
        return (item[0]**2 * item[1]) % self.size;
    def append(self,item):
        self.map[self.createKey(item)].append(item);
    def extend(self,items):
        for i in items:
            self.append(i);

def push(dif,shape,map):
    # < and > are 2 vals apart. subtracting 61 get -1 for <left and 1 for >right
    new = [];
    for block in shape:
        b = block.copy();
        b[0] += dif;
        if b[0] <= 0 or b[0] >= 8:
            return;
        if b in map:
            return;
        new.append(b);
    return new;
def drop(shape,map):
    new = [];
    for block in shape:
        b = block.copy();
        b[1] -= 1;
        if b[1] <= 0:
            return;
        if b in map:
            return;
        new.append(b);
    return new;

def createObject(number,height):
    if number == 0:
        return createHLine(height);
    if number == 1:
        return createPlus(height);
    if number == 2:
        return createL(height);
    if number == 3:
        return createVLine(height);
    if number == 4:
        return createSquare(height);
def createPlus(height):
    points = [[4,height+2],[4,height]];
    for i in range(3):
        points.append([3+i,height+1]);
    return points;
def createL(height):
    points = [];
    for i in range(3):
        points.append([3+i,height]);
    for i in range(1,3):
        points.append([5,height+i]);
    return points;
def createHLine(height):
    points = [];
    for i in range(4):
        points.append([3+i,height]);
    return points;
def createVLine(height):
    points = [];
    for i in range(4):
        points.append([3,height+i]);
    return points;
def createSquare(height):
    return [[3,height],[4,height],[3,height+1],[4,height+1]];

def dropBlocks(cycles,moves,blockMap,part):
    maxHeight = 0;
    moveNum = 0;
    moveLength = len(moves);
    spawnNum = 0;
    cycle = 0;
    lastTracker = [];
    last = 0;
    while True:
        if moveNum < last and spawnNum == 0 and part == 2:
            for i in reversed(range(len(lastTracker))):
                if lastTracker[i][0] == moveNum:
                    cycleDif = cycle - lastTracker[i][1];
                    heightDif = maxHeight - lastTracker[i][2];
                    cyclesNeeded = cycles - cycle;
                    loopsLeft = math.floor(cyclesNeeded / cycleDif);
                    cycle = cycle + cycleDif * loopsLeft;
                    break;
            lastTracker.append([moveNum,cycle,maxHeight]);
        if spawnNum == 0:
            last = moveNum;
        if cycle >= cycles:
            if part == 2:
                maxHeight += heightDif * loopsLeft;
            break;
        cycle += 1;
        block = createObject(spawnNum,maxHeight+4);
        spawnNum = (spawnNum + 1) % 5;
        while True:
            direction = ord(moves[moveNum]) - 61;
            moveNum = (moveNum + 1) % moveLength;
            newPos = push(direction,block,blockMap);
            if newPos:
                block = newPos;
            newPos = drop(block,blockMap);
            if not newPos:
                block = [tuple(b) for b in block];
                for b in block:
                    if b[1] > maxHeight:
                        maxHeight = b[1];
                blockMap.extend(block);
                break;
            block = newPos;
    return maxHeight;

def part1(moves):
    mapSize = 5000;
    blocksNeeded = 2022;
    blockMap = hashMap(mapSize);
    return dropBlocks(blocksNeeded,moves,blockMap,1);
def part2(moves):
    mapSize = 5000;
    blocksNeeded = 1000000000000
    blockMap = hashMap(mapSize);
    return dropBlocks(blocksNeeded,moves,blockMap,2);
    


start = time.time();
mapSize = 5000;
moves = open("day17in.txt").readline().strip();
blockMap = hashMap(mapSize);

print("Part 1: ",part1(moves),"in",time.time()-start,"s");
start = time.time();
print("Part 2: ",part2(moves),"in",time.time()-start,"s");

