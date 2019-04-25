hello_str = "    \t\n\r"
# 判断是否都是空白字符（含空格、换行、回车等）
print(hello_str.isspace())


num_str = "1.2, \u00b2"
num_str2 = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

print(num_str2.isdecimal())
print(num_str2.isdigit())
print(num_str2.isnumeric())


