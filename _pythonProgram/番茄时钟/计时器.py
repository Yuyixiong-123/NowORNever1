# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:52:36 2020

@author:maregul

to me, you are my perfect 
"""

import pygame
import time

timecounter=0
mint=0
print('start')
while(timecounter<60*5*5):
     filepath = r"C:\Users\YuYX\Desktop\腰背挺直1.mp3";
     pygame.mixer.init()
     pygame.mixer.music.load(filepath)
     pygame.mixer.music.play(start=0.0)
     time.sleep(5)
     pygame.mixer.music.stop()
     for i in range(5):
          print(mint)
          time.sleep(60)
          mint+=1         
     timecounter+=300

filepath = r"C:\Users\YuYX\Desktop\赶紧休息.mp3";
pygame.mixer.init()
pygame.mixer.music.load(filepath)
pygame.mixer.music.play(start=0.0)
time.sleep(8)
pygame.mixer.music.stop()

