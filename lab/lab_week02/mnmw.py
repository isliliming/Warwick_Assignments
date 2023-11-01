#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:21:32 2023

@author: liming
"""
import os
import openpyxl

# load file names
directory_path = '/Users/liming/Documents/GitHub/Warwick_Assignments/lab/lab_week02/GPC'
filenames = []  # 创建一个空列表来存储文件名

for filename in os.listdir(directory_path):
    if os.path.isfile(os.path.join(directory_path, filename)):
        filenames.append(filename)  # 将文件名添加到列表中

#print(filenames)  # 打印包含所有文件名的列表

#read data
workbook = openpyxl.load_workbook('/Users/liming/Documents/GitHub/Warwick_Assignments/lab/lab_week02/GPC/PGT_01 1.xlsx')
sheet = workbook['MW Results']

peasks = ['Mp (g/mol)', 'Mn (g/mol)', 'Mw (g/mol)', 'Mz (g/mol)', 'Mz+1 (g/mol)', 'Mv (g/mol)', 'PD']
# 查找'MW Averages'的位置
for row in sheet.iter_rows():
    for cell in row:
        if cell.value == "MW Averages":
            mw_averages_row = cell.row

# 读取'MW Averages'下的两行数据 type(header_row) list
# header_row = [cell.value for cell in sheet[mw_averages_row + 1]][1:6]
peak1 = [cell.value for cell in sheet[mw_averages_row + 2]][1:8]

