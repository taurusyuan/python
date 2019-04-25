import numpy as np

a = np.arange(4)

b = a
c = a
d = b
a[0] = 11  # 改变a的第一个值，b,c,d同时都会发生变化，四个变量是关联的
print(a)
print(b is a, c is a, d is a)

# 如果不想改变b,c,d, 即不想要关联各个变量的话,则使用copy()
b = a.copy()    # deep copy
print(b)        # array([11, 22, 33,  3])
a[3] = 44
print(a)        # array([11, 22, 33, 44])
print(b)        # array([11, 22, 33,  3])

