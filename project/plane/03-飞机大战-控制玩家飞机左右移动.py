#-*- coding:utf-8 -*-
# pip install pygame
import pygame
import time

def main():

    screen = pygame.display.set_mode((480,852),0,32)


    backgroud = pygame.image.load("./feiji/background.png")

    #3. 创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")

    x = 210
    y = 700

    while True:
        screen.blit(backgroud,(0,0))

        screen.blit(hero,(x,y))
        pygame.display.update()


        x+=1
        y-=1

        time.sleep(0.01)


if __name__ == "__main__":
    main()
'''
sudo apt-get install python3-pip
pip3  install pygame
'''