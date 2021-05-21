#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, pygame
from pygame.locals import *
import objects, config
import time


class State:
    def handle(self, event):
        # """ 只处理退出事件的默认事件处理 """
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    def firstDisplay(self, screen):
        """   用于第一次显示状态,使用背景色填充屏幕"""
        screen.fill(config.background_color)
        # 记得要调用flip,让更改可见
        pygame.display.flip()

    def display(self, screen):
        """"""

        pass


class Level(State):
    """
    游戏等级,用于计算已经落下了多少秤砣,移动子图形以及其它和游戏逻辑相关的任务
    """

    def __init__(self, number=1):
        self.number = number
        # 本关内还要落下多少秤砣?
        self.remaining = config.weights_per_level

        speed = config.drop_speed
        # 为每个大于1的等级都增加一个speed_increase:
        speed += (self.number - 1) * config.speed_increase

        # 创建秤砣和香蕉
        self.weight = objects.Weight(speed)
        self.banana = objects.Banana()
        both = self.weight, self.banana  # This could contain more sprites.
        self.sprites = pygame.sprite.RenderUpdates(both)

    def update(self, game):
        # """ 从前一帧更新游戏状态""""
        # 更新所有的子图形
        self.sprites.update()
        # 如果香蕉碰到秤砣 那么告诉游戏切到gameover状态
        if self.banana.touches(self.weight):
            game.nextState = GameOver()
        # 否则在秤砣落地时其复位
        # 如果本关内的所有秤砣都落下了,则让游戏切到LevelCleared状态
        elif self.weight.landed:
             self.weight.reset()
             self.remaining -= 1
             if self.remaining == 0:
                 game.nextState = LevelCleared(self.number)

    def display(self, screen):
        """
            在第一次显示(只清空屏幕)后显示状态,与firstDisplay 不同,这个方法使用pygame.display.update 对self.sprites.draw提供的 需要更新的矩形列表进行更新
        """
        screen.fill(config.background_color)
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)


class Paused(State):
    """
    简单的暂停游戏状态 按下键盘上任意键 or 点击mouse 都会结束这个状态
    """

    finished = 0  # 用户结束暂停了吗?
    image = None  # 如果用户要图片,将这个变量设定为文件名
    text = " "  # 设定为一些提示性文本

    def handle(self, event):
        """
        通过对State进行委托(一般处理退出事件)以及对按键和mouse点击作出自应来处理事件
        如果按下或者 mouse 被点击self.finished 设定为真
        """

        State.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.finished = 1

    def update(self, game):
        # """
        # 更新等级,如果按键被按下或者mouse 被点击 eg self.finished为真 ,告诉游戏到下一个由
        # self.nextState() 表示的状态(应该由子类来实现)
        # """

        if self.finished:
            game.nextState = self.nextState()

    def firstDisplay(self, screen):
        """
        暂停状态第一次出现时,绘制图像,如果有 ,并生成文本
        """

        # 首先使用填充背景色的方法清空屏幕:
        screen.fill(config.background_color)

        # 使用默认的外观和指定的大小创建font对象
        font = pygame.font.Font(None, config.font_size)

        # 获取self.text中的文本行,忽略开头和结尾的空行

        lines = self.text.strip().splitlines()

        # 计算文本的高度(using font.get_linesize( 获取每行文本的高度
        height = len(lines) * font.get_linesize()

        # 计算文本的放置位置(centered on the screen)
        center, top = screen.get_rect().center  # 为400,300
        top -= height // 2  # 260

        # 如果有图片要显示的话
        if self.image:
            # load图片
            image = pygame.image.load(self.image).convert()
            # 获取它的rect
            r = image.get_rect()  # 为rect(0,0,166,132)
            # 图片向下移动其高度的一半的距离
            top += r.height // 2  # 326
            # 将图片放在文本上方20pixel处
            r.midbottom = center, top - 20  # 400, 306
            # 将图片移动到屏幕上
            screen.blit(image, r)

        antialias = 1  # Smooth the text
        black = 0, 0, 0  # Render it as black

        # 生成所有行,从计算过的top开始,并
        # 对于每一行向下移动font.get_linesize() 像素
        for line in lines:
            text = font.render(line.strip(), antialias, black)
            r = text.get_rect()  # 0,0,312,37
            r.midtop = center, top  # 400,326
            screen.blit(text, r)
            top += font.get_linesize()

        # 显示所有更改
        pygame.display.flip()


class Info(Paused):
    """
    简单的暂停状态,显示有关游戏的信息, 在level状态后显示 (第一级)
    """

    nextState = Level
    text = """
    In this game you are a banana,
    trying to survive a course in
    self-defense against fruit, where the
    participants will "defend" themselves
    against you with a 16 ton weight."""


class StartUp(Paused):
    """
    显示展示图片和welcome message 在Info 状态后显示
    """

    nextState = Info
    image = config.splash_image #config.py splash_image 指定的图片 
    text = """
    Welcome to Squish, by evan tag
    the game of Fruit Self-Defense
    """


class LevelCleared(Paused):
    """
    提示用户过关的暂停状态,在next level 状态后显示
    """

    def __init__(self, number):
        self.number = number
        self.text = (
            """ Level %i cleared
        Click to start next level """
            % self.number
        )

    def nextState(self):
        return Level(self.number + 1)


class GameOver(Paused):
    """
    表示用户输掉游戏的状态,在first level后显示
    """

    nextState = Level
    text = """
    Game Over
    Click to Restart, Esc to Quit"""


class Game:
    """
    负责主事件循环的游戏对象 任务包括在不同状态间切换
    """

    def __init__(self, *args):
        # 获取游戏和图像放置的目录 may 2021 os.path.abspath(file)返回代码文件的所在的目录,不带文件名
        path = os.path.abspath(args[0]) #当前代码文件路径 原来用在这里的 Game(*sys.argv)
        #print(os.path.abspath(args[0]))
        #print(path) #/home/evan/github/python/project/chapter29squish/game.py
        dir = os.path.split(path)[0]  # 代码目录
        # 移动哪个目录 (这样图片文件可以在随后打开)
        #print(dir) #/home/evan/github/python/project/chapter29squish
        os.chdir(dir)  # cd到代码目录
        # 无状态方式启动
        self.state = None 
        # 在第一个事件循化迭代中移动到StartUp
        self.nextState = StartUp() # to  class StartUp  #here evan 

    def run(self):
        """
        这个方法动态设定变量,进行一些重要的初始化工作,并进入主事件循环
        """

        pygame.init()  # 初始化所有pygame模块

        # 决定以窗口模式还是全屏模式显示游戏

        flag = 0  # 默认窗口

        if config.full_screen:
            flag = FULLSCREEN  # 全屏模式  config.py 里面是0 所以这句不会执行的,也就是窗口默认
        screen_size = config.screen_size
        screen = pygame.display.set_mode(screen_size, flag)

        pygame.display.set_caption("Fruit Self Defense")
        pygame.mouse.set_visible(False)

        # 主循环
        while True:
            # (1)如果nextState 被 修改了 那么移到新的状态,并显示它(第一次 )
            if self.state != self.nextState:
                self.state = self.nextState
                self.state.firstDisplay(screen)
            # (2)代理当前状态的事件处理
            for event in pygame.event.get():
                self.state.handle(event)
            # (3) 更新当前状态
            self.state.update(self)
            # (4)显示当前状态
            self.state.display(screen)


if __name__ == "__main__":
    #print(sys.argv) #['game.py']
    #game = Game(sys.argv[0]) #这样也是可以的
    game = Game(*sys.argv)

    game.run()
