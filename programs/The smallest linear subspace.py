import numpy as np

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

m, n = map(int, input().split())

vectors = n*[0]
for i in range(n):
    vectors[i] = list(map(float, input().split()))
    
matrix = calculate_RREF(np.array(vectors).T)

t = 0
if n<=m:
    for i in range(m):
        if matrix[i][i] == 0:
            t+=1
else: 
    for i in range(m):
        if np.all(matrix[i][0:-1]==0):
            t+=1    
print(m-t)