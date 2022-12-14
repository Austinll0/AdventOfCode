import time;
def checkVisible(map,val,xr,yr):
    for x in xr:
        for y in yr:
            if int(map[x][y]) >= val:
                return False;
    return True;
def checkScenicScore(map,val,x0,y0,xr,yr,dir): #dir 0 = left ,1 = up, 2 = right, 3 = down
    if dir ==0:
        xr = reversed(range(x0
    for x in reversed(xr):
        for y in reversed(yr):
            if int(map[x][y]) >= val:
                if dir % 2  == 1:
                    return abs(y - y0)
                else:
                    return abs(x - x0)
    if dir == 0:
        return x0;
    if dir == 1:
        return y0;
    if dir == 2:
        return max(xr) - x0;
    else:
        return max(yr) - y0;
out1 = 0;
out2 = 0;
map = []
for line in open("day8ex.txt"):
    map.append(line.strip());
xMax = len(map);
yMax = len(map[0]);

for x in range(xMax):
    for y in range(yMax):
        if x == 0 or x == xMax or y == 0 or y == yMax:
            out1 += 1;
            continue;
        val = int(map[x][y]);
        temp = checkScenicScore(map,val,x,y,xMax,yMax,1);
        temp *= checkScenicScore(map,val,x,y,xMax,yMax),3);
        temp *= checkScenicScore(map,val,x,y,xMax,yMax,0);
        temp *= checkScenicScore(map,val,x,y,xMax,yMax,2);
        print(temp);
        if temp > out2:
            out2 = temp;

        if(checkVisible(map,val,[x],range(y))):
            out1 += 1;
            continue;
        if(checkVisible(map,val,[x],range(y+1,yMax))):
            out1 += 1;
            continue;
        if(checkVisible(map,val,range(x),[y])):
            out1 += 1;
            continue;
        if(checkVisible(map,val,range(x+1,xMax),[y])):
            out1 += 1;
            continue;
print(out1);
print(out2);



