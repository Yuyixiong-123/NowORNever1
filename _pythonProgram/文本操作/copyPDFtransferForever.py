# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:29:54 2021

@author:maregul

to me, you are my perfect 
https://blog.csdn.net/nanbei2463776506/article/details/82967140

"""
def E_trans_to_C(string):
    E_pun = u',.!?[]()<>"\''
    C_pun = u'，。！？【】（）《》“‘'
    table= {ord(f):ord(t) for f,t in zip(E_pun,C_pun)}
    return string.translate(table)
stop=False
while(stop==False):
    a=''
    for i in range(100):
         s=str(input('getMeCome:'))
         if s=='q':
             stop=True
             break
         if not s=='':
              s=s.strip()
              a=a+s
         else:
              break
    # for i in range(len(a)):
    a.replace(" ", '')
    a.replace('\n', '')
    a.replace("\r", '')
    ca=E_trans_to_C(a)
    print("********************************************************************")
    print(ca)
    print("********************************************************************")
