# -*-coding:utf-8 -*-

a = 'sdfsasddiqwoxckqwe'

s1 = []
for i in a:
    if i not in s1:
        s1.append(i)
print(''.join(sorted(s1)))


s2 = set(a)
print(''.join(sorted(s2,reverse=True)))
# 去重后保留顺序
s2 = set(a)
print(''.join(sorted(s2,key=lambda x:a.index(x))))





