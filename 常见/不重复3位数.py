# -*-coding:utf-8 -*-

# 方法1
a = [1, 2, 3, 4]
s = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                s += 1
print(s)

# 方法2
from itertools import permutations

# for i,j,k in permutations(a,3):
#     print(i,j,k)
print(len(list(permutations(a, 3))))
