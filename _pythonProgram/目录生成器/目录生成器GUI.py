# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:51:57 2020

@author:maregul

to me, you are my perfect 
"""

from os import listdir
import tkinter as tk
root=tk.Tk()
root.title("目录生成器")
root.geometry('500x600')
e=tk.Entry(root,width=40,textvariable=u"请输入文件夹路径" ,show = True)
e.grid(row=0, column=0)
e.pack()

def getad():
     adress=str(e.get())
     ylist=[]
     list1=listdir(adress)
     for x in list1:
          y=x.split(".")
          ylist.append(y[0])
     ylist.sort()
     for item in ylist:
          item2=item+"\n"
          text.insert(0.0,item2)
               
    
b=tk.Button(root,text="生成目录",command=getad)
b.pack()
text=tk.Text(root, height=60)
text.pack()
root.mainloop()