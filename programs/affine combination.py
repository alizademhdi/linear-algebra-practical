from sys import stdin, stdout
import numpy as np

input, print = stdin.readline, stdout.write

def complite(matrix, row_counter, row, col, i):
    matrix[row_counter, i:col] = matrix[row_counter, i:col] / matrix[row_counter, i];
    vector = matrix[row_counter, i:col]
            
    if row_counter > 0:
        above = np.arange(row_counter)
        matrix[above, i:col] = matrix[above, i:col] - np.transpose(np.outer(vector, matrix[above, i]))
        
    if row_counter < row-1:
        below = np.arange(row_counter+1,row)
        matrix[below, i:col] = matrix[below, i:col] - np.transpose(np.outer(vector, matrix[below, i]))
        
    
                
def calculate_RREF(input_matrix, tol=1e-8):
    matrix = input_matrix.copy()
    row, col = matrix.shape
    
    row_counter = 0
    for i in range(col):
        pivot = np.argmax (np.abs (matrix[row_counter:row,i])) + row_counter
        element = np.abs(matrix[pivot][i])
        if element <= tol:
            matrix[row_counter:row, i] = np.zeros(row-row_counter)
            
        else:
            if pivot != row_counter:
                matrix[[pivot, row_counter], i:col] = matrix[[row_counter, pivot], i:col]
        
            complite(matrix, row_counter, row, col, i)
                
            row_counter += 1
            
        if row_counter == row:
            break;
        
    return matrix

n, m, k = map(int, input().split())

vectors = m*[None]
for i in range(m):
    vectors[i] = list(map(float, input().split()))+[1]
    
vectors = np.array(vectors).T
result = ""
for i in range(k):
    vector = np.array(list(map(float, input().split()))+[1]).T
    
    temp = np.c_[vectors, vector] 
    matrix = calculate_RREF(temp)
   
    v = "YES"
    for j in range(n+1):
        if(np.all((matrix[j][0:-1]==0)) and matrix[j][-1] != 0):
            v = "NO"
            break
        
    result += v + '\n'

print(result)
    
    

    