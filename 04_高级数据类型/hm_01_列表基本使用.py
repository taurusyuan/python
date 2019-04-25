name_list = ["zhangsan", "lisi", "wangwu"]

print(name_list[0])
print(name_list.index("wangwu"))
name_list[1] = "李四"
name_list.append("王小二")
print(name_list)
name_list.insert(1, '小美眉')
print(name_list)
temp_list = ["孙悟空", "猪二哥"]
name_list.extend(temp_list)
print(name_list)
name_list.remove("wangwu")
print(name_list)
name_list.pop(3)
print(name_list)
name_list.pop()
print(name_list)
del name_list[1]
# del本质上是从内存上删除 
print(name_list)
name_list.clear()
print(name_list)
