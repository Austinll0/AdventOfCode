import time
part1 = 0;
part2 = 0;

def mergeRanges(ranges):
    change = False;
    new = []
    while (len(ranges) > 0):
        a = ranges.pop(0)
        if len(ranges) == 0:
            new.append(a)
            break
        for i in range(len(ranges)-1,-1,-1):
            b = ranges[i]
            if checkOverlap(a,b):
                ranges.pop(i)
                a = newRange(a,b)
                change = True
        new.append(a)
    if change: return mergeRanges(new)
    return new


def checkOverlap(a,b):
    if a[0] < b[0] and a[1] < b[0]:
        return False
    if a[0] > b[1] and a[1] > b[1]:
        return False
    return True

def newRange(a,b):
    one = a[0] if a[0] <= b[0] else b[0]
    two = a[1] if a[1] >= b[1] else b[1]
    return [one,two]
def inRange(x,a):
    if x >= a[0] and x<=a[1]:
        return True
    return False

ranges = [];
IDs = [];
with open("Day05in.txt","r") as f:
    line = f.readline()
    while line:
        if line == "\n":
            break
        thing = line.split("-");
        thing[0] = int(thing[0])
        thing[1] = int(thing[1])
        ranges.append(thing)
        line = f.readline()
    line = f.readline()
    while line:
        IDs.append(int(line))
        line = f.readline()
ranges = mergeRanges(ranges)
for i in IDs:
    for r in ranges:
        if inRange(i,r):
            part1 += 1
            continue;
for r in ranges:
    part2 += 1 + r[1] - r[0]
print(ranges)
print(IDs)

print(part1)
print(part2)
