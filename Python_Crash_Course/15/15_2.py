import matplotlib.pyplot as plt

x_value = range(1, 5001)
cubes = [x**3 for x in x_value]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_value, cubes, c=cubes, cmap=plt.cm.Greens, s=10)

ax.set_title('cubes', fontsize=14)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('cube of value', fontsize=14)

ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5001, 0, 5001**3])

plt.show()