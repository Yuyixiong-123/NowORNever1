# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:41:24 2020

@author:maregul

to me, you are my perfect 
"""
import os
shici=open("苏轼诗词集.txt",'r',encoding='UTF-8')
shicilist=shici.readlines()
shici.close()
outputlist=[0]
for i in range(1,50):
     if shicilist[i][0]=='词':
          break
     else:
          outputlist.append(i)
for x in outputlist:
     print(shicilist[x])

for x in range(outputlist[-1],-1,-1):
     shicilist.remove(shicilist[x])

shici=open("苏轼诗词集.txt",'w',encoding='UTF-8')
shici.writelines(shicilist)
shici.close()

os.system("pause")
