out1 = "";
out2 = "";
numpiles = 9;
piles1 = [];
piles2 = [];
for i in range(numpiles):
    piles1.append([]);
    piles2.append([]);
with open("day5in.txt") as f:
    line = f.readline();
    while(line[1] != '1'):
        for i in range(numpiles):
            if(line[1+4*i] == " "):
                continue;
            piles1[i].append(line[1+4*i])
            piles2[i].append(line[1+4*i])
        line = f.readline();
    f.readline();
    line = f.readline()
    while(line):
        line = line.strip().split(" ");
        h,j,k = int(line[1]),int(line[3])-1,int(line[5])-1
        for i in range(h):
            piles1[k].insert(0,piles1[j].pop(0))
        for i in reversed(range(h)):
            piles2[k].insert(0,piles2[j].pop(i))
        line = f.readline();
for p in piles1:
    out1 += p[0];
for p in piles2:
    out2 += p[0];
print("Part1: " + out1);
print("part2: " + out2);
