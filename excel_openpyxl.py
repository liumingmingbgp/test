import openpyxl
wb = openpyxl.load_workbook('test.xlsx')
ws = wb.worksheets[0]
print(ws.cell(row=3, column=2).value)
