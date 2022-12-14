from queue import PriorityQueue;

def BFSrev(map,height, width, start, target):
    check = PriorityQueue();
    check.put((0,[start,0]));
    visited = [];
    for _ in range(height * width):
        visited.append(False);
    visited[start] = True;
    while(not check.empty()):
        if(map[check.queue[0][1][0]] == target):
            break;
        current = check.get()[1];
        steps = current[1];
        currentVal = map[current[0]];
        if currentVal == 83:
            currentVal = 97;
        current = current[0];
        new = current - width;
        if new > 0 and currentVal <= map[new] + 1 and not visited[new]:
            check.put((steps*2 +200-map[new],[new,steps +1]));
            visited[new] = True;
        new = current + width;
        if new < height * width and currentVal <= map[new] + 1 and not visited[new]:
            visited[new] = True;
            check.put((steps*2 + 200-map[new],[new,steps + 1]));
        new = current - 1;
        newPath = [];
        if new % width != width -1 and currentVal <= map[new] + 1 and not visited[new]:
            visited[new] = True;
            check.put((steps*2 + 200-map[new],[new,steps+1]));
        new = current + 1;
        if new % width != 0 and currentVal <= map[new] + 1 and not visited [new]:
            visited[new] = True;
            check.put((steps*2 + 200-map[new],[new,steps+1]));
    out = check.get();
    return out[1][1];
def BFS(map,height, width, start, target):
    check = PriorityQueue();
    check.put((0,[start,0]));
    visited = [];
    for _ in range(height * width):
        visited.append(False);
    visited[start] = True;
    while(not check.empty()):
        if(check.queue[0][1][0] == target):
            break;
        current = check.get()[1];
        steps = current[1];
        currentVal = map[current[0]];
        if currentVal == 83:
            currentVal = 97;
        current = current[0];
        new = current - width;
        if new > 0 and currentVal >= map[new] - 1 and not visited[new]:
            check.put((steps*2 +200-map[new],[new,steps +1]));
            visited[new] = True;
        new = current + width;
        if new < height * width and currentVal >= map[new] - 1 and not visited[new]:
            visited[new] = True;
            check.put((steps*2 + 200-map[new],[new,steps + 1]));
        new = current - 1;
        newPath = [];
        if new % width != width -1 and currentVal >= map[new] - 1 and not visited[new]:
            visited[new] = True;
            check.put((steps*2 + 200-map[new],[new,steps+1]));
        new = current + 1;
        if new % width != 0 and currentVal >= map[new] - 1 and not visited [new]:
            visited[new] = True;
            check.put((steps*2 + 200-map[new],[new,steps+1]));
    out = check.get();
    return out[1][1];


strmap = "";
map = [];
visited = [];
height = 0;
for line in open("day12in.txt"):
    strmap += line.strip();
    height += 1;
for c in strmap:
    map.append(ord(c));
width = int(len(map) / height);
start = strmap.find("S");
end =strmap.find("E");
map[start] = ord('a')
map[end] = ord('z');
for _ in range(height * width):
    visited.append(False);
visited[start] = True;
print("Part 1: " + str(BFS(map,height,width,start,end)));
print("Part 2: " + str(BFSrev(map,height,width,end,ord("a"))));
