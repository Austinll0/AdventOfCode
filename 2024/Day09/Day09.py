def checkSum(value,position,iterate):
    val = 0;
    for i in range(iterate):
        val += value * position
        position += 1;
    return val


part1 = 0

with open("Day09in.txt") as f:
    line = f.read().strip();
thingy = [];
thingy2 = [];
id = 0;
for i,a in enumerate(line):
    if i % 2 == 0:
        thingy.append([id,int(line[i])]); #id,size
        thingy2.append([id,int(line[i])]); #id,size
        id += 1;
    else:
        thingy.append([-1,int(line[i])]); #value, size, value of -1 is blank
        thingy2.append([-1,int(line[i])]); #value, size, value of -1 is blank
counter = 0;
while len(thingy) > 0:
    t = thingy.pop(0)
    if t[0] > -1:
        part1 += checkSum(t[0],counter,t[1])
        counter += t[1]
    else:
        if not thingy:
            break;

        t2 = thingy.pop();
        while t2[0] < 0 and len(thingy) > 0:
            t2 = thingy.pop();
        while t2[0] < 0:
            t2 = thingy.pop();
        if t2[1] > t[1]:
            thingy.append([t2[0],t2[1]-t[1]]);
            part1 +=checkSum( t2[0],counter, t[1]);
            counter += t[1];
            continue
        elif t2[1] < t[1]:
            thingy.insert(0,[-1,t[1]-t2[1]])
        part1 += checkSum(t2[0], counter, t2[1])
        counter += t2[1]

print(part1)
thingy = thingy2
part2 = 0;
counter = 0;
while len(thingy) > 0:
    t = thingy.pop(0)
    print(t)
    if t[0] >= 0:
        part2 += checkSum(t[0],counter, t[1])
        counter += t[1]
        continue;
    else:
        space = t[1]
        for j in range(len(thingy)-1,-1,-1):
            if thingy[j][0] < 0:
                continue
            if thingy[j][1] <= space:
                t2 = thingy.pop(j)
                print(counter, t2,"t")
                space -= t2[1]
                part2 += checkSum(t2[0],counter,t2[1])
                counter += t2[1]
        counter += space;
print(part2)

