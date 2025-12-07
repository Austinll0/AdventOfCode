import time
def combo(comboCode,A,B,C):
    if comboCode in {0,1,2,3}:
        return comboCode
    if comboCode == 4:
        return A
    if comboCode == 5:
        return B
    if comboCode == 6:
        return C
        

def adv(comboCode,A,B,C):
    return int(A / pow(2,combo(comboCode,A,B,C)));
def bxl(literal,B):
    return literal ^ B
def bst(comboCode,A,B,C):
    return combo(comboCode,A,B,C) % 8
def bxc(B,C):
    return B^C
def out(comboCode,A,B,C):
    return combo(comboCode,A,B,C) % 8
def bdv(comboCode,A,B,C):
    return adv(comboCode,A,B,C)
def cdv(comboCode,A,B,C):
    return adv(comboCode,A,B,C)
def process(A,B,C,ops):
    string = "";
    i = 0;
    while i < len(ops):
        fun = ops[i]
        code = ops[i+1];
        match fun:
            case 0:
                A = adv(code,A,B,C)
            case 1:
                B = bxl(code,B)
            case 2:
                B = bst(code,A,B,C)
            case 3: 
                if A != 0:
                    i = code - 2
            case 4:
                B = bxc(B,C)
            case 5:
                string += str(out(code,A,B,C)) + ","             
            case 6:
                B = bdv(code,A,B,C)
            case 7:
                C = cdv(code,A,B,C)
        i += 2
    string = string[0:len(string)-1]
    return string 
def compare(A,B,C,ops,line):
    string = "";
    i = 0;
    j = 0;
    while i < len(ops):
        fun = ops[i]
        code = ops[i+1];
        match fun:
            case 0:
                A = adv(code,A,B,C)
            case 1:
                B = bxl(code,B)
            case 2:
                B = bst(code,A,B,C)
            case 3: 
                if A != 0:
                    i = code - 2
            case 4:
                B = bxc(B,C)
            case 5:
                string += str(out(code,A,B,C)) + ","             
                for k in range(len(string)):
                    if string[k] != line[k]:
                        return
            case 6:
                B = bdv(code,A,B,C)
            case 7:
                C = cdv(code,A,B,C)
        i += 2
    string = string[0:len(string)-1]
    return string 


A = -1;
B = -1;
C = -1;


with open("Day17in.txt") as f:
    A = int(f.readline().split(": ")[1])
    B = int(f.readline().split(": ")[1])
    C = int(f.readline().split(": ")[1])
    f.readline()
    line = f.readline().split(": ")[1]
    ops = [int(i) for i in line.strip().split(",")]
print(process(A,B,C,ops))

i = 0;
while compare(i,0,0,ops,line) != line:
    i += 1
print(i)
