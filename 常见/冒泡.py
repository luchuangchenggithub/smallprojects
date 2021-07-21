# -*-coding:utf-8 -*-
a = [11,2,33,1,5,88,3]
n = len(a)
for j in range(n-1,0,-1):
    for i in range(0,j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    print(a)
print(a)