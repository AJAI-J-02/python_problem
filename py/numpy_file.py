import numpy as np

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])


trans=np.transpose(matrix)
t=np.trace(matrix)
print(trans)