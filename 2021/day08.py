left = []
right = []
out1 = 0;

def getA(one,seven):
  for i in range(3):
    if seven[i] not in one:
      return seven[i]
def getC(one,options):
  #print(one)
  #print(options)
  for i in range(2):
    for j in options:
      if one[i] not in j:
        #print(one[i])
        return one[i]

def getBDEG(known,options,four):
  #           b,d,e,g
  toReturn = [0,0,0,0]
  for i in range(4):
    l = four[i]
    if l in options[0] and l in options[1] and l in options[2]:
      toReturn[1] = four[i]
      known[3] = four[i]
  for i in range(4):
    if four[i] not in known:
      toReturn[0]
      known[1] = four[i]
  for i in range(5):
    l = options[0][i]
    if l not in known and l in options[1] and l in options[2]:
      known[6] = l
      toReturn[3] = l
  for i in options:
    for j in range(5):
      if i[j] not in known:
        toReturn[2] = i[j]
        known[4] = i[j]

def getF(C,one):
  for i in range(2):
    if one[i] != C:
      return one[i]

with open("2021/day08in.txt") as f:
  puzzleIn = f.readlines()
  for i in puzzleIn:
    i = i.split(" | ")
    left.append(i[0].split(" "))
    right.append(i[1].split(" "))

for i in right:
  for j in i:
    if j[-1] == "\n":
      j = j[:-1]
    L = len(j)
    if L == 2 or L == 3 or L == 4 or L == 7:
      out1 = out1 + 1

out2 = 0
for i in range(len(left)):
  pos = [0,0,0,0,0,0,0]
  j = left[i]
  #     [a,b,c,d,e,f,g]
  j.sort(key = lambda x: len(x))
  #print(i)
  pos[0] = getA(j[0],j[1])
  pos[2] = getC(j[0],j[6:9])
  pos[5] = getF(pos[2], j[0])
  getBDEG(pos,j[3:6],j[2])
  #print(pos)
  num = 0;
  for k in range(len(right[i])):
    l = right[i][k]
    if "\n" in l:
      l = l[:-1]
    val = -1;
    if len(l) == 2:
      val = 1
    elif len(l) == 4:
      val = 4
    elif len(l) == 3:
      val = 7
    elif len(l) == 7:
      val = 8
    elif len(l) == 6 and pos[3] not in l:
      val = 0
    elif len(l) == 6 and pos[4] not in l:
      val = 9
    elif len(l) == 6 and pos[2] not in l:
      val = 6
    elif len(l) == 5 and pos[4] in l:
      val = 2
    elif len(l) == 5 and pos[2] in l:
      val = 3
    elif len(l) == 5:
      val = 5
    if val == -1:
      print(right[i][k])
    num = num*10 + val
  out2 = out2 + num

print("part 1: " + str(out1))
print("part 2: " + str(out2))
