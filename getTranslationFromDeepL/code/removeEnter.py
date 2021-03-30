# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:55:27 2021

@author: yixiong YU

note: 
"""

alist=[]
ss=True
while(ss):
     alist.clear()
     print("*********************************************************")
     while(True):
          a=input()
          if a == "s":
               print("***********************************************")
               break
          if a == 'ss':
               ss=False
          alist.append(a.replace("\n", ""))
          
     print(' '.join(alist))
     