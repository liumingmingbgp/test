from docx import Document
from deepdiff import DeepDiff

def get_doc_value(path):
    doc = Document(path)
    tables = doc.tables
    table = tables[0]
    all_values = []
    for row in table.rows:
        values = []
        for cell in row.cells:
            values.append(cell.text)
        all_values.append(values)
    return all_values

table1 = get_doc_value('table.docx')
print(table1)
table2 = get_doc_value('table_modify.docx')
print(table2)

diff = DeepDiff(table1, table2)
print(diff)