# -*-coding:utf-8 -*-
"""
100-1000的水仙花
"""

for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
print('----------')
for i in range(100, 1000):
    if i == sum([int(j) ** 3 for j in str(i)]):
        print(i)
