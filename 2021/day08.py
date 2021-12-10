left = []
right = []
out1 = 0;
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
print("part 1: " + str(out1))
