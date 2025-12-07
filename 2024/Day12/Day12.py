import itertools;

def isAdjacent(A,B):
    if A[0] == B[0] or A[1] == B[1]:
        dist = max([abs(A[0]-B[0]), abs(A[1]-B[1])])
        if dist == 1:
            return True
    return False

def getGroups(plots):
    thingy = []
    while len(plots)> 0:
        queue = [plots.pop()]
        new = [queue[0]]
        while len(queue) > 0:
            q = queue.pop(0)
            toRemove = []
            for p in plots:
                if isAdjacent(q,p):
                    queue.append(p)
                    new.append(p)
                    toRemove.append(p)
            for R in toRemove:
                plots.remove(R)
        thingy.append(new);
    return thingy
    
    
    
    
part1 = 0;
plots={}
# get all plots
with open("Day12in.txt") as f:
    L = 0;
    H = 0;
    line = f.readline().strip()
    while line:
        for p in line:
            if p not in plots.keys():
                plots[p] = [];
            plots[p].append([L,H,4])
            L += 1;
        L = 0;
        H += 1;
        line = f.readline().strip()
# seperate plots that share a letter but don't connect
doinky = []
for p in plots:
    for g in getGroups(plots[p]):
        doinky.append(g)
plots = doinky

# set fences on each plot
for p in plots:
    if len(p) == 1:
        part1 += 4;
        continue;
    for c in itertools.combinations(p,2):
        if isAdjacent(c[0],c[1]):
            c[0][2] -= 1;
            c[1][2] -= 1;
    perimeter = 0;
    area = 0;
    for thing in p:
        area += 1;
        perimeter += thing[2];
    part1 += area*perimeter;
print(part1)
