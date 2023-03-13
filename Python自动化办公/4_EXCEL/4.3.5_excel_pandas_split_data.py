import pandas as pd
people = pd.read_excel('pandas5.xlsx', index_col='ID')
# print(people)
df = people['Full Name'].str.split(expand=True)
# print(df)
people['姓氏'] = df[0]
people['名字'] = df[1]
print(people)