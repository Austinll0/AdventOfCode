from itertools import combinations

class machine:
    def __init__(self,line):
        l = line.split(" ")
        thing = l.pop(0)[1:-1]
        self.lights = 0
        for i in range(len(thing)):
            if thing[i] == '#': self.lights += (1 << i)
        thing = l.pop() # not used Part 1
        self.buttons = [];
        for A in [B[1:-1].split(",") for B in l]:
            b = 0
            for num in A:
                b += 1 << int(num)
            self.buttons.append(b)
        
    def start(self):
        l = len(self.buttons)
        nums = range(l)
        for i in range(1,l):
            for p in combinations(self.buttons,i):
                newLights = 0
                for n in p:
                    newLights = newLights ^ n
                if newLights == self.lights: return i
        return l

machs = open("Day10in.txt","r").read().split("\n")
machs.pop()
machs = [machine(m) for m in machs]
part1 = 0;
for m in machs:
    part1 += m.start() 
print(part1)
