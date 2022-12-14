def moveHead(H,dir):
    if dir == 'R':
        H[0] += 1;
    elif dir == 'L':
        H[0] -= 1;
    elif dir == 'U':
        H[1] += 1;
    else:
        H[1] -= 1;
    return H;
def moveTail(H,T):
    dist = abs(H[0] - T[0]) + abs(H[1] - T[1])
    if H[0] != T[0] and  H[1] != T[1]:
        if(dist > 2):
            T[0] +=(H[0] > T[0]) * 1 + (H[0] < T[0])* -1;
            T[1] +=(H[1] > T[1]) * 1 + (H[1] < T[1])* -1;
    elif dist > 1:
            T[1] +=(H[1] > T[1]) * 1 + (H[1] < T[1])* -1;
            T[0] +=(H[0] > T[0]) * 1 + (H[0] < T[0])* -1;
    return T;
rope = [];
for i in range(10):
    rope.append([0,0]);
places = [];
p2 = [[0,0]];

for line in open("day9in.txt"):
    line = line.split(" ");
    for i in range(int(line[1])):
        rope[0] = moveHead(rope[0],line[0]);
        for i in range(1,len(rope)):
            rope[i] = moveTail(rope[i-1],rope[i]);
        places.append([rope[1][0],rope[1][1]])
        p2.append([rope[9][0],rope[9][1]]);

print("Part 1: " + str(len(set(tuple(x) for x in places))));
print("Part 2: " + str(len(set(tuple(x) for x in p2))));

