from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_cofig = {'title' : '结果'}
y_axis_cofig = {'title' : '结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果', xaxis=x_axis_cofig, yaxis=y_axis_cofig)
offline.plot({'data':data, 'layout':my_layout}, filename='D6.html')