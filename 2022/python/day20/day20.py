def updatePositions(arr,OG, position, val):
    length = len(arr);
    print("val",val);
    newPosition  =(position + val) % length;
    print("old",position)
    print("new",newPosition);
    if position < newPosition:
        dif = -1;
        for i in range(length):
            if arr[i] >position and arr[i] <= newPosition:
                print("moved position",i,"-1");
                arr[i] += dif;
    elif position > newPosition:
        dif = 1;
        for i in range(length):
            if arr[i] <position and arr[i] >= newPosition:
                arr[i] += dif;
    arr[OG] = newPosition;
    return arr;
        

positions = [];
arr = [];
for line in open("day20ex.txt"):
    arr.append(int(line));
for i in range(len(arr)):
    positions.append(i);

for i in range(len(positions)):
    print("pos",i);
    print("pos2",positions[i]);
    value = arr[i];
    position = updatePositions(positions,i,positions[i],value);
    new = [];
    for j in range(len(positions)):
        for k in range(len(positions)):
            if positions[k] == j:
                new.append(arr[k]);
    print(positions);
    print(arr);
    print(new);
    print(" ")
