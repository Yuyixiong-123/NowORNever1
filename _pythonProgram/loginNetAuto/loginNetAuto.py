# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:32:39 2021

@author: YUYixiong
"""

from selenium import webdriver
import time
import sys
import os
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser=webdriver.Chrome(options=options)
browser.get(r'https://gw.buaa.edu.cn')
time.sleep(2) 
a=''
try:
    browser.find_element_by_id("username").send_keys('BY2005315')
    browser.find_element_by_id("password").send_keys('54yyx52mareguli')
    browser.find_element_by_id("login").click()
    browser.close()
except:
    browser.close()
print('goodBoy')
#sys.exit()
# os._exit(0)
os.system('cmd.exe /C')