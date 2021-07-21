# -*-coding:utf-8 -*-
'''
返回的是一个相同的数字
如22252
一个字符，5次
两个字符，2次
3个字符，1次
4个字符，0
5个字符，0
'''
a = '22252'

b = []
for i in range(1,len(a)+1):
    for j in range(len(a)):
        new_a = a[j:j+i]
        if new_a.count(new_a[0])==i:
            b.append(new_a)
print(b)