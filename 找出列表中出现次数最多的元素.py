# -*- coding: UTF-8 -*-
from collections import Counter

a = ['my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I', 'need', 'skills', 'more', 'my', 'ability', 'are', 'so',
     'poor']
# a = ['my','poor','poor', 'my','a','a']

# dict1 = {}
# for i in a:
#     # print(a.count(i))
#     if i not in dict1.keys():
#         dict1[i] = a.count(i)
# print(dict1)
# print(list(dict1.items()))
# print(sorted((list(dict1.items())), key=lambda x: x[1])[-1])
# print(dict1)
dict1 = dict(Counter(a))
b = sorted((list(dict1.items())), key=lambda x: x[1],reverse=True)
print(b)
keyword = [b[0][0]]
for i in range(1,len(b)):
    if b[i][1] != b[0][1]:
        break
    keyword.append(b[i][0])
print(keyword)
# 有BUG，当次数最多的元素有多个时
print(max(a, key=lambda x: a.count(x)))
