name_list = ['zhangsan', '小美眉', '李四', 'wangwu', '李四', '王小二', '孙悟空', '猪二哥']

list_len = len(name_list)
print("列表中有 %d 个元素" % list_len)

count = name_list.count('李四')
print("李四出现了 %d 次" % count)

name_list.remove('王小二')
print(name_list)