# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:24:54 2021

@author: YU Yixiong
"""
import requests
import base64
import time
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=UEoyx1rz1AaomIBnfkT0bVCM&client_secret=95bWpv3mGjvswdRPl3q0L4iZewMwZjBi'
response = requests.get(host)
access_token = response.json()['access_token']

'''
人脸注册
'''
def register(fp,group_id,user_id):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    f = open(fp, 'rb')
    img = base64.b64encode(f.read())
    
    # notice to use utf-8 to standarlize the str
    # set the parameter "liveness_control" to lower the restriction
    params = "{\"image\":\""+str(img, 'utf-8') +"\",\"image_type\":\"BASE64\",\"group_id\":\""+group_id+"\",\"user_id\":\""+user_id+"\",\"user_info\":\"abc\",\"quality_control\":\"LOW\",\"liveness_control\":\"NORMAL\",\"liveness_control\":\"NONE\"}"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())

# =============================================================================
# for i in range(2,21):
#     register("C:/Users/YU Yixiong/Desktop/faces94/male/9326871/9326871.%i.jpg"%(i), 'test', '9326871')
#     time.sleep(2)
# =============================================================================

def checkInfo(group_id,user_id):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/get"

    params = "{\"user_id\":\""+user_id+"\",\"group_id\":\""+group_id+"\"}"
    access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())

checkInfo('test', '9326871')
# request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

# params = "{\"image\":\"C:/Users/YU Yixiong/Desktop/pe.jpg\",\"image_type\":\"FACE_TOKEN\",\"face_field\":\"faceshape,facetype\"}"
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/json'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())