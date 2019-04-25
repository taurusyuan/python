import numpy as np
A = np.arange(-1, 11).reshape((3, 4))
print(A)
# 其中的 argmin() 和 argmax() 两个函数分别对应着求矩阵中最小元素和最大元素的索引，索引指的是所在的位置，而不是元素本身。
print(np.argmin(A))  # 最小值-1在第0位，故输出0
print(np.argmax(A))  # 最大值10在第11位，故输出11
print(np.average(A)) # 均值
print(np.median(A))  # 中位数
print(np.cumsum(A))  # 累差，呈现整个过程
print(np.diff(A))  # 累差，该函数计算的便是每一行中后一项与前一项之差。故一个3行4列矩阵通过函数计算得到的矩阵便是3行3列的矩阵。
print(np.nonzero(A))  # 找出非零元素所在的位置

B = np.arange(14,2,-1).reshape((3,4))
print(B)
print(np.sort(B))  # 排序函数仍然仅针对每一行进行从小到大排序操作
print(np.transpose(B)) # 矩阵的转置1
print(B.T)             # 矩阵的转置2
print(np.clip(B,5,9)) #大于9的数全部变成9，小于5的数全部变成5，其余不变

print(np.mean(B,axis=1)) # 行均值
print(np.mean(B,axis=0,dtype=np.int)) # 列均值
