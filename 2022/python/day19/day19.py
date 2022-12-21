import math
import time
def parse(line):
    line = line.split(" ");
    oreCost = [int(line[6]),0,0,0];
    clayCost = [int(line[12]),0,0,0];
    obsidianCost = [int(line[18]),int(line[21]),0,0];
    geodeCost = [int(line[27]),0,int(line[30]),0];
    return [oreCost,clayCost,obsidianCost,geodeCost];

def turnsToMake(cost,production,inventory):
    turns = 0;
    for i in range(4):
        needed = cost[i] - inventory[i];
        if needed <= 0:
            continue;
        if production[i] == 0:
            return 999;
        val  = math.ceil(needed/production[i]);
        if val > turns:
            turns = val;
    return turns;
def matrixMath(production,cost,inventory,turns):
    new = [];
    for i in range(4):
        new.append(inventory[i] - cost[i] + production[i]*turns);
    return new;
def getMax(costs):
    arr = [0,0,0,99];
    for i in range(4):
        for j in range(4):
            if costs[i][j] > arr[j]:
                arr[j] = costs[i][j];
    return arr;
def matches(state1,state2):
    for i in range(4):
        if state1[0][i] != state2[0][i]:
            return False;
        if state1[1][i] != state2[1][i]:
            return False;
    if state1[2] != state2[2]:
        return False;
    return True;
def simulate(start,costs):
    queue = [start];
    maxBots = getMax(costs);
    geodes = 0;
    while queue:
        round = queue.pop();
        maxGeodes = round[1][3] + round[0][3] * round[2] + sum(range(round[2]+1))
        if maxGeodes < geodes:
            continue;
        canBuild = False;
        for i in range(4):
            if round[0][i] >= maxBots[i]:
                continue;
            turnsNeeded = turnsToMake(costs[i],round[0],round[1]);
            if turnsNeeded + 1> round[2]:
                continue;
            newInv = matrixMath(round[0],costs[i],round[1],turnsNeeded+1);
            newPrd = round[0].copy();
            newPrd[i] += 1;
            newTrn = round[2] - turnsNeeded - 1;
            newRnd = [newPrd,newInv,newTrn];
            queue.append([newPrd,newInv,newTrn]);
            canBuild = True;
        if not canBuild:
            newGeodes = round[1][3] + round[0][3] * round[2];
            if newGeodes > geodes:
                geodes = newGeodes;
    return geodes;

def part1():
    blueprint = 0;
    out = 0;
    for line in open("day19in.txt"):
        blueprint += 1;
        costs = parse(line);
        startProduction = [1,0,0,0];
        startInventory = [0,0,0,0];
        start = [startProduction,startInventory,24];
        queue = [start];
        out += simulate(start,costs) * blueprint;
    return out;
def part2():
    out = 1;
    with open("day19in.txt") as f:
        for _ in range(3):
            line = f.readline();
            costs = parse(line);
            startProduction = [1,0,0,0];
            startInventory = [0,0,0,0];
            start = [startProduction,startInventory,32];
            queue = [start];
            out *= simulate(start,costs);
    return out;
startTime = time.time();
print("Part 1:" , part1() , "in" , time.time()-startTime,"s");
startTime = time.time();
print("Part 2:" , part2() , "in" , time.time()-startTime,"s");
