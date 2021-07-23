# -*-coding:utf-8 -*-

a = 'abcabadcsabbauyiiyu'
b = []
for i in range(2, len(a) + 1):
    s = []
    for j in range(len(a) - i + 1):  # 要减去i不然最后一个字符串不合法
        new_a = a[j:j + i]
        if new_a == new_a[::-1]:
            b.append(new_a)
print(f'回文子串共有：{b},{len(b)}个')
