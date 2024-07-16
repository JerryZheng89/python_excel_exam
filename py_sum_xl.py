from openpyxl import Workbook

wb = Workbook()

ws = wb.active

ws['A1'] = '=SUM(1,2,3)'

wb.save('./py_sum.xlsx')
