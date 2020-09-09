import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1000))
y_values = [x ** 2 for x in x_values]

# plt.scatter(2, 4, s=20)
# plt.scatter(x_values, y_values, edgecolors='none', s=40, c='red')
# plt.scatter(x_values, y_values, edgecolors='none', s=40, c=(0, 0, 0.8))

# 颜色映射 c和cmap
plt.scatter(x_values, y_values, edgecolors='none', s=40, c=y_values, cmap=plt.cm.Reds)

plt.title("Square Numbers", fontsize=15)
plt.xlabel("Value", fontsize=15)
plt.ylabel("Square of Value", fontsize=15)

plt.tick_params(axis='both', which='major', labelsize=15)

plt.axis([0, 1100, 0, 1100000])

# plt.show()

# 第二个参数表示将周围的空白裁剪掉 可省略
plt.savefig('square_plot.png', bbox_inches='tight')
