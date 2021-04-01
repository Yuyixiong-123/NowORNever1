# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:58:34 2021

@author:maregul

to me, you are my perfect 
"""
senList=[]
for i in range(100):
# 
# print(a)
     a=str(input("please input the para:"))
     if not (a==None or a==''):
          senList.append(a)
     else:
          break
# shell.clear()

b=[]
print('*********************************************************************************')
for i in range(len(senList)):
     print(senList[i])
     print('\n')

c=input()