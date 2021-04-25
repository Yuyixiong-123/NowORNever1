# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:38:50 2021

@author: YU Yixiong
"""

from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options) 
engPara="Not the answer you're looking for? Browse other questions tagged python unicode encode or ask your own question. "
browser.get(r'https://www.deepl.com/translator#en/zh/'+engPara)
print('sleep')
time.sleep(5)
print('wake up')
fs=(browser.page_source)
# fs='                        <div class="lmt__translations_as_text" dl-test="translator-target-result-as-text-container" style="font-size: 20px;"><p class="lmt__translations_as_text__item lmt__translations_as_text__main_translation" dl-test="translator-target-result-as-text-entry"><button class="lmt__translations_as_text__text_btn">你必须使用Visual Studio来在windows上建立一个Python扩展。 如果你得到这个错误，说明你还没有安装Visual C++。 请注意，Visual Studio有很多种类，比如用于C语言开发的Visual Studio。 你需要安装Visual Studio for C++。</button><button class="lmt__translations_as_text__copy_button"></button></p></div>'
regex=re.compile('lmt__translations_as_text__text_btn">(.*)</button><button class="lmt')
x=regex.findall(fs)
browser.close()
# with open("1.txt",'w',encoding='utf-8') as f:
#     f.write(browser.page_source)
# browser.execute_script('alert("To bottom")')