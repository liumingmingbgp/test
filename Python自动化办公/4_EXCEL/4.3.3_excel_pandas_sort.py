import pandas as pd
people = pd.read_excel('pandas3.xlsx', index_col='ID')
people.sort_values(by='工资', inplace=True, ascending=False)
print(people)
people.sort_values(by=['靠谱', '工资'], inplace=True, ascending=[True, False])
print(people)