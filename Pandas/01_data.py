import pandas as pd
import numpy as np
# 如果用 python 的列表和字典来作比较, 那么可以说 Numpy 是列表形式的，没有数值标签,而 Pandas 就是字典形式。
# Pandas是基于Numpy构建的，让Numpy为中心的应用变得更加简单

# Series的字符串表现形式为：索引在左边，值在右边
s = pd.Series([1,3,6,np.nan,44,1]) # np.nan就是什么都没有
print(s)

# DataFrame是一个表格型的数据结构，它包含有一组有序的列，每列可以是不同的值类型,它可以被看做由Series组成的大字典
dates = pd.date_range('20190101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20190101'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print(df2.dtypes) # 类型
print(df2.index)  # 列的序号
print(df2.columns)# 数据的名称
print(df2.values) # 值，只能看到数值型的数据的值
print(df2.describe()) #数据的总结
print(df2.T)
print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_index(axis=0, ascending=False))
print(df2.sort_values(by='B'))