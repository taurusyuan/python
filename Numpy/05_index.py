import numpy as np

A = np.arange(3, 15)
print(A)
print(A[2])
A = np.arange(3,15).reshape((3,4))
print(A)
print(A[2])
print(A[2,2])
print(A[2][2])
print(A[2,:])
print(A[1, 1:3])  #第1行的第1列到第3列（不包含第3列的值），从0行0列开始

for row in A:
    print(row)
print(A.T)
for column in A.T:
    print(column)
print(A.flatten())

for item in A.flat:
    print(item)