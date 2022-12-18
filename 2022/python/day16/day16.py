import time;
import itertools;
class valve: 
    def __init__(self,line):
        temp = valve.parse(line);
        self.name = temp[0];
        self.rate = temp[1];
        self.connections = temp[2];
        self.distances = dict();
    
    def connections(valves):
        for v in valves:
            connections = [];
            for name in v.connections:
                connections.append(valve.find(valves,name));
            v.connections = connections;
    def find(valves,name):
        for v in valves:
            if v.name == name:
                return v;
    def parse(line):
        line = line.split(" ");
        name = line[1];
        rate = int(line[4].split("=")[1].strip(";"));
        connections = [];
        for i in range(len(line) - 9):

            connections.append(line[9+i].strip(",\n"));
        return [name,rate,connections];
    def getDistance(valve,target):
        if valve.name == target:
            return 0;
        queue = [[[valve.name],valve]];
        while queue:
            current = queue.pop(0);
            path = current[0];
            V = current[1];
            for c in V.connections:
                if c.name == target:
                    return len(path) + 1;
                if c.name in path:
                    continue;
                newPath = path.copy();
                newPath.append(c.name);
                queue.append([newPath,c]);
    def getDistances(valves):
        for v in valves:
            for v2 in valves:
                v.distances[v2.name] = valve.getDistance(v,v2.name);

def part1(valves,start,startSteps):
    #node contains steps left, open valves, current pos, score
    startNode =[startSteps,[], start,0];
    queue = [startNode];
    max = 0;
    bestActive = [];
    while queue:
        Node = queue.pop(0);
        openValves = Node[1];
        currentPos = Node[2];
        score = Node[3];
        stepsLeft = Node[0] -1;
        for v in valves:
            if v.name in openValves:
                continue;
            if v.rate == 0:
                continue;
            distance = currentPos.distances[v.name]-1;
            if stepsLeft - distance < 0:
                if score > max:
                    bestActive = openValves;
                    score = max;
                continue;
            newSteps = stepsLeft - distance;
            newScore = score + (v.rate * (newSteps));
            newValves = openValves.copy();
            newValves.append(v.name);
            if newScore > max:
                max = newScore;
                bestActive = newValves;
            if stepsLeft - distance == 0 or len(newValves) == len(valves):
                continue;
            queue.append([newSteps,newValves,v,newScore]);
    return [max,bestActive];

def part2(valves,start):
    out = 0;
    vals = part1(valves,start,26);
    eValves = list(filter(lambda v : v.name not in vals[1],valves))
    evals = part1(eValves,start,26);
    out = vals[0] + evals[0];
    perms = [];
    for i in range(len(vals[1])):
        perms.extend(itertools.combinations(vals[1],i));
    for p in perms:
        newValves = valves.copy();
        for str in p:
            newValves.remove(valve.find(newValves,str));
        newVals = part1(newValves,start,26);
        newEValves = list(filter(lambda v : v.name not in newVals[1],valves));
        newEVals = part1(newEValves,start,26);
        newOut = newVals[0] + newEVals[0];
        if newOut > out:
            out = newOut;
    return out;

startTime = time.time();
valves = [];
for line in open("day16in.txt"):
    valves.append(valve(line));
valve.connections(valves);
valve.getDistances(valves);
start = valve.find(valves,"AA");
start2 = valve.find(valves,"AA");
valves = list(filter(lambda v : v.rate > 0, valves)); 
print("Part 1:",part1(valves,start,30)[0],"in",time.time()-startTime,"s");
startTime = time.time();
print("Part 2:",part2(valves,start2),"in",time.time()-startTime,"s");
