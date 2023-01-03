import calendar
calendar.setfirstweekday(firstweekday=6)
year = 2020
# print(calendar.monthcalendar(2023,1))
for i in range(1, 13):
    for j in range(len(calendar.monthcalendar(year, i))):
        for k in range(len(calendar.monthcalendar(year, i)[j])):
            value = calendar.monthcalendar(year, i)[j][k]
            