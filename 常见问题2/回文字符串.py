# -*-coding:utf-8 -*-

"""
1、使用切片方法
2、使用reversed方法
"""

a = '2abc1cba2'
b = a[::-1]
if a == b:
    print(True)
else:print(False)

c = ''.join(reversed(a))
if a == c:
    print(True)
else:print(False)


