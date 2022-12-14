out1 = 0;
out2 = 0;

with open("day3in.txt") as f:
    line = f.readline();
    while line:
        comp1 = line[int((len(line) -1)/2):len(line)-1]
        comp2 = line[0:int((len(line)-1)/2)]

        for c in comp1:
            if c in comp2:
                out1 += c.isupper() * (ord(c)-38) + c.islower() * (ord(c)-96)
                break;
        line = f.readline();

print("Part 1: " + str(out1));

with open("day3in.txt") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    while(line1):
        for c in line1:
            if c in line2 and c in line3:
                out2 += c.isupper() * (ord(c)-38) + c.islower() * (ord(c)-96)
                break
        line1 = f.readline();
        line2 = f.readline();
        line3 = f.readline();
print("Part 2: " + str(out2));
