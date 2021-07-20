# -*-coding:utf-8 -*-

# 1-10的列表
print([i for i in range(1, 11) if i % 2 == 0])
# 列表的平方
a = [1, 2, 3, 4, 5]
print([i ** 2 for i in a])
# 列表大于0的数
a = [-3, 1, -2, 5, 89, -6, 2]
print([i for i in a if i > 0])
# 统计列表中的正数和负数
a = [-3, 1, -2, 5, 89, -6, 2]
print(len([i for i in a if i > 0]))
print(len([i for i in a if i < 0]))
# 删除列表中姓张的
a = ['张三', '李四', '张四', '王五']
print([i for i in a if not i.startswith('张')])


def remove_zhang(x):
    return not str(x).startswith('张')


print(list(filter(remove_zhang,a)))
print(list(filter(lambda x:not str(x).startswith('张'),a)))
