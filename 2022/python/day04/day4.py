out1 = 0;
out2 = 0;
with open("day4in.txt") as f:
    line = f.readline()
    while(line):
        line = line.strip().replace('-',',').split(",");
        for i in range(4):
            line[i] = int(line[i])
        if(line[0] <= line[2] and line[1] >= line[3]):
            out1 += 1;
            out2 += 1;
        elif(line[0] >= line[2] and line[1] <= line[3]):
            out1 += 1;
            out2 += 1;
        elif(line[0] <= line[2] and line[1] >= line[2]):
            out2 += 1;
        elif(line[0] <= line[3] and line[1] >= line[3]):
            out2 += 1;
        line = f.readline()
print("Part 1:" + str(out1))
print("Part 2:" + str(out2))
