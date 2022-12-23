from openpyxl import load_workbook
wb = load_workbook(filename='big.xlsx', read_only=True)
ws = wb['big']

for row in ws.rows:
    for cell in row:
        print(cell.value)