import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,1,1)  #2*1的中的第1个位置
plt.plot([0,1],[0,1]) #(0,0),(1,1)的两个点连成的线

plt.subplot(2,3,4)  #2*3的中的第4个位置
plt.plot([2,1],[0,2])

plt.subplot(2,3,5)
plt.plot([3,1],[1,3])

plt.subplot(2,3,6)
plt.plot([4,1],[2,3])
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.show()