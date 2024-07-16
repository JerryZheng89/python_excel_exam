import pandas as pd

#读取 Excel 文件

df = pd.read_excel('./pyxl_test.xlsx', sheet_name='Sheet1')
df_sorted = df.sort_values(by='No.', ascending=True)

print('sorted NO.: \n', df_sorted)

df_filtered = df[df['No.'] > 5]

print('No > 5: \n', df_filtered)

average = df['No.'].mean()
print('No average: ', average)
