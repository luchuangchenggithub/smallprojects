# -*-coding:utf-8 -*-

# def fun():
#     temp = [lambda x:i*x for i in range(4)]
#     # 返回的是一个函数，4次
#     return temp

def fun():
    temp = []
    for i in range(4):
        def inner(x):
            return i * x

        temp.append(inner)
    return temp


for everyLambda in fun():
    print(everyLambda(2))
