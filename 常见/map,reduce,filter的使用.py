# -*-coding:utf-8 -*-
from functools import reduce

'''
1、计算1-100的和 
2、1-10每个数的平方
3、[a,ab,abc,bc,cd]输出含有c的元素
'''
print(reduce(lambda x,y:x+y,range(1,100)))
print(list(map(lambda x:x**2,range(1,11))))
a = ['a','ab','abc','bc','cd']
print(list(filter(lambda x:'c' in x,a)))