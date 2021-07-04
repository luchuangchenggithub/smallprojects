# -*- coding: UTF-8 -*-

num = 100
a = 0
b = 1
n = 1
s = []
while n <= 100:
    n = a + b
    a, b = b, n
    if n >= 100:
        break
    s.append(n)
print(s)
