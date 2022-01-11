# -*-coding:utf-8 -*-
import pandas as pd
import os


# 读取文件，csv和xlsx一样
data = pd.read_csv("某招聘网站数据.csv",encoding='gbk')
# data1 = pd.read_excel("TOP2501.xlsx")
# data2 = pd.read_excel('../file_1/data.csv')

# 读取前20行
# print(data.head(20))
# print(data[:20])
# 读取20行之后的
# print(data[20:])
