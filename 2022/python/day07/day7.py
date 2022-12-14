class dir:
    def __init__(self, name, parent):
        self.parent = parent;
        self.name = name;
        self.children = [];
        self.files = [];
    def __str__(self):
        return f"{self.name} {self.children} {self.files}"
    def child(self, name):
        for c in self.children:
            if c.name == name:
                return c;
    def top(self):
        if self.name != "/":
            return self.parent.top()
        else: return self;
    def getSize(self):
        self.size = 0;
        for i in self.files:
            self.size += i;
        for c in self.children:
            self.size += c.getSize();
        return self.size;
    def part1(self):
        out = 0;
        for c in self.children: 
            out += c.part1();
        if self.size < 100000:
            out += self.size;
        return out;
    def part2(self,needed):
        out = self.size;
        for c in self.children:
            val = c.part2(needed);
            if val < out and val > needed:
                out = val
        return out;
total = 70000000
needed = 30000000
with open("day7in.txt") as f:
    line = f.readline();
    line = f.readline();
    activeDirectory = dir("/","NA")
    while(line):
        line = line.strip().split(" ");
        if line[0] == '$':
            if line[1] == "cd":
                if line[2] == "..":
                    activeDirectory = activeDirectory.parent;
                else:
                    activeDirectory = activeDirectory.child(line[2]);
        elif line[0] == "dir":
            activeDirectory.children.append(dir(line[1],activeDirectory))
        else:
            activeDirectory.files.append(int(line[0]));
        line = f.readline();
    activeDirectory = activeDirectory.top();
    activeDirectory.getSize();
    print("Part 1: " + str(activeDirectory.part1()));
    print("Part 2: " + str(activeDirectory.part2(needed - (total - activeDirectory.size))));
