import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html
# matplotlib 仅仅是用来 show 图片的, 即 plt.show()
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# 为了方便观看效果, 我们累加这个数据
data = data.cumsum()
data.plot()
plt.show()

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
data = data.cumsum()
data.plot()
plt.show()

# plot 和 scatter. 因为scatter只有x，y两个属性，我们我们就可以分别给x, y指定数据
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()