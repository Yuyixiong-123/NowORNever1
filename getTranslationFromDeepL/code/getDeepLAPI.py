# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:41:09 2021

@author: YU Yixiong
"""

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip


def getTranFromDeepL(engPara):
    browser = webdriver.Chrome()
    
    # engPara="As a function of the type of target being tracked and the selected messagegeneration options for the Intel CAC, intelligence reports are generated to perform a variety of functions on the battlefield. These reports can be used as a source of targeting information for attack operations by both surface-to-surface tactical missiles and attack aircraft loaded with air-to-surface weapons. This targeting information supports both initial detection of potential targets as well as Battle Damage Assessment (BDA) of attacked targets. Reports on the potential target locations are either a result of surveillance of the specific ground target or a launch point prediction based on detection of a ballistic missile. These reports can also be used to provide sensor cueing and intelligence-based target prioritization based on detection of both missiles and aircraft."
    browser.get(r'https://www.deepl.com/translator#en/zh/'+engPara)
    
    time.sleep(6) 
    browser.find_element_by_class_name("lmt__target_toolbar__copy").click()
    # time.sleep(1) 
    
    print(0)
    print(pyperclip.paste())
    print(1)
    # time.sleep(1) 
    browser.close()

chPara=getTranFromDeepL("When an Intel CAC receives a track message that is marked as an intel message, then the message is immediately processed and an intelligence report is generated with no checks on the number of sources, updates, time-interval criteria, or correlation probability. The message is delayed by the amount of time specified on the Track Data Message Processing Time field on the Communication Options window of the Intelligence Center ruleset window.")
