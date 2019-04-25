import numpy as np

a = np.array([2,2.3,4],dtype=np.int) #是以小数还是整数的形式存在
print(a)
print(a.dtype)

a = np.array([2,2.3,4],dtype=np.int64)
print(a)
print(a.dtype)

a = np.array([2,2.3,4],dtype=np.float) #是以小数还是整数的形式存在
print(a)
print(a.dtype)

a = np.array([[1,2,3],
                  [2,3,4]])  #列表转化为矩阵
print(a)

a = np.empty((3,4))
print(a)

a = np.zeros((3,4))
print(a)

a = np.ones((3,4))
print(a)

a = np.arange(10,20,2) #10-19的数据，2步长
print(a)

a= np.arange(12).reshape((3,4)) #三行四列，0到11
print(a)

a = np.linspace(1,10,5)  #线段，开始端1，结束10，且分割为5段
print(a)

a = np.linspace(1,10,6).reshape((2,3))
print(a)