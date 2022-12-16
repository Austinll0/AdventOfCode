import time;

def getNums(line):
    line = line.split(" ");
    line = [line[2],line[3],line[8],line[9]];
    for i in range(4):
        line[i] = int(line[i].split("=")[1].strip("\n, :"))
    return line;
def merge(ranges):
    combined = True;
    while combined:
        combined = False;
        for i in range(len(ranges)):
            for j in range(i+1,len(ranges)):
                if intersects(ranges[i],ranges[j]):
                    new = [min(ranges[i][0],ranges[j][0]),max([ranges[i][1],ranges[j][1]])];
                    ranges.pop(j);
                    ranges.pop(i);
                    ranges.append(new);
                    combined = True;
                    break;
            if combined:
                break;
    return ranges;

def intersects(range1,range2):
    if range1[0] >= range2[0] -1 and range1[0] <=range2[1]+1:
        return True;
    if range1[1] >= range2[0] -1 and range1[1] <=range2[1]+1:
        return True;
    if range2[0] >= range1[0] -1 and range2[0] <=range1[1]+1:
        return True;
    if range2[1] >= range1[0] -1 and range2[1] <=range1[1]+1:
        return True;
    return False;
    
def findClearedRange(positions,height):
    Sx = positions[0];
    Sy = positions[1];

    Bx = positions[2];
    By = positions[3];
    dist = abs(Sx - Bx) + abs(Sy - By);
    distToHeight = abs(Sy - height);
    diff = dist - distToHeight;
    if diff >= 0:
        return (Sx-diff, Sx+diff);

sets = [];
p1height = 2000000;
for line in open("day15in.txt"):
    sets.append(getNums(line));
start = time.time();
clearedRanges = [];
for s in sets:
    newRange = findClearedRange(s,p1height);
    if newRange:
        clearedRanges.append(newRange);
clearedRanges = merge(clearedRanges)[0];
p1 = max([clearedRanges[0] + clearedRanges[1], clearedRanges[1] - clearedRanges[0] + 1]);
beacons = [];
for s in sets:
    beacons.append((s[2],s[3]));
beacons = set(beacons);
for b in beacons:
    if b[1] == p1height and b[0] > clearedRanges[0] and b[0] < clearedRanges[1]:
        p1 -= 1;
print("Part 1:",p1,"in",time.time()-start,"s");
start = time.time();
for i in range(4000000):
    clearedRanges =[];
    for s in sets:
        newRange = findClearedRange(s,i);
        if newRange:
            clearedRanges.append(newRange);
    clearedRanges = merge(clearedRanges);
    if len(clearedRanges) > 1:
        val = 0;
        if clearedRanges[0][0] == clearedRanges[1][1] + 2:
            val += (clearedRanges[0][0]-1) * 4000000 + i;
        else:
            val += (clearedRanges[0][1]+1) * 4000000 + i;
        print("Part 2:",val,"in",time.time()-start,"s");
        break;
