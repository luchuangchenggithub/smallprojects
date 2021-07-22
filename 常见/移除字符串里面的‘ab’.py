# -*-coding:utf-8 -*-
'''
需要循环移除
'''
a = ['aababbc','badabcab']
new_a = []
for i in a:
    while 'ab' in i:
        i = i.replace('ab','')
    new_a.append(i)
print(new_a)
