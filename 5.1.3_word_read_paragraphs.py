from docx import Document

doc = Document('new_exist.docx')
for p in doc.paragraphs:
    print(p.text)
