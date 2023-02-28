from mailmerge import MailMerge

doc = MailMerge('入职证明.docx')

doc.merge(name='田傻傻', 
          id='333333333', 
          year='2020', 
          month='09', 
          department_name='风险投资部', 
          job_name='风险分析师')

doc.write('入职证明_new.docx')