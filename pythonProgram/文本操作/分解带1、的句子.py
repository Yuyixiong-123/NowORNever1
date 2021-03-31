# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:13:45 2021

@author:maregul

to me, you are my perfect 
"""
def find(s):
     h=0
     for i in range(len(s)):
          if s[i]==".":
               h=i
               break
     return h
a=[]
while(True):
     b=str(input('come:')) 
     if b == '1':
          break
     if b!='':
          a.append(b[find(b)+1:])

print(a)
for i in a:
     print("\""+i+"\",")
b=input()
