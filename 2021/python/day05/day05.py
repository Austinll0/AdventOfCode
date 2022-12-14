import numpy as np

class Line:
  def __init__(self,p1,p2):
      mapSize = 100
      p1 = [int(p1[0]), int(p1[1])]
      p2 = [int(p2[0]), int(p2[1])]

      self.points = hashMap(mapSize)
      # vertical case
      if(p1[0] == p2[0]):
        start = min([p1[1], p2[1]])
        end = max(p1[1],p2[1])
        for i in range(start,end+1):
          self.points.append([p1[0],i])
      # horizontal case
      elif(p1[1] == p2[1]):
        start = min([p1[0], p2[0]])
        end = max(p1[0],p2[0])
        for i in range(start,end+1):
          self.points.append([i,p1[1]])
      # diagonal class


             

Lines = []
intersections = 0
map = np.zeros([1000, 1000])
with open("2021/day05in.txt") as f:
  for input in f.readlines():
    points = input.split(" -> ")
    p1 = points[0].split(",")
    p1 = [int(p1[0]),int(p1[1])]
    p2 = points[1].split(",")
    p2 = [int(p2[0]),int(p2[1])]
    # vertical case
    if(p1[0] == p2[0]):
      start = min([p1[1], p2[1]])
      end = max(p1[1],p2[1])
      for i in range(start,end+1):
        map[p1[0]][i] = map[p1[0]][i] + 1
    # horizontal case
    elif(p1[1] == p2[1]):
      start = min([p1[0], p2[0]])
      end = max(p1[0],p2[0])
      for i in range(start,end+1):
        map[i][p1[1]] = map[i][p1[1]] + 1
    else:
      #make p1 the more left point to simplify
      if(p1[1] > p2[1]):
        temp = p1;
        p1 = p2;
        p2 = temp
      if(p1[0] < p2[0]):
        for i in range(1 + p2[0]-p1[0]):
          map[p1[0] + i][p1[1] + i] =map[p1[0] + i][p1[1] + i] + 1
      else: 
        for i in range(1 + p1[0]-p2[0]):
          map[p1[0] - i][p1[1] + i] =map[p1[0] - i][p1[1] + i] + 1

for i in range(1000):
  for j in range(1000):
    if(map[i][j] > 1):
      intersections = intersections + 1
print(intersections)