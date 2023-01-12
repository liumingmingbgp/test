import pandas as pd
people = pd.read_excel('pandas4.xlsx', index_col='ID')
print(people.isnull().any())
people.dropna(inplace=True)
# print(people)
pass_woman = people[(people['性别'] == 'F') & (people['分数'] >= 60)]
print(pass_woman)

def score_50_to_90(a):
    return 50<= a < 90
def age_20_to_30(a):
    return 20<= a < 30

mans_pass = people[people['性别'] == 'M'].loc[people['分数'].apply(score_50_to_90)].loc[people['年龄'].apply(age_20_to_30)]
print(mans_pass)
