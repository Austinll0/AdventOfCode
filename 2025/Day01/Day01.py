import math
Part1 = 0;
Part2 = 0;
with open('Day01in.txt', 'r') as f:
    line = f.readline()
    safe = 50;
    while line:
        num = int(line[1:-1])
        if num >= 100:
            Part2 += math.floor(num/100)
            num = num %100
        if line[0] == "R":
            if num > 100 - safe:
                Part2 += 1
            safe += num
        else:
            if num > safe and safe is not 0:
                Part2 += 1
            safe -= num
        safe = safe % 100
        if safe == 0:
            Part1 += 1;
        line = f.readline()
print(Part1)
print(Part2 + Part1)
