
part1 = 0
part2 = 0

def checkAround(papers, pos):
    x = pos[0];
    y = pos[1];
    X = len(papers[0])
    Y = len(papers)
    count = 0;
    for i in range(x-1,x+2):
        if i < 0: continue
        if i >= Y: continue
        for j in range(y-1,y+2):
            if j < 0: continue
            if j >= X: continue
            if i == x and j ==y: continue
            if papers[i][j] == "@": count+=1
            if count >= 4: return 0
    print(pos)
    return 1

with open("Day04in.txt") as f:
    papers = f.read().strip().split("\n")
    for i in range(len(papers)):
        for j in range(len(papers[0])):
            if papers[i][j] == ".":continue
            part1 += checkAround(papers,[i,j])
print(part1)

