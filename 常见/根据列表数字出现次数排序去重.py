# -*-coding:utf-8 -*-

a = [1, 2, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 6]
print(sorted(set(a),key=lambda x:a.count(x),reverse=True))

b = [(i,a.count(i)) for i in set(a)]
b.sort(key=lambda x:x[1],reverse=True)
print(list(map(lambda x:x[0],b)))
