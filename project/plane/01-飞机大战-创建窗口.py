#-*- coding:utf-8 -*-
# pip install pygame
import pygame
import time

def main():

    screen = pygame.display.set_mode((480,852),0,32)


    backgroud = pygame.image.load("./feiji/background.png")

    while True:
        screen.blit(backgroud,(0,0))

        pygame.display.update()

        time.sleep(0.01  )


if __name__ == "__main__":
    main()
'''
sudo apt-get install python3-pip
pip3  install pygame
'''