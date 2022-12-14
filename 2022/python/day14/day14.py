def points(line):
    points = [i.strip().split(",") for i in line.split("->")]
    out = [];
    for i in range(len(points)-1):
        xp = [int(points[i][0]),int(points[i+1][0])];
        yp = [int(points[i][1]),int(points[i+1][1])];
        xmin = min(xp)
        xmax = max(xp)+1;
        ymin = min(yp);
        ymax = max(yp)+1;
        for x in range(xmin,xmax):
            for y in range(ymin,ymax):
                out.append([x,y]);
    out = [tuple(i) for i in out]
    return out;

for line in open("day14ex.txt"):
    print(points(line));
