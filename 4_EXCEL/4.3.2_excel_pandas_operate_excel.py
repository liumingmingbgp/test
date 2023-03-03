import pandas as pd
from datetime import date, timedelta


df = pd.DataFrame({
    'id':[1,2,3],
    'name':['张三','李四','王五'],
    'age':[28,25,30]
})
df = df.set_index('id')
df.to_excel('people.xlsx')


people001 = pd.read_excel('people001.xlsx', skiprows=4, usecols='B:E', dtype={'ID':str, 'gender':str, 'birthday':str})
# print(people001.index)
startday = date(2019,9,1)
for i in people001.index:
    people001.at[i, 'ID'] = i+1
    people001.at[i, 'gender'] = 'Male' if i%2 == 0 else 'Famale'
    people001.at[i, 'birthday'] = date(startday.year+i, startday.month, startday.day)
people001.set_index('ID', inplace=True)
people001.to_excel('people2.xlsx')


people002 = pd.read_excel('people002.xlsx', index_col='ID')
def add_1000(x):
    return x+1000
people002['money'] = people002['money'] + 1000
people002['money'] = people002['money'].apply(add_1000)
people002['money'] = people002['money'].apply(lambda x:x+1000)
people002.to_excel('people3.xlsx')
