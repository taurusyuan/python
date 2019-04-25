import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                       'A': ['A0', 'A1', 'A2', 'A3'],
                       'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
#用merge， 依据key column合并，并打印出
res = pd.merge(left, right, on='key') # on代表依据哪个模块进行合并
print(res)

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                         'C': ['C0', 'C1', 'C2', 'C3'],
                         'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
#依据key1与key2 columns进行合并，并打印出四种结果['left', 'right', 'outer', 'inner']
res1 = pd.merge(left, right, on=['key1', 'key2'], how='inner')
res2 = pd.merge(left, right, on=['key1', 'key2'], how='outer')
res3 = pd.merge(left, right, on=['key1', 'key2'], how='left')
res4 = pd.merge(left, right, on=['key1', 'key2'], how='right')
print(res1)
print(res2)
print(res3)
print(res4)

# indicator=True会将合并的''记录''放在新的一列
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column') # 自定indicator column的名称，并打印出
print(res)


# 依据index合并
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print(left)
print(right)

res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)

# 解决overlapping的问题
import pandas as pd

# 定义资料集
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
# 使用suffixes解决overlapping的问题, 在合并的表格中表头如果是重复的，利用suffixes（后缀）来区别命名
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)





