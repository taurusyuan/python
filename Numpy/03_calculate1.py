import numpy as np
a=np.array([10,20,30,40])   # array([10, 20, 30, 40])
b=np.arange(4)              # array([0, 1, 2, 3])
c0=a-b  # array([10, 19, 28, 37]) #矩阵中元素的差
c1=a+b   # array([10, 21, 32, 43]) #矩阵中元素的和
c2=a*b   # array([  0,  20,  60, 120]) #矩阵中元素的乘积
c3=b**2  # array([0, 1, 4, 9]) #矩阵中元素的逐个平方
print(a,b)
print(c0,c1,c2,c3)
print(b<3)   #矩阵中元素的正误判断
print(b==3)
d=10*np.sin(a)
print(d)

a1=np.array([[1,1],[1,2]])
b1=np.array([[1,0],[3,2]])
c_dor1 = np.dot(a1,b1) #矩阵的乘法
c_dor2 = a1.dot(b1)
print(a1)
print(b1)
print(c_dor1)
print(c_dor2)

e=np.random.random((2,3))
print(e)
print(np.sum(e,axis=1)) #axis=1代表行，所以这个做行和
print(np.min(e,axis=0)) #axis=0代表列
print(np.max(e,axis=1))

