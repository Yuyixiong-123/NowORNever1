# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:08:14 2021

@author: YU Yixiong
"""

# encoding:utf-8

# import requests 
import requests
import base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=zCLERFdytz8bn38mPrM9ceWs&client_secret=ESFdhhG7dO9QkyeFvSOQDtbK2tsX28Il'
response = requests.get(host)
# if response:
#     print(response.json())

'''
通用文字识别（高精度版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('C:/Users/YU Yixiong/Desktop/pic/ (1).png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = response.json()['access_token']
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json()['words_result'][0]['words'])