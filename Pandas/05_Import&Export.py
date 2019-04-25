import pandas as pd


data = pd.read_csv('student.csv')
print(data)

data.to_csv('student2.csv')