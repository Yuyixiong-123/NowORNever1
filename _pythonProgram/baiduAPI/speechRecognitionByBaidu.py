# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:26:15 2021

@author: YU Yixiong
"""

from aip import AipSpeech

APP_ID='24109623'
API_KEY='3VA6as1deWqQYo8kzB85INnP'
SECRET_KEY='sy9qFiWG1qDEcdLOS2Au5FfF693CGkGj '
# API_KEY='517d60b47eed4ebfa794dcf667f5eec3'
# SECRET_KEY='e054e6b427d0468296e3436893c5e25b'
client=AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
filePath='C:/Users/YU Yixiong/Desktop/5月1日 上午11点01分停车20.aac'
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
result=client.asr(get_file_content(filePath), 'aac', 16000, {
    'dev_pid': 1537,
})

print(result)