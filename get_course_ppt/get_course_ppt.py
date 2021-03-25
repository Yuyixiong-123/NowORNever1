# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:04:14 2021

@author: YU Yixiong
"""

# -*- coding: utf-8 -*-  
import urllib    
import urllib2  
import cookielib
from pyquery import PyQuery as pq
import sys
import ConfigParser
import os
import StringIO
import codecs
# 防止出现编码错误
reload(sys)
sys.setdefaultencoding( "utf-8" )


if __name__ == '__main__':
    config_file = 'config.txt'
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    cf = ConfigParser.ConfigParser()



    cf.read(config_file)
    stu_id = cf.get('student_info', 'id')
    stu_pw = cf.get('student_info', 'password')
    course_name = unicode(cf.get('course_info', 'course_name'),'utf-8')
    course_url = cf.get('course_info', 'course_url')
    user_agent = u'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    header = { 'User-Agent' : user_agent }

    # cookie
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    # 打开VPN
    req = urllib2.Request(
        url = 'https://e.buaa.edu.cn/users/sign_in',
        headers = header
    )

    # 通过pyquery获取表单信息，填写账号密码登录
    result = opener.open(req).read()
    p = pq(result)
    postdata = {}
    inputs = p('form').find('input')
    for i in range(len(inputs)):
        key = inputs.eq(i).attr('name')
        value = inputs.eq(i).attr('value')
        postdata[key] = value
    postdata['user[login]']=stu_id
    postdata['user[password]']=stu_pw

    postdata=urllib.urlencode(postdata)

    req = urllib2.Request(
        url = 'https://e.buaa.edu.cn/users/sign_in',
        data = postdata,
        headers = header
    )
    result = opener.open(req).read()
    print 'Sign into VPN.'

    # 登录课程中心
    postdata = {}
    postdata['eid']=stu_id
    postdata['pw']=stu_pw
    postdata['type']='ldap'

    postdata=urllib.urlencode(postdata)
    req = urllib2.Request(
        url = 'https://course.e.buaa.edu.cn/opencourse/login',
        headers = header,
        data = postdata
    )

    result = opener.open(req).read()
    req = urllib2.Request(
        url = course_url,
        headers = header
    )


    result = opener.open(req).read()
    print 'Sign to course center.'
    p = pq(result)
    a_s = p('.dataGrid').eq(0).find('a')
    urls = {}
    for i in range(len(a_s)):
        url = a_s.eq(i).attr('href')
        filename = a_s.eq(i).text()
        urls[filename] = url


    os.makedirs(course_name)
    for filename in urls:
        print 'Downloading ', filename, '...'
        savefile = open(course_name + '/' + filename,'wb')
        try:
        	savefile.write(opener.open(urls[filename]).read())
        	savefile.close()
        except:  
    		print urls[filename]