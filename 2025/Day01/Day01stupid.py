thing = 0;

with open('Day01in.txt', 'r') as f:
    line = f.readline()
    safe = 50
    while line:
        num = int(line[1:-1])
        d = 1 if line[0] == "R" else - 1
        while num > 0:
            safe += d
            num -= 1
            safe = safe % 100
            if safe == 0:
                thing += 1
        line = f.readline()
print(thing)
