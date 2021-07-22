# -*-coding:utf-8 -*-
from copy import copy,deepcopy
# 不可变 int str tuple
# 可变 list set dict
li = [1,2,[3,4]]
x = li[:]
a = copy(li)
b = deepcopy(li)
c = li
li[0]=8
li[2][0]=6
print(li)
print(x)
print(a)
print(b)