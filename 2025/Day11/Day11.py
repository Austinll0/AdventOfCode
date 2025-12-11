import functools
class device:
    def  __init__(self,line):
        self.name = line[0:3] 
        self.sub = line[5:].split(" ")
        self.goals = {};
    def __repr__(self):
        return self.name
    def __eq__(self,other):
        A = self.name
        if type(other) == str:
            return A == other
        return A == other.name

    def findRoutes(self,goal):
        if goal in self.goals: return self.goals[goal]
        self.goals[goal] = 0;
        for child in self.sub:
            if child == goal:
                self.goals[goal] = 1;
            else:
                if child == "out":
                    return 0
                self.goals[goal] += child.findRoutes(goal)
        return self.goals[goal]
devices = open("Day11in.txt","r").read().split("\n")
devices.pop()
devices = [device(d) for d in devices]
for A in devices:
    for B in devices:
        Bn = B.name
        if Bn in A.sub: 
            A.sub.remove(Bn)
            A.sub.append(B)

nums = [0,0,0,0,0,0]
for d in devices: 
    if d.name == "you":
        print(d.findRoutes("out"))
    if d.name == "svr":
        nums[0] = d.findRoutes("dac")
        nums[1] = d.findRoutes("fft")
    if d.name == "dac":
        nums[2] = d.findRoutes("fft")
        nums[3] = d.findRoutes("out")
    if d.name == "fft":
        nums[4] = d.findRoutes("dac")
        nums[5] = d.findRoutes("out")
part2 = nums[1] * nums[4] * nums[3] + nums[0] * nums[2]*nums[5]
print(part2)
