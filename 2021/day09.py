
def bfs(map, start):
  out = 1
  M = len(map)
  N = len(map[i])
  queue = [start]
  visited =  [[0 for i in range(N)] for j in range(M)]
  visited[start[1]][start[0]] = 1
  while(queue):
    p = queue.pop(0)
    x = p[0]
    y = p[1]

    if(int(map[y][x-1]) < 9 and visited[y][x-1] < 1):
      visited[y][x-1] = 1
      out = out + 1
      queue.append([x-1, y])
    if(int(map[y][x+1]) < 9 and visited[y][x+1] < 1):
      visited[y][x+1] = 1
      out = out + 1
      queue.append([x+1, y])
    if(int(map[y-1][x]) < 9 and visited[y-1][x] < 1):
      visited[y-1][x] = 1
      out = out + 1
      queue.append([x,y-1])
    if(int(map[y+1][x]) < 9 and visited[y+1][x] < 1):
      visited[y+1][x] = 1
      out = out + 1
      queue.append([x, y+1])

  return out



map = []
largest = [0 , 0 , 0]
out1 = 0
out2 = 1
with open("2021/day09in.txt") as f:
  for l in f.readlines():
    if(l[-1] == "\n"):
      l = l[:-1]
    map.append("9" + l +"9")
  s = ""
  for i in range(len(map[0])):
    s = s + "9"
  map.insert(0,s)
  map.append(s)


for i in range(1,len(map)-1):
  for j in range(1,len(map[0])-1):
    val = int(map[i][j])
    up = int(map[i-1][j])
    down = int(map[i+1][j])
    left = int(map[i][j-1])
    right = int(map[i][j+1])
    if val < up and val < down and val < right and val < left:
      out1 = out1 + val + 1
      val = bfs(map,[j, i])
      if min(largest) < val:
        largest[largest.index(min(largest))] = val
  
print("Part 1: " + str(out1))
print("Part 2: " + str(largest[0] * largest[1] * largest[2]))
