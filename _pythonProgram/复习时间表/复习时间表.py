# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:09:23 2020

@author:maregul

to me, you are my perfect 
"""
import os
import time
import openpyxl

def setdate(x):
     a=str(int(time.strftime("%Y")))
     b=str(int(time.strftime("%m")))
     c=str(int(time.strftime("%d"))+x)
     
     monthday=0
     biglist=[1,3,5,7,8,10,12]
     smalllist=[4,6,9,11]
     if int(time.strftime("%m"))==4:
          monthday=28
     if int(time.strftime("%m")) in biglist:
          monthday=31
     if int(time.strftime("%m")) in smalllist:
          monthday=30
          
     
     if int(c)>monthday:
          c=str(int(c)-monthday)
          b=str(int(b)+1)
     
     day=a+'年'+b+'月'+c+'日'
     return day
     
reviewList=openpyxl.load_workbook("复习清单.xlsx")
sheet=reviewList['Sheet1']

sign=2
signCell='B'+str(sign)
test=sheet[signCell].value
while(test):
     sign+=1
     signCell='B'+str(sign)
     test=sheet[signCell].value

today=str(int(time.strftime("%Y")))+'年'+str(int(time.strftime("%m")))+'月'+str(int(time.strftime("%d")))+'日'

order=str(input())

if order=='1':#检索需要复习的内容并输出
     
     sign-=1
     signCell='H'+str(sign)
     j=1
     
     for a in sheet['C3':signCell]:
          for b in a:
               if b.value==today:
                    rownum=int(b.row)
                    contextcell='B'+str(rownum)
                    print(str(j)+'、'+str(sheet[contextcell].value))
                    j+=1
                    break
     


if order=='2':
     context=str(input())
     sheet[signCell]=(context)
     time0='C'+str(sign)
     sheet[time0]=today
     
     time1='D'+str(sign)
     time2='E'+str(sign)
     time3='F'+str(sign)
     time4='G'+str(sign)
     time5='H'+str(sign)
     

     
     sheet[time1]=setdate(1)
     sheet[time2]=setdate(2)
     sheet[time3]=setdate(4)
     sheet[time4]=setdate(7)
     sheet[time5]=setdate(15)

     reviewList.save("复习清单.xlsx")

print("加油哦!!会当凌绝顶一览众山小")

os.system("pause")
