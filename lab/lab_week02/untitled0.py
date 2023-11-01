#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 20:50:15 2023

@author: liming
"""

#import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#read date
datepath = '/Users/liming/Documents/GitHub/Warwick_Assignments/lab/lab_week02/GPCallinone.xlsx'
#workbook = openpyxl.load_workbook('/Users/liming/Documents/GitHub/Warwick_Assignments/lab/lab_week02/GPCallinone.xlsx')
#sheet = workbook['Sheet1']
df = pd.read_excel(datepath)
# x = df['s/m'].head(4)
# y = df['1/DPn'].head(4)
# y_m = df["1/DPN'"].head(4)
x = df['s/m'][4:13]
y = df['1/DPn'][4:13]
y_m = df["1/DPN'"][4:13]
# 绘制点图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Mayo')
plt.scatter(x, y_m, color='black', label="Modified Mayo")

# 一次方程拟合
m, b = np.polyfit(x, y, 1)
m_m, b_m = np.polyfit(x, y_m, 1)
x_fit = np.linspace(0, x.max(), 100)  # 生成拟合直线的x值
plt.plot(x_fit, m*x_fit + b, color='red',label='Mayo')
plt.plot(x_fit, m_m*x_fit + b_m, color='green',label='Modified Mayo')

# 计算线性相关系数
corr_coef = np.corrcoef(x, y)[0, 1]
corr_coef_m = np.corrcoef(x, y_m)[0, 1]

# 在图中添加文字说明
plt.text(0.15, 0.85, f'Mayo:y = {m:.4f}x + {b:.4f}\nR = {corr_coef:.4f}', fontsize=18, va='top', ha='left', transform=plt.gcf().transFigure)
plt.text(0.15, 0.70, f'Modified Mayo:y = {m_m:.4f}x + {b_m:.4f}\nR = {corr_coef_m:.4f}', fontsize=18, va='top', ha='left', transform=plt.gcf().transFigure)
# 在直线旁边添加"Mayo plot"标注
# x_text = 0.5 * x.max()
# y_text = m * x_text + b
# plt.text(x_text, y_text, 'Mayo plot', fontsize=18, va='bottom', ha='left')

plt.legend(loc = 'lower right',fontsize='small', frameon=False)



# 设置坐标轴标签和标题
plt.xlabel(r'$\frac{[S]}{[M]}$', fontsize=18)
plt.ylabel(r'$\frac{1}{DP_n}$', fontsize=18)


# 设置坐标轴范围
plt.xlim(left=0)
plt.ylim(bottom=0)

# 设置x轴刻度格式
def format_func_x(value, tick_number):
    return "0" if value == 0 else f"{value:.4f}"
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_func_x))

# 设置y轴刻度格式
def format_func_y(value, tick_number):
    return "0" if value == 0 else f"{value:.4f}"
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_func_y))

# save
#plt.savefig('Styrene.jpg', dpi=300)
#plt.savefig('mma.jpg', dpi=300)
# 显示图表
plt.show()






