import statistics
out1 = 0
out2 = []
openers = ['[', '{', '<','(']
closers = [']', '}', '>',')']
syntScore =   [57, 1197,25137,3]
correctScore = [2,3,4,1]
for line in open("2021/day10in.txt").readlines():
  queue = []
  score = 0
  for i in range(len(line)):
    c = line[i]
    if c == "\n":
      for j in queue:
        score = score * 5 + correctScore[openers.index(j)]
      out2.append(score)
      continue
    if(c in openers):
      queue.insert(0,c)
    elif(c != closers[openers.index(queue.pop(0))]):
      out1 = out1 + syntScore[closers.index(c)]
      break
out2.sort()
print(len(out2))
print("part 1: " + str(out1))
print("part 2: " + str(statistics.median(out2)))

