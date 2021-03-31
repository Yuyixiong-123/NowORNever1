# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:54:50 2021

@author:maregul

to me, you are my perfect 
"""
# 配置以下模块
import requests 
import re
import os
import time

# 1.运行 py源文件
# 2.输入你想搜索的关键词，比如“柯基”、“泰迪”等
# 3.输入你想下载的页数，比如5，那就是下载 5 x 60=300 张图片

# 在学习过程中有什么不懂得可以加我的
# python学习扣扣qun，784758214
# 群里有不错的学习视频教程、开发工具与电子书籍。
# 与你分享python企业当下人才需求及怎么从零基础学习好python，和学习什么内容
# 获取图片url连接
def get_parse_page(pn,name):

    for i in range(int(pn)):
        # 1.获取网页
        print('正在获取第{}页'.format(i+1))

        # 百度图片首页的url
        # name是你要搜索的关键词
        # pn是你想下载的页数

        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d' %(name,i*20)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}

        # 发送请求，获取相应
        response = requests.get(url, headers=headers)
        html = response.content.decode()
        # print(html)

        # 2.正则表达式解析网页
        # "objURL":"http://n.sinaimg.cn/sports/transform/20170406/dHEk-fycxmks5842687.jpg"
        results = re.findall('"objURL":"(.*?)",', html) # 返回一个列表

        # 根据获取到的图片链接，把图片保存到本地
        save_to_txt(results, name, i)

def save_to_txt(results, name, i):

    j = 0
    # 在当目录下创建文件夹
    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    # 下载图片
    for result in results:
        print('正在保存第{}个'.format(j))
        try:
            pic = requests.get(result, timeout=10)
            time.sleep(1)
        except:
            print('当前图片无法下载')
            j += 1
            continue

        # 可忽略，这段代码有bug
        # file_name = result.split('/')
        # file_name = file_name[len(file_name) - 1]
        # print(file_name)
        #
        # end = re.search('(.png|.jpg|.jpeg|.gif)$', file_name)
        # if end == None:
        #     file_name = file_name + '.jpg'

        # 把图片保存到文件夹
        file_full_name = './' + name + '/' + str(i) + '-' + str(j) + '.jpg'
        with open(file_full_name,'wb') as f:
            f.write(pic.content)

        j += 1

# 核心代码：
# pic = requests.get(result, timeout=10)
# f.write(pic.content)

# **3.主函数代码：**

# 主函数
if __name__ == '__main__':

    name = input('请输入你要下载的关键词：')
    pn = input('你想下载前几页（1页有60张）:')
    get_parse_page(pn, name)


