# -*-coding:utf-8 -*-
import os


def print_directory_contents(sPath):
    """
    :param sPath:接受文件夹的名称
    :return:该文件夹中文件的路径，以及其包含文件夹中文件的路径
    """
    for file_name in os.listdir(sPath):
        # 拼接路径
        child = os.path.join(sPath, file_name)
        # 判断是否文件
        if os.path.isfile(child):
            print(f'文件:{child}')
        else:
            print(f'文件夹:{child}')
            print_directory_contents(child)


if __name__ == '__main__':
    path = r'C:\Users\admin\Desktop\安装包'
    print_directory_contents(path)
