import numpy as np
A = np.arange(12).reshape((3, 4))
print(A)

print(np.split(A, 3, axis=0)) # 横向对等分割
print(np.split(A, 2, axis=1)) # 纵向对等分割

# 不等项的分割 np.array_split()
print(np.array_split(A, 3, axis=1))

print(np.vsplit(A, 3)) #等于 print(np.split(A, 3, axis=0))
print(np.hsplit(A, 2)) #等于 print(np.split(A, 2, axis=1))