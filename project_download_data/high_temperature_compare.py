import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename_sitka = 'sitka_weather_2014.csv'
filename_valley = 'death_valley_2014.csv'


dates_s, highs_s, dates_v, highs_v = [], [], [], []
with open(filename_sitka) as f_s:
    reader_s = csv.reader(f_s)
    header_row = next(reader_s)

    for row in reader_s:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates_s.append(current_date)

        high = int(row[1])
        highs_s.append(high)

with open(filename_valley) as f_v:
    reader_v = csv.reader(f_v)
    header_row = next(reader_v)

    for row in reader_v:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
        except ValueError:
            print(ValueError)
        else:
            dates_v.append(current_date)
            highs_v.append(high)

# 根据数据绘制图形
fig = plt.figure(figsize=(10, 6), dpi=128)
plt.plot(dates_s, highs_s, c='red', alpha=0.5)
plt.plot(dates_v, highs_v, c='blue', alpha=0.5)
# plt.fill_between(dates_s, highs_s, highs_v, facecolor='blue', alpha=0.1)

# 设置图形格式
plt.title('Daily high and low temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F', fontsize=16)
# 刻度的参数
plt.tick_params(axis='both', which='both', labelsize=16)

plt.show()
