def getNums(line):
    line = line.split(" ");
    line = [line[2],line[3],line[8],line[9]];
    for i in range(4):
        line[i] = int(line[i].split("=")[1].strip("\n, :"))
    return line;

def findClearedSpaces(positions,height):
    out = [];
    Sx = positions[0];
    Sy = positions[1];

    Bx = positions[2];
    By = positions[3];
    dist = abs(Sx - Bx) + abs(Sy - By);
    distToHeight = abs(Sy - height);
    if dist >= distToHeight:
        out.append((Sx,height));
        for i in range(1,dist - distToHeight+1):
            out.append((Sx+i,height));
            out.append((Sx-i,height));
    return out;
clearedSpaces = [];
sets = [];
for line in open("day15in.txt"):
    sets.append(getNums(line));
for s in sets:
    spaces = findClearedSpaces(s,2000000);
    clearedSpaces.extend(spaces);
clearedSpaces = set(clearedSpaces);

for s in sets:
    beacon = (s[2],s[3]);
    clearedSpaces.discard(beacon);
print(len(clearedSpaces));
