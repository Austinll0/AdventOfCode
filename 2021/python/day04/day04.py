def checkBingo(nums,card):
  soonest = 9999
  for i in range(5):
    hfail = False
    vfail = False
    for j in range(5):
      if card[i][j] not in nums:
        hfail = True
      if card[j][i] not in nums:
        vfail = True
    if(not hfail):
      h = [];
      for j in range(5):
        h.append(nums.index(card[i][j]))
      soonest = min([soonest, max(h)]) 
      
    if(not vfail):
      h = []
      for j in range(5):
        h.append(nums.index(card[j][i]))
      
      soonest = min([soonest, max(h)]) 
      
  return soonest

#nums is shortened to win time
def score(nums, card):
  score = 0
  for i in range(5):
    for j in range(5):
      if card[i][j] not in nums:
        score += card[i][j]
  score = score * nums[-1]
  return score


best = 0
worst = 0
soonest = 9999
lastest = 0
nums = 0
cards = []
with open("2021/day04in.txt") as f:
  nums = f.readline().split(",")
  for i in range(len(nums)):
    nums[i] = int(nums[i])
  input = list(filter(lambda val: val != '\n', f.readlines())) # remove new lines

  while(len(input)):
    card = []
    for i in range(5):
      card.append(input.pop(0));
    cards.append(card)
  for c in cards:
    for i in range(5):
      c[i] = list(filter(lambda val: val != "", c[i].split(" ")))
      for j in range(5):
        c[i][j] = int(c[i][j])
    out = checkBingo(nums,c)
    if out < soonest:
      soonest = out
      best = c
    if out > lastest:
      lastest = out
      worst = c
    
  print("part 1: "  + str(score(nums[0:soonest+1],best)))
  print("part 2: "  + str(score(nums[0:lastest+1],worst)))
    

      
    
  



