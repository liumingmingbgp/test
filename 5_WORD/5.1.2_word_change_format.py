from win32com import client

doc_path = 'exist.doc'
docx_path = 'new_exist.docx'

Word = client.Dispatch('WPS.Application')
doc = Word.Documents.Open(doc_path)
doc.SaveAs(docx_path, 12)
doc.Close()
Word.Quit()