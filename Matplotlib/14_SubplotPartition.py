import matplotlib.pyplot as plt

plt.figure()
# subplot2grid
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3) #3*3的网格里。第0行第0列出发，colspan代表列跨度为3
ax1.plot([1, 2, 3], [1, 2, 4])    # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

ax4.scatter([1, 2], [2, 3])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')

# gridspec
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.figure()
gs = gridspec.GridSpec(3, 3)
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

#subplots
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True) # g共享x,y轴坐标信息
ax13.scatter([1,2], [1,2])
# plt.tight_layout()表示紧凑显示图像, plt.show()表示显示图像
plt.tight_layout()
plt.show()