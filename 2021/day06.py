import time

input = open("2021/day06in.txt").readline().split(',')
numdays = 256
start = time.time()
     #  0 1 2 3 4 5 6 7 8
fish = [0,0,0,0,0,0,0,0,0]
for i in range(len(input)):
  num = int(input[i])
  fish[num] = fish[num] + 1
for i in range(numdays):
  temp = fish[0];
  for j in range(8):
    fish[j] = fish[j+1]
  fish[8] = temp
  fish[6] = fish[6] + temp
  if(i == 79):
    print(time.time() - start)
    print("part 1: " + str(sum(fish)))

print(time.time() - start)
print("part 2:" + str(sum(fish)))
