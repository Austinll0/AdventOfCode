import math
part1 = 0
part2 = 0

def part1(nums,ops):
    ans = [];
    out = 0;
    for o in ops:
        if o == "*": ans.append(1)
        else: ans.append(0)

    for i in range(len(nums)):
        n = nums[i]
        k = i % len(ops)
        o = ops[k]
        if o == "+": ans[k] += n
        else: ans[k] *= n
    for n in ans:
        out += n
    return out
def leadZeros(nums):
    setLength = 4;
    for i in range(len(nums)):
        nums[i] = nums[i] * (10 ** (4-(math.floor(math.log10(nums[i]))+1)))
nums = []
ops = []
with open("Day06ex.txt","r") as f:
    cha = f.read(1);
    buf = "";
    while(cha):
        if cha == '\n' or cha == ' ':
            if len(buf) > 0:
                nums.append(int(buf))
                buf = ""
            cha = f.read(1)
            continue;
        if cha == "+" or cha == "*":
            ops.append(cha)
            cha = f.read(1)
            continue
        buf += cha
        cha = f.read(1) 

print(part1(nums,ops))

leadZeros(nums)
print(nums)
