from sys import stdin, maxsize
import numpy as np

input = stdin.readline
    

def main():
    a = np.array(list(map(int, input().split())))
    b = np.array(list(map(int, input().split())))

    size_a = a.size
    size_b = b.size
    
    result = np.zeros(size_a+size_b-1, dtype=np.int64)
    
    for i in range(size_a):
        result[i:i+size_b] += a[i]*b
        
    np.set_printoptions(threshold=maxsize)
    print(result)
    
main()