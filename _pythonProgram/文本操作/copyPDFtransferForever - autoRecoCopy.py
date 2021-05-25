# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:29:54 2021

@author:maregul

to me, you are my perfect 
https://blog.csdn.net/nanbei2463776506/article/details/82967140

"""
import pyperclip
def E_trans_to_C(string):
    E_pun = u',.!?[]()<>"\''
    C_pun = u'，。！？【】（）《》“‘'
    table= {ord(f):ord(t) for f,t in zip(E_pun,C_pun)}
    return string.translate(table)
stop=False
while(stop==False):
    pyperclip.waitForNewPaste() 
    a=pyperclip.paste()
    a.replace(" ", '')
    a.replace('\n', '')
    a.replace("\r", '')
    ca=E_trans_to_C(a)
    print("********************************************************************")
    print(ca)
    pyperclip.copy(ca)
    print("********************************************************************")
