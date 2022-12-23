import time;
class monkey:
    def __init__(self,line):
        line = line.split(":");
        self.name = line[0];
        try:
            line = int(line[1]);
            self.value = line;
        except:
            self.value = line[1].strip().split(" ");
    def printAll(self):
        print(self.name,self.value);

def operate(val1,val2,op):
    if op == '/':
        return val1 / val2;
    if op == '*':
        return val1 * val2;
    if op == '+':
        return val1 + val2;
    if op == '-':
        return val1-val2;
    print("you fucked up");

def operate2(val1,val2,op):
    val1Int = type(val1) != list
    if op == '/':
        if val1Int:
            pass; #does not happen
        return [val1[0]/val2,val1[1]/val2];
    if op == '*':
        if val1Int:
            return [val2[0]*val1,val2[1]*val1];
        return [val1[0]*val2,val1[1]*val2];
    if op == '+':
        if val1Int:
            return [val2[0]+val1,val2[1]];
        return [val1[0]+val2,val1[1]];
    if op == '-':
        if val1Int:
            return [val1 - val2[0],val2[1]];
        return [val1[0] - val2,val1[1]];
    print("you fucked up");

def evaluate(monkey,monkeyList):
    if type(monkey.value) == int:
        return monkey.value;
    val1 = evaluate(findMonkey(monkey.value[0],monkeyList),monkeyList);
    val2 = evaluate(findMonkey(monkey.value[2],monkeyList),monkeyList);
    op = monkey.value[1];
    return operate(val1,val2,op);

def evaluate2(monkey,monkeyList):
    if type(monkey.value) == int:
        if monkey.name == "humn":
            return [0,1] #add, multiply
        return monkey.value;
    val1 = evaluate2(findMonkey(monkey.value[0],monkeyList),monkeyList);
    val2 = evaluate2(findMonkey(monkey.value[2],monkeyList),monkeyList);
    op = monkey.value[1];
    if type(val1) != list and type(val2) != list:
        return operate(val1,val2,op);
    return operate2(val1,val2,op);
def solve(monkey,monkeyList):
    val1 = evaluate2(findMonkey(monkey.value[0],monkeyList),monkeyList);
    val2 = evaluate2(findMonkey(monkey.value[2],monkeyList),monkeyList);
    if type(val1) != list:
        return (val1 - val2[0]) / val2[1];
    return (val2 - val1[0]) / val1[1];
def findMonkey(name,monkeyList):
    for m in monkeyList:
        if m.name == name:
            return m;

monkeys = [];
for line in open("day21in.txt"):
    monkeys.append(monkey(line));
start = time.time();
print("Part 1: ",int(evaluate(findMonkey("root",monkeys),monkeys)),"in",time.time() - start,"s");
start = time.time();
print("Part 2: ",int(solve(findMonkey("root",monkeys),monkeys)),"in",time.time()-start,"s");
print("idk why the absolute value of the above is the answer");
