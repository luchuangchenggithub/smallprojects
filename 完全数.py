# -*-coding:utf-8 -*-

"""
完全数：等于它本身之外的其他除数之和
如：6=3+2+1，28=14+7+4+2+1
"""

for a in range(2,1000):
    s = []
    for i in range(1, a):
        if a % i == 0:
            s.append(i)
    if sum(s) == a:
        print(a)

for b in range(2, 1000):
    if sum([i for i in range(1, b) if b % i == 0]) == b:
        print(b)
