import heapq
class box:
    def __init__(self,pts):
        pts = pts.split(",")
        self.x = int(pts[0])
        self.y = int(pts[1])
        self.z = int(pts[2])
        self.chain = 0
        
    def __repr__(self):
        x = str(self.x)
        y = str(self.y)
        z = str(self.z)
        return x + " " + y + " " + z
    def getDist(self,B):
        dX = (self.x-B.x)**2
        dY = (self.y-B.y)**2
        dZ = (self.z-B.z)**2
        return (dX + dY + dZ) ** 0.5
    def checkClosest(self,B):
        d = self.getDist(B)
        if d < self.closest[1]:
            self.closest = [B,d]
def insert(A,arr):
    #link format [box1,box2,dist]
    # insert with shortest dist at front
    for i in range(len(arr)):
        if A[2] < arr[i][2]:
            arr.insert(i,A)
            return
    arr.append(A)
def merge(A,B):
    while(B):
        b = B.pop()
        b.chain = A
        if b not in A: A.append(b)
def applyLink(chains,links):
    c = heapq.heappop(links)
    if not( c[1].chain or c[2].chain):
        newChain = [c[1],c[2]]
        chains.append(newChain)
        c[1].chain = newChain
        c[2].chain = newChain
        return c
    if c[1].chain ==  c[2].chain:
        return c
    if c[1].chain and c[2].chain:
        chains.remove(c[2].chain)
        merge(c[1].chain,c[2].chain)
        return c
    if c[2].chain:
        c[2].chain.append(c[1])
        c[1].chain = c[2].chain
    else: 
        c[1].chain.append(c[2])
        c[2].chain = c[1].chain
    return c

    
ex = False
link = "Day08ex.txt"
connections = 10
if not ex:
    link = "Day08in.txt"
    connections = 1000
boxes = open(link,"r").read().split("\n")
boxes.pop()
boxes = [box(b) for b in boxes]

links = []
for i in range(len(boxes)):
    closest = []
    for j in range(i+1,len(boxes)):
        A = boxes[i]
        B = boxes[j]
        d = A.getDist(B)
        heapq.heappush(links,[d,A,B])
chains = []
for i in range(connections):
    applyLink(chains,links)
nums = [len(c) for c in chains]
nums = sorted(nums,reverse=True)
print(nums[0]*nums[1]*nums[2])
part2 = 0;
while(len(chains[0]) != len(boxes)):
    part2 = applyLink(chains,links)
print(part2[1].x * part2[2].x)
