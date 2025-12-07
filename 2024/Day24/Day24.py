import re

class wire:
    def __init__(self,line):
        if len(line) == 2:
            self.value = int(line[1])
            self.name = line[0]
            return
        self.w1 = line[0]
        self.w2 = line[2]
        self.op = line[1]
        self.name = line[4]
        self.value = -1

    def evaluate(self):
        if self.value != -1:
            return self.value
        else:
            one = self.w1.evaluate()
            two = self.w2.evaluate()
            if self.op == "AND":
                self.value = one and two
                return self.value
            if self.op == "OR":
                self.value = one or two
                return self.value
            if self.op == "XOR":
                self.value = one^two
                return self.value

def makeLinks(wires):
    for key in wires:
        w = wires[key]
        if w.value != -1:
            continue
        w.w1 = wires[w.w1]
        w.w2 = wires[w.w2]
            

wires = {}
with open("Day24in.txt") as f:
    line = f.readline().split()
    while(line):
        if line == "\n":
            line = f.readline().split()
            continue
        if len(line) == 2:
            wires[line[0].strip(":")] = wire(line)
        else:
            wires[line[4]] = wire(line)
        line = f.readline()
        if line == "\n":
            line = f.readline()
        line = line.split()
makeLinks(wires)
part1 = 0;
bits = [];
for key in wires:
    w = wires[key]
    if re.search("z\d\d",w.name):
        w.evaluate()
        bits.append((int(w.name[1:3]),w.value))
bits = sorted(bits, key = lambda x: x[0])

for i,b in enumerate(bits):
    if b[1]:
        part1 += pow(2,i)
print(part1)
