from docx import Document
from docx.shared import Inches

doc = Document()
doc.add_picture('ICON.jpeg', width=Inches(1.25))

doc.save('new2.docx')