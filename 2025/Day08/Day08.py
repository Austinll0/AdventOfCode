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
ex = False
link = "Day08ex.txt"
connections = 10
if not ex:
    link = "Day08in.txt"
    connections = 1000
boxes = open(link,"r").read().split("\n")
boxes.pop()
boxes = [box(b) for b in boxes]

links = [];
for i in range(len(boxes)):
    closest = []
    for j in range(i+1,len(boxes)):
        A = boxes[i]
        B = boxes[j]
        d = A.getDist(B)
        if len(closest) < 10:
            insert([A,B,d],closest)
            continue
        elif d < closest[-1][2]:
            insert([A,B,d],closest)
            closest.pop()
    for c in closest:
        insert(c,links)
chains = []

for i in range(connections):
    c = links[i]
    if not( c[0].chain or c[1].chain):
        newChain = [c[0],c[1]]
        chains.append(newChain)
        c[0].chain = newChain
        c[1].chain = newChain
        continue;
    if c[0].chain ==  c[1].chain:
        continue;
    if c[0].chain and c[1].chain:
        chains.remove(c[1].chain)
        merge(c[0].chain,c[1].chain)
        continue;
    if c[1].chain:
        c[1].chain.append(c[0])
        c[0].chain = c[1].chain
    else: 
        c[0].chain.append(c[1])
        c[1].chain = c[0].chain
nums = [len(c) for c in chains]
nums = sorted(nums,reverse=True)
print(nums[0]*nums[1]*nums[2])
