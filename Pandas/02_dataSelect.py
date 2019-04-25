import pandas as pd
import numpy as np

dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])

print(df)
print(df['A'])  #简单的筛选
print(df.A)     #同 print(df['A'])
print(df[0:3])   # 让选择跨越多行
print(df['20190102':'20190104']) # 让选择跨越多行
print(df.loc['20190102']) # 通过标签loc选择某一行数据
print(df.loc[:,['A','B']])  # 通过标签loc选择某几列数据
print(df.loc['20190102':'20190104',['A','C']]) #通过标签loc选择某几行中的某几列数据

# 可以采用位置进行选择 序列iloc, 通过位置选择在不同情况下所需要的数据，例如选某一个，连续选或者跨行选等操作
print(df.iloc[3,1])
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],[1,3]]) #通过标签iloc选择某几行中的某几列数据

print(df.ix[:3,['A','C']]) # ix
print(df[df.A>8]) # 通过判断的筛选