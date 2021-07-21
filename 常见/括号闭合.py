# -*-coding:utf-8 -*-

def is_str_close(a):
    b = []
    flag = True
    for i in a:
        if i == "{" or i == "[" or i == "(":
            # 左边的括号加进去
            b.append(i)
        elif i == "}":
            # 遇到右边括号}弹出最后面的一个{
            if len(b) == 0 or b.pop() != "{":
                return False
        elif i == "]":
            # 遇到右边括号]弹出最后面的一个[
            if len(b) == 0 or b.pop() != "[":
                return False
        elif i == ")":
            # 遇到右边括号)弹出最后面的一个(
            if len(b) == 0 or b.pop() != "(":
                return False
    # 判断最后列表b里面的左边括号是否全部被弹出
    if len(b) != 0:
        flag = False
    return flag


if __name__ == '__main__':
    a = "{[{()}]()}"
    print(is_str_close(a))
    b = "({[{()}]()}"
    print(is_str_close(b))
    c = "{[{()}]()}]"
    print(is_str_close(c))
