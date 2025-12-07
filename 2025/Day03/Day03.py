part1 = 0
part2 = 0
def jolt(line,digits):
    nums = list(line[len(line)-digits:len(line)])
    for i in range(digits):
        nums[i] = int(nums[i])
    for i in range(len(line)-1-digits,-1,-1):
        k = int(line[i])
        for j in range(len(nums)):
            if nums[j] <= k:
                nums[j],k = k, nums[j]
            else: break
    joltage = 0;
    for i in range(digits):
        joltage += nums[i]*10**(digits-i-1)
    return joltage
    
with open("Day03in.txt") as f:
   line = f.readline().strip()
   while(line):
       part1 += jolt(line,2)
       part2 += jolt(line,12)
       line = f.readline().strip()
print(part1)
print(part2)
