import pandas as pd
from mailmerge import MailMerge

job_seeker = pd.read_excel('求职者.xlsx')
template = '合同.docx'
doc = MailMerge(template)

def merge(name):
    doc.merge(company = '中国移动', employee = name, year='2020', month='09', day='08')
    doc.write(f'求职合同/{name}_合同.docx')

for name in job_seeker['人员姓名']:
    merge(name)
print('done!')
