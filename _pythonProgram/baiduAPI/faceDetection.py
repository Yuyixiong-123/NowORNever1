# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:24:54 2021

@author: YU Yixiong
"""
import requests
import base64
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=UEoyx1rz1AaomIBnfkT0bVCM&client_secret=95bWpv3mGjvswdRPl3q0L4iZewMwZjBi'
response = requests.get(host)
access_token = response.json()['access_token']

'''
人脸注册
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
f = open('D:/labWork/NowORNever1/_pythonProgram/baiduAPI/dobrik-people.jpg', 'rb')
img = base64.b64encode(f.read())

# notice to use utf-8 to standarlize the str
# set the parameter "liveness_control" to lower the restriction
params = "{\"image\":\""+str(img, 'utf-8') +"\",\"image_type\":\"BASE64\",\"group_id\":\"test\",\"user_id\":\"test\",\"user_info\":\"abc\",\"quality_control\":\"LOW\",\"liveness_control\":\"NORMAL\",\"liveness_control\":\"NONE\"}"
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
    
# request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

# params = "{\"image\":\"C:/Users/YU Yixiong/Desktop/pe.jpg\",\"image_type\":\"FACE_TOKEN\",\"face_field\":\"faceshape,facetype\"}"
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/json'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())