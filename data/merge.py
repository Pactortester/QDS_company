# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 15:56
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: test.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

fa = open('驰名商标.txt')
a = fa.readlines()
fa.close()
fb = open('著名商标.txt')
b = fb.readlines()
fb.close()
fc = open('地理标志商标.txt')
c = fc.readlines()
fc.close()
d = [i for i in a if i in b if i in c]
fd = open('驰著名地理商标.txt', 'w')
fd.writelines(d)
fd.close()