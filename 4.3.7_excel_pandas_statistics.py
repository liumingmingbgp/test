import pandas as pd

people = pd.read_excel('pandas7.xlsx', index_col='ID')
# print(people)
col_name = ['小测1','小测2','小测3']
# print(people['小测2'])
row_sum = people[col_name].sum(axis=1)
row_mean = people[col_name].mean(axis=1)
# print(people)
total = '总分'
average = '平均分'
people[total] = row_sum
people[average] = row_mean
col_name += [total, average]

col_mean = people[col_name].mean()
col_mean['名称'] = 'Summary'
people = people.append(col_mean, ignore_index = True)
print(people)