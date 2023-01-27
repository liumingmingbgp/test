import pandas as pd
student = pd.read_excel('student.xlsx', sheet_name='name')
# print(student)
score = pd.read_excel('score.xlsx', sheet_name='score')
age = pd.read_excel('age.xlsx', sheet_name='age')
table = student.merge(score, how='left', on='ID').fillna(0)
table['分数'] = table['分数'].astype(int)
# print(table)
table2 = table.merge(age, how='left', on='ID').fillna(0)
table2['年龄'] = table2['年龄'].astype(int)
# print(table2)
pass_student = table2[(table2['年龄'] >= 20) & (table2['分数'] >= 60)]
print(pass_student['名称'])