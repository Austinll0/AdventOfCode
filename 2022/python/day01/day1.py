out = [0,0,0];
with open("day1in.txt") as f:
    line = f.readline();
    temp = 0;
    while(line):
        if (line != '\n'):
            temp += int(line);
        else:
            out[0] = (temp > out[0]) * temp + (out[0] > temp) * out[0];
            out.sort()
            temp = 0;
        line = f.readline();
print("Part 1: " + str(out[2]));
print("Part 2: " + str(sum(out)));
