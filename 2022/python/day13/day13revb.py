import time;

def compare(left, right):
    for i in range(len(left)):
        l = left[i];
        try:
            r = right[i];
        except: 
            return -1;
        ltype = type(l);
        rtype = type(r);
        if ltype is int and rtype is int:
            if l < r:
                return 1;
            if r < l:
                return -1;
        elif ltype is list and rtype is int: 
            val = compare(l,[r]);
            if val != 0:
                return val;
        elif ltype is int and rtype is list:
            val = compare([l],r);
            if val != 0:
                return val;
        elif ltype is list and rtype is list:
            val = compare(l,r);
            if val != 0:
                return val;
    if len(left) < len(right):
        return 1;
    return 0;


def parse(line,val):
    out = [];
    i = val;
    while line[i] != "]":
        if line[i] == ",":
            i = i + 1
            continue;
        if line[i] == "[":
            new = parse(line,i+1);
            i = new[1] + 1;
            out.append(new[0]);
        else:
            j = i + 1;
            while line[j] not in [ ",","]"]:
                j += 1;
            out.append(int(line[i:j]));
            i = j
    return [out,i];

start = time.time();
p1 = 0;
with open("day13in.txt") as f:
    i = 1;
    line = f.readline();
    while line:
        l = parse(line,1)[0];
        r = parse(f.readline(),1)[0];
        if compare(l,r) != -1:
            p1 += i;
        f.readline();
        line = f.readline();
        i += 1
print("Part 1:", p1,"in",time.time()-start,"s");
start = time.time();
packets = [];
for line in open("day13in.txt"):
    if line == "\n":
        continue;
    packets.append(parse(line,1)[0]);
packet1 = parse("[[2]]",1)[0];
packet2 = parse("[[6]]",1)[0];
div1 = 0;
div2 = 0;
for p in packets:
    if compare(p,packet1) == 1:
        div1 += 1;
        div2 += 1;
    elif compare(p,packet2) ==1:
        div2 += 1;
print("Part 2: ",div1*div2,"in",time.time()-start,"s");
