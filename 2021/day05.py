class hashMap:
  def __init__(self, mapSize):
    self.Map = [];
    self.mapSize = mapSize
    for i in range(mapSize):
      self.Map.append([])

  def makeKey(self,point):
    #print(point)
    
    key = point[0] * point[1] % self.mapSize
    #print(key)
    return key
  def append(self, point):
    self.Map[self.makeKey(point)].append(point)
  
  def contains(self,point):
    for p in self.Map[self.makeKey(point)]:
      if p[0] == point[0] and p[1] == point[1]:
        #print(p)
        #print(point)
        return True
      print(p)
      print(point)
      print(" ")

    return False
  
  def pop(self):
    for a in self.Map:
      if a:
        return a.pop(0)
    return []
  def isEmpty(self):
    for a in self.Map:
      if a:
        return False
    return True
  def print(self):
    for a in self.Map:
      for b in a:
        print(b)


class Line:
  def __init__(self,p1,p2):
      mapSize = 50
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
intersections = []

with open("2021/day05in.txt") as f:
  for input in f.readlines():
    points = input.split(" -> ")
    Lines.append(Line(points[0].split(","), points[1].split(",")))

while len(Lines):
  #print(len(Lines))
  l1 = Lines.pop(0)
  l1.points.print()
  for l2 in Lines:
    while not l1.points.isEmpty():
      p1 = l1.points.pop()
      #print(p1)
      #print("p1: " + str(p1))
      if l2.points.contains(p1):
        intersections.append(p1)
print(len(intersections))
          


