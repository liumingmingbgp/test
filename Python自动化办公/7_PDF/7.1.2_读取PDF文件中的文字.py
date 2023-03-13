import fitz
from pathlib import Path

pdfpath = Path('7_PDF\Continuous_Recording.pdf')

def extract_all_document_text():
    pdf = fitz.open(pdfpath)
    content = ''
    for page in pdf:
        text = page.get_text()  # getText()方法更新为get_text()
        content += text
    with open('7_PDF\荷塘月色1.txt', 'w') as f:
        f.write(content)

extract_all_document_text()