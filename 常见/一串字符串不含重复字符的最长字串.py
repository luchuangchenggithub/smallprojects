# -*-coding:utf-8 -*-

a = 'pwwkew'
b = []
for i in range(1, len(a) + 1):
    s = []
    for j in range(len(a) - i + 1):  # 要减去i不然最后一个字符串不合法
        new_a = a[j:j + i]
        if len(new_a) == len(set(new_a)):
            b.append(new_a)
print(len(max(b,key=lambda x:len(x))))
