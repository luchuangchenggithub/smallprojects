# -*- coding: UTF-8 -*-
"""
33333 = 3*10**4+3*10**3+3*10**2+3*10**1+3*10**0
"""

s = 0
n = 5
a = 3
next_a = 0

for i in range(n):
    next_a += a * 10 ** i
    print(next_a)
    s += next_a
print(s)
