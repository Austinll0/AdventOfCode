def score(height, view):
    for i in range(len(view)):
        if int(view[i]) >= height:
            return i + 1;
    return -1;
out1 = 0;
out2 = 0;
map = "";
width = 0;
height = 0;
with open("day8in.txt") as f:
    line = f.readline().strip();
    width = len(line);
    while(line):
        map += line;
        height += 1;
        line = f.readline().strip();
for x in range(width):
    for y in range(height):
        visible = False;
        if x == 0 or x == width-1 or y == 0 or y == height-1:
            out1 += 1;
            continue;
        viewScore = 1;
        position = y*width + x;
        val = score(int(map[position]), map[position - width : 0  : -width]);
        if val == -1:
            viewScore *= y;
            visible = True;
        else: 
            viewScore *= val; 
        val = score(int(map[position]), map[position + width : width*height : width]);
        if val == -1:
            visible = True;
            viewScore *= height - y-1;
        else: 
            viewScore *= val;
        val = score(int(map[position]), map[position + 1: position + width - x: 1]);
        if val == -1:
            visible = True;
            viewScore *= width - x-1;
        else: 
            viewScore *= val
        val = score(int(map[position]), map[y * width: position : 1][::-1]);
        if val == -1:
            visible = True;
            viewScore *= x;
        else:
            viewScore *= val;
        if visible:
            out1 += 1;
        if viewScore > out2:
            out2 = viewScore;
print("Part 1: " + str(out1));
print("Part 2: " + str(out2));
