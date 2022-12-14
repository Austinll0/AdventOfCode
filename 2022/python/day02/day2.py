out1 = 0;
out2 = 0;
with open("day2in.txt") as f:
    line = f.readline();
    while line:
        line = line.split(" ")
        line[0] = ord(line[0]) -  65
        line[1] = ord(line[1][0]) - 88;
        out1 += 1 + line[1];
        out2 += 1;
        if (line[1] == (line[0] + 1)%3):
            out1 += 6
        if (line[1] == line[0]):
            out1+=3
        if (line[1] == 0):
            out2 += (line[0] -1)%3
        if (line[1] == 1):
            out2 += 3 + line[0];
        if (line[1] == 2):
            out2 += 6 + (line[0]+1)%3
        line = f.readline() 

print("part 1:" + str(out1))
print("part 2:" + str(out2))
