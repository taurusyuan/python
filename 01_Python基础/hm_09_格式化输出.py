price = float(input("苹果的单价："))
weight = float(input("苹果的重量："))
money = price * weight
scale = 0.25
print("苹果单价 %.2f 元/斤，购买了 %.2f 斤，共计 %.2f 元" % (price, weight, money))
print("数据比例是 %.2f%%" % (scale*100))

if a == 1 :
    print()