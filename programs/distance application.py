import numpy as np


k, m, n = map(int, input().split())

coordinates = m*[None]
for i in range(m):
    coordinates[i] = list(map(float, input().split()))
    
coordinates = np.array(coordinates)

selections = np.array(list(map(int, input().split())))
selections.shape = (selections.size, 1)
    
result = ""    
for i in range(n):
    point = np.array(list(map(float, input().split())))
    dist = np.transpose(np.sum(np.abs(coordinates-point)**2,axis=1)**(1./2))
    dist.shape = (dist.size, 1)
    vectors = np.concatenate((selections, dist), axis=1)
    
    vectors = vectors[vectors[:, 1].argsort()]
    
    vector = vectors[:,0][0:k]    
    result += str(np.bincount(vector.astype(int)).argmax()) + " "

print(result)