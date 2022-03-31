import numpy as np


def print_vector(a, direct):
    result = ""
    seperator = "\r\n"
    if direct == "R":
        seperator= " "
    for i in range(a.size):
        result+= str(int(a[i]))
        result+= seperator
            
    print(result, end="")
    if direct == "R":
        print()
 
            
def dot_product(a, direct, vector):
    if(direct == "C"):
        return
    b = np.array(list(map(int, vector))) 
    if(b.size != a.size):
        return
     
    print(int(np.dot(a,b)))
    
    
def reset(k):
    return np.ones(k)


def cross_product(a, vector):
    if(a.size != 3):
        return
    
    b = np.array(list(map(int, vector))) 
     
    result = np.cross(a, b)
    
    length = np.linalg.norm(result)
    result/=length
    print(format(result[0], ".4f"), format(result[1], ".4f"), format(result[2], ".4f"))
    
    
def hadamard_product(a, vector):
    b = np.array(list(map(int, vector))) 
    
    if(a.size != b.size):
        return (None, 0)
    return (np.multiply(a,b), 1)
    

def out(a, direct, vector, k):
    if direct == "R":
        return (None, 0)
    
    b = np.array(list(map(int, vector)))
    result = np.outer(a,b)
    a = result[k-1]
    return (a, 1)
     
def transpose(direct):
    if direct == "C":
        return "R"
    return "C"


n = int(input())
a = np.ones(n)
direct = "C"

q = int(input())
for i in range(q):
    command = input()
    if command.startswith("print"):
        print_vector(a, direct)
    if command.startswith("T"):
        direct = transpose(direct)
    if command.startswith("dot"):
        dot_product(a, direct, command.split()[1:])
    if command.startswith("reset"):
        a = reset(int(command.split()[1]))
    if command.startswith("cross"):
        cross_product(a, command.split()[1:])
    if command.startswith("out"):
        parts = command.split()
        (output, v) = out(a, direct, parts[1:-2], int(parts[-1]))
        if v == 1:
            a = output
            direct = "R"
    if command.startswith("had"):
        output, v = hadamard_product(a, command.split()[1:])
        if v == 1:
            a = output
