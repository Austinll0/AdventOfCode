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
blueprint = 0;
out = 0;
for line in open("day19ex.txt"):
    blueprint += 1;
    costs = parse(line);
    maxBots = getMax(costs);
    startProduction = [1,0,0,0];
    startInventory = [0,0,0,0];
    start = [startProduction,startInventory,24];
    queue = [start];
    geodes = 0;
    while queue:
        round = queue.pop(0);
        canBuild = False;
        for i in range(4):
            if round[0][i] >= maxBots[i]:
                print(round[0]);
                continue;
            turnsNeeded = turnsToMake(costs[i],round[0],round[1]);
            if turnsNeeded + 1> round[2]:
                continue;
            newInv = matrixMath(round[0],costs[i],round[1],turnsNeeded);
            newPrd = round[0].copy();
            newPrd[i] += 1;
            newTrn = round[2] - turnsNeeded;
            newRnd = [newPrd,newInv,newTrn];
            found = False;
            for q in queue:
                if matches(newRnd,q):
                    found = True;
                    break;
            if found:
                continue;
            queue.append([newPrd,newInv,newTrn]);
            canBuild = True;
        if not canBuild:
            newGeodes = round[1][3] + round[0][3] * round[2];
            if newGeodes > geodes:
                geodes = newGeodes;
    out += geodes * blueprint;
print(out);

