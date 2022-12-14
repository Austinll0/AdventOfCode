
def flash(map,y,x):
  out = 1
  for i in range(-1,2):
    if y+i < 0 or y+i >= len(map):
      continue
    for j in range(-1,2):
      if i == 0 and j == 0:
        continue
      if x+j < 0 or x+j >= len(map[0]):
        continue

      map[y+i][x+j] += 1
      if map[y+i][x+j] == 10:
        out += flash(map,y+i,x+j)

  return out

map = []
flashes = 0
numSteps = 100
for i in open("2021/day11in.txt").readlines():
  line = []
  if i[-1] == "\n":
    i = i[:-1]
  for j in range(len(i)):
    line.append(int(i[j]))
  map.append(line)
simultaneous = False
step = 0
while not simultaneous:
  step += 1
  #print(map)
  for i in range(len(map)):
    for j in range(len(map[i])):
      map[i][j] += 1
      if(map[i][j] == 10):
        flashes += flash(map,i,j)
  simultaneous = True
  for i in range(len(map)):
    for j in range(len(map[0])):
      if map[i][j] >= 10:
        map[i][j] = 0
      else:
        simultaneous = False
  step += 0
  if(numSteps == step):
    print("Part 1: " + str(flashes))

print("part 2: " +str(step))
