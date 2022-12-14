def checkNotables(notables, cycle, x):
    if cycle in notables: 
        return cycle * x;
    return 0;
def checkPixel(cycle,x):
    column = cycle % 40 - 1;
    if cycle == 10:
        print(cycle,x);
    diff = abs(x - column);
    pixel = "";
    if diff <= 1:
        pixel +=  "█";
    else: pixel += " ";
    if column == -1:
        pixel += "\n";
    return pixel;
x = 1;
cycle = 0;
out1 = 0;
out2 = "";
notableCycles = [20,60,100,140,180,220];
for line in open("day10in.txt"):
   
    line = line.strip().split(" ");
    if(line[0] == "noop"):
        cycle += 1;
        out1 += checkNotables(notableCycles,cycle,x);
        out2 += checkPixel(cycle,x);
        continue;
    elif line[0] == "addx":
        cycle += 1;
        out1 += checkNotables(notableCycles,cycle,x);
        out2 += checkPixel(cycle,x);
        cycle += 1;
        out1 += checkNotables(notableCycles,cycle,x);
        out2 += checkPixel(cycle,x);
        x += int(line[1]);
        continue;
print(out1);
print(out2);
