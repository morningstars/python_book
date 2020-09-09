from die import Die

import pygal

die = Die()

results = []

# 掷单个骰子
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)


# 分析结果

frequencies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 绘制直方图

hist = pygal.Bar()

hist.title = "Results of rolling ond D6 1000 times"

hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')
