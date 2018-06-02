#-*- coding:utf-8 -*-
# pip install pygame
import pygame
import time

def main():

    screen = pygame.display.set_mode((480,852),0,32)


    backgroud = pygame.image.load("./feiji/background.png")

    #3. 创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")

    while True:
        screen.blit(backgroud,(0,0))

        screen.blit(hero,(210,700))
        pygame.display.update()

        time.sleep(0.01  )


if __name__ == "__main__":
    main()
'''
sudo apt-get install python3-pip
pip3  install pygame
'''