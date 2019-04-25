import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n) #生成0-11的数字
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内。
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

#函数plt.text分别在柱体上方（下方）加上数值
for x, y in zip(X, Y1):  #zip相当于打包两个值进行同时传值
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.01, y + 0.05, '%.2f' % y, ha='center', va='bottom')#描述数字处在图中的位置

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.01, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.xlim(-0.5, n-0.5)
#plt.xticks(())
plt.ylim(-1.25, 1.25)
#plt.yticks(())

plt.show()