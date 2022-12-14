f = open("day6in.txt")
line = f.readline().strip();

for i in range(4,len(line)):
    if( len(set(line[i-4:i])) == 4 ):
        print("part 1: " + str(i));
        break;
for i in range(14,len(line)):
    if( len(set(line[i-14:i])) == 14):
        print("part 2: " + str(i));
        break;
