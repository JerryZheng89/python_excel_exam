import pandas as pd

#读取 Excel 文件

df = pd.read_excel('./pyxl_test.xlsx', sheet_name='Sheet1')

print(df)
