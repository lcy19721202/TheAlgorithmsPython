import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.font_manager import FontProperties
from typing import List, Tuple
import os

# 设置中文字体，兼容Windows和Mac OS X
if os.name == 'nt':
    font_path = r"c:\windows\fonts\simsun.ttc"
else:
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
try:
    font = FontProperties(fname=font_path, size=12)
except Exception:
    print("警告：未找到指定字体，将使用系统默认字体")
    font = FontProperties(size=12)

# 数据来源：基于2015-2024年北京市高考期间（6月7日-10日）历史天气数据
# 数据经过处理：四日最高温度取最大值，湿度和降水概率取平均值
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]  # 添加2025年
max_temps = [33.5, 34.2, 32.8, 33.7, 34.0, 31.5, 32.3, 29.0, 35.5, 28.0, 31.0]  # 预测2025年最高温度
avg_humidities = [68, 65, 70, 63, 66, 72, 69, 75, 60, 78, 70]  # 预测2025年平均湿度
avg_precip_prob = [45, 30, 25, 35, 40, 55, 45, 60, 30, 70, 50]  # 预测2025年降水概率

# 创建图形和第一个Y轴
fig, ax1 = plt.subplots(figsize=(14, 8))  # 增加图表尺寸

# 添加网格线
ax1.grid(True, linestyle='--', alpha=0.7)

# 绘制四日最高温度折线图（红色）
color = 'tab:red'
ax1.set_xlabel('年份', fontproperties=font)
ax1.set_ylabel('最高温度℃', fontproperties=font, color=color)
# 历史数据用实线
line1 = ax1.plot(years[:-1], max_temps[:-1], color=color, marker='o', label='最高温度℃', linewidth=2)
# 预测数据用虚线
ax1.plot([years[-2], years[-1]], [max_temps[-2], max_temps[-1]], color=color, linestyle='--', marker='o', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))

# 设置X轴刻度
ax1.set_xticks(years)
ax1.set_xticklabels([str(year) for year in years], fontproperties=font)

# 添加温度数据标注
for x, y in zip(years, max_temps):
    ax1.annotate(f'{y}℃', (x, y), textcoords="offset points", xytext=(0,10), 
                ha='center', fontproperties=font, color=color, fontsize=8)

# 创建第二个Y轴（湿度，蓝色）
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('平均湿度% / 平均降水概率%', fontproperties=font, color=color)
# 历史数据用实线
line2 = ax2.plot(years[:-1], avg_humidities[:-1], color=color, marker='s', label='平均湿度%', linewidth=2)
# 预测数据用虚线
ax2.plot([years[-2], years[-1]], [avg_humidities[-2], avg_humidities[-1]], color=color, linestyle='--', marker='s', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.set_ylim(0, 100)  # 设置湿度Y轴范围

# 添加湿度数据标注
for x, y in zip(years, avg_humidities):
    ax2.annotate(f'{y}%', (x, y), textcoords="offset points", xytext=(0,-15), 
                ha='center', fontproperties=font, color=color, fontsize=8)

# 在同一个Y轴上绘制降水概率（绿色）
color = 'tab:green'
# 历史数据用实线
line3 = ax2.plot(years[:-1], avg_precip_prob[:-1], color=color, marker='^', label='平均降水概率%', linewidth=2)
# 预测数据用虚线
ax2.plot([years[-2], years[-1]], [avg_precip_prob[-2], avg_precip_prob[-1]], color=color, linestyle='--', marker='^', linewidth=2)

# 添加降水概率数据标注
for x, y in zip(years, avg_precip_prob):
    ax2.annotate(f'{y}%', (x, y), textcoords="offset points", xytext=(0,10), 
                ha='center', fontproperties=font, color=color, fontsize=8)

# 添加标题和图例
plt.title('2015-2024年北京高考期间天气情况变化趋势及2025年预测', fontproperties=font, pad=20, fontsize=14)

# 调整图例位置到底部
legend_lines = [line1[0], line2[0], line3[0]]
legend_labels = ['最高温度℃', '平均湿度%', '平均降水概率%']
ax1.legend(legend_lines, legend_labels, loc='upper center', prop=font, bbox_to_anchor=(0.5, -0.1), ncol=3)

# 在图例下方添加说明文字
plt.figtext(0.5, 0.07, '（高考通常安排在每年的6月7日~6月10日的四天中）', 
            ha='center', fontproperties=font, fontsize=10)

# 调整图表边距，确保图例和说明文字可见
plt.subplots_adjust(bottom=0.25)

# 显示图表
plt.show()
