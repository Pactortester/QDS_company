import csv
import os
import unittest


def read():

    # 获取当前文件所在路径
    path = os.path.dirname(__file__)
    path = path +'/data/'
    print(path)
    file = open(path,'r')
    table = csv.reader(file)
    return table
    # for row in table:
    #   print(row[0])



# with 这句话可保证 关闭文件 相当于file.close()


if __name__ == "__main__":
    read()