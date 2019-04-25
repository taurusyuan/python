# 导入随机数工具包
import random

player = int(input("请输入您要输入的手势 石头1 剪刀2 布3:"))
computer = random.randint(1, 3)
# random.randint(1, 3) 随机输出1-3之间的整数
print("玩家选择的是手势是 %d, 电脑选择的手势是 %d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")
