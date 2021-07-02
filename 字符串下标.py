# -*-coding:utf-8 -*-

a = 'hello welcome to the world'

if 'welcome' in a:
    print(a.index('welcome'))
else:
    print('-1')

print(a.index('welcome') if 'welcome' in a else -1)

# 起始位置
print(a.index('e',5,10))