# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:41:26 2021

@author:maregul

to me, you are my perfect 
"""

import os
import os.path
rootdir = r"D:\博士学习文件\20 计算机\test\晚间流程提醒\bin\Debug\photo/" #末尾斜杠不要丢
files = os.listdir(rootdir)
b=1
for name in files:
    a=os.path.splitext(name)
    print(a[0])
    newname = str(b)+'.jpg'
    b = b + 1
    os.rename(rootdir+name,rootdir+newname)
    

