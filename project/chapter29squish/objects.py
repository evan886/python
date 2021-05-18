#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame, config,os
from random import randrange


class SquishSprite(pygame.sprites.Sprite):








    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen =pygame.display.get_surface()
        shrink = -config.margin *2 # ?
        size = screen.get_rect(); # ?
        self.area = screen.get_rect.inflate(shrink,shrink) # ?



class Weight(SquishSprite):







    def __init__(self,speed):
        SquishSprite.__init__(self,config.weight_image)
        self.speed = speed
        self.reset()

    def reset(self):
        x = randrange(self.area.left,self.area.right)
        self.rect.midbottom = x,0

    def update(self):
        """
 根据它的速度将秤砣垂直移动(下落)一段距离,并根据它是否触及屏幕底端来设置landed属性
        """
        self.rect.top += self.speed
        self.landed = self.rect.otp >=self.area.bottom









class  Banana(SquishSprite):
    """
    绝望的banana 使用SquishSprite 构造func设置香蕉的图像,并会停留在屏幕底端 它的水平位置由当前的mouse 位置(有一定限制)决定
    """

    def __init__(self):
        SquishSprite.__init__(self, config.banana_image)
        self.rect.bottom = self.area.bottom
        """在没有香蕉的部分进行填充,如果秤砣移动到了这些区域,它不会被判为碰撞 或说把香蕉压扁 """
        self.pad_top = config.banana_pad_top
        self.pad_side =config.banana_pad_top


    def update(self):
        """  """
        self.rect.centerx = pygame.mouse.get_post()[]
        self.rect = self.rect.clamp(self.area)

    def  touches(self,other):
        """  ""
        bounds = self.rect.inflate(-self.pad_side,-self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)
