#!/usr/bin/python
#encoding=utf-8

import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'background.png'
mouse_image_filename = 'mouse.png'

#Pygame初始化
pygame.init()

screen = pygame.display.set_mode((512, 512), 0, 32)
pygame.display.set_caption("Hello, World!")

#加载图片
background = pygame.image.load(background_image_filename).convert() 
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

#进入Pygame循环
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.blit(background, (0,0))

	x, y = pygame.mouse.get_pos()

	x-= mouse_cursor.get_width() / 2
	y-= mouse_cursor.get_height() / 2

	screen.blit(mouse_cursor, (x, y))

	pygame.display.update()
