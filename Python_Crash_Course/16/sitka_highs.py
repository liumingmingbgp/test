import csv
import matplotlib.pyplot as plt

filename = 'C:/Users/liumi/Desktop/Python/Practice/Python_Crash_Course/16/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    
    for index, col_header in enumerate(header_row):
        print(index, col_header)

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
    print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

ax.set_title('2018年7月每日最高气温', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('温度(F)', fontsize=16)
ax.tick_params(axis='both', which = 'major', labelsize=16)

plt.show()
