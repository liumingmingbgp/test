from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die(6)
die_2 = Die(6)

results = []
for roll_num in range(100):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_cofig = {'title' : '结果', 'dtick': 1}
y_axis_cofig = {'title' : '结果的频率'}
my_layout = Layout(title='掷两个D6 1000次的结果', xaxis=x_axis_cofig, yaxis=y_axis_cofig)
offline.plot({'data': data, 'layout': my_layout}, filename='D6乘以D6.html')