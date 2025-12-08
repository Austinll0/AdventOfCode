import time


def simulate(particles, splitters):
    new = [];
    splits = 0;
    while particles:
        p = particles.pop();
        x = p[0]
        y = p[1]+1
        if [x,y] in splitters:
            splitters.remove([x,y])
            p1 = [x-1,y]
            p2 = [x+1,y]
            if p1 not in new: new.append(p1)
            if p2 not in new: new.append(p2)
            splits += 1;
        elif [x,y] not in new: new.append([x,y])
    particles.extend(new)
    return splits
def diverge(timelines,splitters):
    new = []
    while timelines:
        t = timelines.pop()
        p = t[1]
        p[1] += 1
        if p in splitters:
            splitters.remove(p)
            p1 = [p[0]-1,p[1]]
            p2 = [p[0]+1,p[1]]
            t1 = False
            t2 = False
            for n in new:
                p3 = n[1]
                if p3 == p1: 
                    n[0] += t[0]; t1 = True
                if p3 == p2: 
                    n[0] += t[0]; t2 = True
            if not t1: new.append([t[0],p1])
            if not t2: new.append([t[0],p2])
        else:
            doinky = False;
            for n in new:
                if p == n[1]: n[0] += t[0]; doinky = True;
            if not doinky:
                new.append([t[0],p]) 

    timelines.extend(new)

def countTimes(timelines):
    n = 0;
    for t in timelines:
        n += t[0]
    return n
part1 = 0
part2 = 0
particles = [];
splitters = [];

### GET INPUT 
with open("Day07in.txt","r") as f:
    cha = f.read(1)
    x,y = -1,0
    while cha:
        x += 1;
        if cha == '^': splitters.append([x,y]);
        elif cha == 'S': particles.append([x,y]);
        elif cha == '\n': x = -1; y += 1;
        cha = f.read(1)
### SET DEPTH
depth = 0;
for s in splitters:
   if s[1] > depth:
    depth = s[1]

### PART 1
p = particles.copy()
s = splitters.copy()
start = time.time()
while p[0][1] < depth:
    part1 += simulate(p,s)
end1 = time.time()
### PART 2
t = [[1,p] for p in particles.copy()]
s = splitters.copy()
while t[0][1][1] < depth:
    diverge(t,s)
part2 = countTimes(t)
end2 = time.time()


print("Part 1: ", part1, " in " ,end1-start,"s")
print("Part 2: ", part2, " in " ,end2-start,"s")
