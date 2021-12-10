import math

position = [];

def calcFuel(val):
  return sum(range(val+1))

with open("2021/day07in.txt") as f:
  input = f.readline().split(",")
  for i in input:
    position.append(int(i))

out = 999999
out2 = 0
for i in range(max(position)):
  val = 0
  for j in position:
    val = val + abs(i - j)
  if(out < val):
    print("part 1: " + str(out))
    break
  out = val
avg = math.floor(sum(position)/len(position)) - 1#idk why this works with -1, but it's required
print(avg)
for i in position:
  out2 = out2 + calcFuel(abs(i - avg))
print(out2)


