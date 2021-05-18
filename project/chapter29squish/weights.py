#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, pygame
from pygame.locals import *
from random  import  randrange

class Weight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #在画sprite时使用的图像和矩型
        self.image = weight_image
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        """
        秤砣移动到屏幕顶端的随机位置
        """
        self.rect.top = self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    def update(self):
        """
        更新秤砣 显示下一帧
        """
        self.rect.top += 1
        if self.rect.top > screen_size[1]:
            self.reset()

#初始化 pass 
pygame.init()
screen_size = 800, 600
pygame.display.set_mode(screen_size,FULLSCREEN)
pygame.mouse.set_visible(0)

#load秤砣图像
weight_image = pygame.image.load('weights.png')
weight_image = weight_image.convert()   # ? to match the display

#创建一个子图形组
sprites = pygame.sprite.RenderUpdates()
sprites.add(Weight())

#取屏表面 全白填充
screen =pygame.display.get_surface()
bg =(255,255,255) # while
screen.fill(bg)
pygame.display.flip()

#用于清除图形
def clear_callback(surf, rect):
    surf.fill(bg,rect)

while True:
    #检查退出事件
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        #清除前面的位置
        sprites.clear(screen,clear_callback)
        #更新所有子图形
        sprites.update()
        #绘制所有子图形
        updates = sprites.draw(screen)
        #更新要显示的部分
        pygame.display.update(updates)
