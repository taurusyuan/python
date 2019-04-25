import pandas as pd
import numpy as np
dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
print(df)
df.iloc[2,2] = 1111
df.loc['20190101','B'] = 2222
df.B[df.A>4] = 0
df['F'] = np.nan # 加1列
print(df)
df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20190101',periods=6)) # 添加数据
print(df)