import pandas as pd
import matplotlib.pyplot as plt

student = pd.read_excel('student_score.xlsx')
student.sort_values(by='SCORE', inplace=True, ascending=False)
plt.bar(student['NAME'], student['SCORE'], color='orange')
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('学生分数', fontsize=16)
plt.xlabel('姓名')
plt.xticks(student.NAME, rotation='90')
plt.ylabel('分数')
plt.tight_layout()
plt.savefig('student_score.png')

print('原始下标：', student['NAME'][0])
print('绝对位置：', student.iloc[0,:]['NAME'])  # 通过iloc方法获取绝对位置
student.reset_index(drop=True, inplace=True)
print('重新排列后的下标:', student['NAME'][0])