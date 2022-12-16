class valve: 
    def __init__(self,line):
        temp = valve.parse(line);
        self.name = temp[0];
        self.rate = temp[1];
        self.connections = temp[2];
    
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


valves = [];
for line in open("day16ex.txt"):
    valves.append(valve(line));
valve.connections(valves);

