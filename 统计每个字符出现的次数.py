# -*-coding:utf-8 -*-
from collections import Counter
"""
找到第二个只出现1次的字符
利用collecions中的Counter
"""
a ='asfxmsjlkfglkgjddfqwer'
b = Counter(a)
print(b)
m = 2
n = 1
s = []
for i,j in dict(b).items():
    if j ==n:
        s.append(i)
print(s[m-1])

s1 = [i for i,j in dict(b).items() if j==n]
print(s1[m-1])

a = ['my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I', 'need', 'skills', 'more', 'my', 'ability', 'are', 'so',
     'poor']
b = Counter(a)
print(dict(b))