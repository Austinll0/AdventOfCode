#TODO revb with doubly linkedlist containing [originalOrder,value]
import time;

def updatePositions(arr,OG, position, val):
    length = len(arr);
    newPosition  = (position + val) % (length -1);
        
    if position < newPosition:
        dif = -1;
        for i in range(length):
            if arr[i] >position and arr[i] <= newPosition:
                arr[i] = (arr[i] + dif) % length;
    elif position > newPosition:
        dif = 1;
        for i in range(length):
            if arr[i] <position and arr[i] >= newPosition:
                arr[i] = (arr[i] + dif) % length;
    arr[OG] = newPosition;
    return arr;
def encrypt(arr,positions):
    for i in range(len(positions)):
        value = arr[i]
        position = updatePositions(positions,i,positions[i],value);
    return position;

def part1(arr,positions):
    positions = encrypt(arr,positions);
    index = positions[arr.index(0)];
    out = 0;
    for i in range(1,4):
        needed = i * 1000 + index;
        needed = needed % length;
        out += arr[positions.index(needed)]
    return out;
def part2(keyArr,positions):
    for _ in range(10):
        positions = encrypt(keyArr,positions);
    index = positions[keyArr.index(0)];
    out = 0;
    for i in range(1,4):
        needed = i * 1000 + index;
        needed = needed % length;
        out += keyArr[positions.index(needed)]
    return out;

positions = [];
arr = [];
keyArr = [];
key =811589153; 
for line in open("day20in.txt"):
    arr.append(int(line));
    keyArr.append(int(line)*key);
length = len(arr);
for i in range(len(arr)):
    positions.append(i);

start = time.time()
print("Part 1:" ,part1(arr,positions.copy()),"in",time.time()-start,"s");
start = time.time()
print("Part 2:" ,part2(keyArr,positions.copy()),"in",time.time()-start,"s");
