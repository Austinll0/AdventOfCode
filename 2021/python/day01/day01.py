with open('2021/day01in.txt') as f:
  prev = [0, 0, 0] #will track the value of the height 3 ago
  p1 = -1 #account for initial
  p2 = -3 #account for initial 3
  while True:
    num = f.readline()
    if num == '':
      break
    num = int(num)
    if num > prev[0]:
      p1 = p1 + 1;
    if num > prev[2]:
      p2 = p2 + 1;
    
    prev[2] = prev[1];
    prev[1] = prev[0];
    prev[0] = num;

  print("Part 1: " + str(p1))
  print("Part 2: " + str(p2))
    
