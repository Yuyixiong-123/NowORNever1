# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:22:45 2021

@author: YU Yixiong
"""

from aip import AipOcr
APP_ID='老老实实抱着我'
API_KEY='517d60b47eed4ebfa794dcf667f5eec3'
SECRET_KEY='e054e6b427d0468296e3436893c5e25b'
client=AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
def image2text(fileName):
    image = get_file_content(fileName)
    dic_result = client.basicGeneral(image)
    res = dic_result['words_result']
    result = ''
    r=1
    for m in res:
        # print(str(m['words']))
        result = result + str(m['words'])+"\n"
    return result

print(image2text("C:/Users/YU Yixiong/Desktop/1.png"))
# with open("C:/Users/YU Yixiong/Desktop/1.txt","a+") as f:
#     for i in range(2,12):
#         result=image2text("C:/Users/YU Yixiong/Desktop/新建文件夹/"+str(i)+".png")
#         f.write("\n"+str(i)+"\n"+result)
#     f.close()
    
    