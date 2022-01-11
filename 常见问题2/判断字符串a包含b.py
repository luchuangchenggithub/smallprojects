# -*-coding:utf-8 -*-


a = 'qqq www bbb'
b = ' www '
if b in a:
    print(True)
else:
    print(-1)

if a.find(b):
    print(True)
else:
    print(-1)

print(True if a.find(b) else -1)