import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
C = np.vstack((A,B))   #上下合并vstack
D = np.hstack((A,B))   #左右合并hstack
print(A)
print(B)
print(C)
print(D)
print(A.shape,C.shape,D.shape)

# A是序列，不是矩阵，转置操作便很有可能无法对其进行转置（因为A并不是矩阵的属性），此时就需要我们借助其他的函数操作进行转置：
print(A[np.newaxis,:])
print(A[np.newaxis,:].shape)
print(A[:,np.newaxis])
print(A[:,np.newaxis].shape)

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
C = np.vstack((A, B))  # vertical stack
D = np.hstack((A, B))  # horizontal stack
print(C)
print(D)

# axis参数很好的控制了矩阵的纵向或是横向打印，相比较vstack和hstack函数显得更加方便。
E = np.concatenate((A,B,B,A),axis=0)  #纵向合并
print(E)
E = np.concatenate((A,B,B,A),axis=1)  #横向合并
print(E)