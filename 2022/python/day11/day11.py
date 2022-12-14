import math;

class monkey:
    def __init__(self,f,reduceWorry):
        self.items = self.parseItems(f.readline());
        self.operation = self.parseOp(f.readline());
        self.test = self.parseTest(f.readline());
        self.Tmonkey = self.parseTrue(f.readline());
        self.Fmonkey = self.parseFalse(f.readline());
        self.inspects = 0;
        self.reduceWorry = reduceWorry;
    def parseItems(self,line):
        line = line.split(":")[1].split(",");
        items = [];
        for i in line:
            items.append(int(i.strip()));
        return items;
    def parseOp(self,line):
        line = line.strip().split(" ");
        return [line[3],line[4],line[5]];
    def parseTest(self,line):
        return  int(line.strip().split(" ")[3]);
    def parseTrue(self,line):
        return int(line.strip().split(" ")[5]);
    def parseFalse(self,line):
        return int(line.strip().split(" ")[5]);
    def inspect(self):
        item = self.items.pop(0);
        item = self.evaluate(item);
        if item % self.test == 0:
            return [self.Tmonkey,item];
        else:
            return [self.Fmonkey,item];
    def evaluate(self,value):
        v2 = 0;
        if (self.operation[2] == "old"):
            v2 = value;
        else:
            v2 = int(self.operation[2]);
        new = 0;
        if self.operation[1] == "+":
            new = value + v2;
        else:
            new = value * v2;
        if self.reduceWorry:
            return math.floor(new/3);
        else:
            return new;
def process(rounds, reduceWorry):
    monkeys = [];
    with open("day11in.txt") as f:
        while(True):
            f.readline();
            monkeys.append(monkey(f,reduceWorry));
            if not f.readline():
                break;
        lcf = 1;
        for m in monkeys:
            lcf *= m.test;
    for i in range(rounds): 
        for m in monkeys:
            m.inspects += len(m.items);
            for i in range(len(m.items)):
                nums = m.inspect();
                monkeys[nums[0]].items.append(nums[1] % lcf);
    highest = [0,0];
    for m in monkeys:
        if m.inspects > highest[0]:
            highest[0] = m.inspects;
        if highest[0] > highest[1]:
            highest = [highest[1] , highest[0]]
    print(highest[0] * highest[1]);
print("Part 1:",end=" ");
process(20,True);
print("Part 2:",end=" ");
process(10000,False);
