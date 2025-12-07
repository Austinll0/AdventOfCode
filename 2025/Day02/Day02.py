import math
def p1check(i):
    l = math.floor(len(str(i))/2)
    m = 10**l
    if math.floor(i/m) == (i%m):
       return i
    return 0 
   
def p2check(i):
    l = str(i)
    for k in range(1,math.floor(len(l)/2)+1):
        check = l[0:k]
        num = len(l)/len(check)
        if num % 1 > 0:
            continue;
        if l.count(check) == num:
            print(l,check,num)
            return i
    return 0


       
        
part1 = 0
part2 = 0
with open("Day02in.txt") as f:
    vals = f.readline()

vals = vals.split(",")
ranges = [];
for val in vals:
    thing = val.split("-")
    thing[0] = int(thing[0])
    thing[1] = int(thing[1])
    ranges.append(thing)

for r in ranges:
    for i in range(r[0], r[1]+1):
        part1 += p1check(i)
        part2 += p2check(i)
print(part1)
print(part2)




