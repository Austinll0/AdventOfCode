
line = open("Day06in.txt","r").read().split("\n")
line.pop(-1)

opsline = line.pop(-1)
op = "";

digits = len(line)
buf = 0;
part2 = 0;
for l in line:
    print(len(l),len(opsline))
for i in range(len(opsline)):
    num = 0
    if opsline[i] != ' ':
        op = opsline[i];
        part2 += buf
        print("buf: ",buf)
        if op == '*': buf = 1;
        else: buf = 0;

    for j in range(digits):
        c = line[j][i]
        if c == ' ': continue
        num *= 10;
        num += int(c)
    if num == 0: continue
    print(num)
    if op == '*': buf *= num
    else: buf += num
part2 += buf

print(part2)
