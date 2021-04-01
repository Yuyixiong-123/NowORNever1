import pygame
import time
while(1): 
    n=str(input())
    if n !='q':
        filepath = r"C:\Users\YuYX\Desktop\嗯嗯.mp3";
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(start=0.0)
        time.sleep(2)
    else:
        print("happy class! good byb")
        break
