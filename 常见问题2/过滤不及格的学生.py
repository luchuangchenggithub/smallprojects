# -*- coding: UTF-8 -*-

a = [
    {"name": "张三", "score": 66},
    {"name": "李四", "score": 12},
    {"name": "王五", "score": 88},
    {"name": "陈六", "score": 50},
    {"name": "李二", "score": 70},
]

print(list(i for i in a if i.get('score') > 60))
print(list(filter(lambda x: x.get('score') > 60, a)))
