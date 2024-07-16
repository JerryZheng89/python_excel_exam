import matplotlib.pyplot as plt
import pandas as pd

#读取 Excel 文件

df = pd.read_excel('./pyxl_test.xlsx', sheet_name='Sheet1')


df['No.'].hist()
plt.show()
plt.scatter(df['X'], df['Y'])
plt.show()
