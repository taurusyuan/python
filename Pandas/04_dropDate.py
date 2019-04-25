import pandas as pd
import numpy as np

dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0,:4] = np.nan
df.iloc[1,2] = np.nan
print(df)

df1=df.dropna(
    axis=0,     # 0: 对行进行操作; 1: 对列进行操作
    how='any'   # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
    )
print(df1)

df2=df.dropna(
    axis=0,     # 0: 对行进行操作; 1: 对列进行操作
    how='all'   # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
    )
print(df2)

# 如果是将 NaN 的值用其他值代替, 比如代替成 0:
df3=df.fillna(value=0)
print(df3)

#判断是否有缺失数据 NaN, 为 True 表示缺失数据:
df4=df.isnull()
print(df4)

#检测在数据中是否存在 NaN, 如果存在就返回 True:
print(np.any(df.isnull()) == True)