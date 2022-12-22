def updatePositions(arr,OG, position, val):
    length = len(arr);
    newPosition  = position + val;
    if newPosition >= length:
        newPosition = (newPosition % length) + 1;
    elif newPosition <= 0:
        newPosition = (newPosition -1) % length;
    if position < newPosition:
        dif = -1;
        for i in range(length):
            if arr[i] >position and arr[i] <= newPosition:
                arr[i] += dif;
    elif position > newPosition:
        dif = 1;
        for i in range(length):
            if arr[i] <position and arr[i] >= newPosition:
                arr[i] += dif;
    arr[OG] = newPosition;
    return arr;
#TODO OG value is what's wrong.Figure out how to save OG value and pass it along. 
def encrypt(arr,positions):
    for i in range(len(positions)):
        value = arr[i];
        position = updatePositions(positions,i,positions[i],value);
    return position;

def part1(arr,positions):
    positions = encrypt(arr,positions);
    new = [];
    for i in range(len(positions)):
        new.append(arr[positions.index(i)]);
    print(new);
    index = positions[arr.index(0)];
    out = 0;
    for i in range(1,4):
        needed = i * 1000 + index;
        needed = needed % length;
        out += arr[positions.index(needed)]
    return out;
def part2(arr,positions):
    for _ in range(10):
        new = [];
        for i in range(len(positions)):
            new.append(arr[positions.index(i)]);
        print(new);
        positions = encrypt(arr,positions);
    index = positions[arr.index(0)];
    out = 0;
    for i in range(1,4):
        needed = i * 1000 + index;
        needed = needed % length;
        out += arr[positions.index(needed)]
    return out;

positions = [];
arr = [];
keyArr = [];
key =811589153; 
for line in open("day20ex.txt"):
    arr.append(int(line));
    keyArr.append(int(line)*key);
length = len(arr);
for i in range(len(arr)):
    positions.append(i);


    new = [];
print(part1(arr,positions.copy()));
print(part2(keyArr,positions));
