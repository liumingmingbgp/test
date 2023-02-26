import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

student = pd.read_excel('pandas8.xlsx')
name = '名称'
score = '分数'
age = '年龄'
myfont = FontProperties(fname='C:\Windows\Fonts\SimHei.ttf')  # 字体路径使用绝对路径
plt.rcParams['font.sans-serif']=['SimHei']   # 指定默认字体

### 绘制柱状图 ###
plt.bar(student[name], student[score], color = 'orange')
plt.title('学生分数', fontproperties=myfont, fontsize = 16)
plt.xlabel(name, fontproperties=myfont)
plt.ylabel(score, fontproperties=myfont)
plt.xticks(student[name], rotation = '90')
plt.tight_layout()
plt.show()

### 绘制折线图 ###
student.plot(y=[score, age])
plt.title('学生分数', fontproperties=myfont, fontsize=16, fontweight ='bold')
plt.xticks(student.index)
plt.show()

### 绘制散点图 ###
student.plot.scatter(x=name, y=score)
plt.title('学生分数', fontsize=16, fontweight='bold')
plt.xlabel(name)
plt.xticks(student[name], rotation = '90')
plt.ylabel(score)
plt.tight_layout()
plt.show()