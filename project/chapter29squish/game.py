#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame.locals import *
import objects, config
import time


class State:
    def handle(self, event):
    """ 只处理退出事件的默认事件处理 """
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()








    def firtDisplay(self,screen):
        """   用于第一次显示状态,使用背景色填充屏幕"""
        screen.fill(config.background_color)
        #记得要调用flip,让更改可见
        pygame.display.flip()

    def display(self,screen):
        """"""

        pass








class Level(State):


if __name__ == "__main__":
    # print(sys.argv)
    game = Game(*sys.argv)
    game.run()
