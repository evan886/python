#-*- coding:utf-8 -*-
# pip install pygame
import pygame
from pygame.locals import *
import time
import random

class BasePlane(object):
    def __init__(self,screen_temp, x , y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image  = pygame.image.load(image_name)
        self.bullet_list = [] #存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)

class HeroPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,210,700,"./feiji/hero1.png")
        #super().__init__(self,screen_temp,210,700,"./feiji/hero1.png")



    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

class EnemyPlane(BasePlane):
    """敌机的类 """
    def __init__(self,screen_temp):
        self.bullet_list = [] #存储发射出去的子弹对象引用
        BasePlane.__init__(self, screen_temp,0, 0, "./feiji/enemy0.png")
        self.direction = "right" #用来存储飞机默认的显示方向
#显示
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move() #why move
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move(self):

        if self.direction=="right":
            self.x += 5
        elif self.direction=="left":
            self.x -= 5


        if self.x>480-50:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

class BaseBullet(object)
    self.x = x
    self.y = y
    self.screen = screen_temp
    self.image = pygame.image.load("./feiji/bullet.png")
class Bullet(object):
    def __init__(self,screen_temp,x,y): #不加x ,y 崩

        BaseBullet.__init__(self,screen_temp,x+40,)
        self.x= x+40
        self.y= y-20
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):
        self.screen.blit(self.image,(self.x, self.y))

    def move(self):
        self.y-=20

#judge v判断
    def judge(self):
        if self.y<0:
            return True
        else:
            return False


class EnemyBullet(object):
    def __init__(self,screen_temp,x,y): #不加x ,y 崩
        self.x= x+25
        self.y= y+40
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet1.png")

    def display(self):
        self.screen.blit(self.image,(self.x, self.y))

    def move(self):
        self.y+=5

#judge v判断
    def judge(self):
        if self.y>852:
            return True
        else:
            return False



#why is hero_temp
def key_control(hero_temp):

    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()


def main():

    screen = pygame.display.set_mode((480,852),0,32)


    background = pygame.image.load("./feiji/background.png")

    #3. 创建一个飞机对象
    hero = HeroPlane(screen)

    # 4. 创建一个敌机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()#调用敌机的移动方法
        enemy.fire()#敌机开火
        pygame.display.update() #更新需要显示的内容
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
'''
sudo apt-get install python3-pip
pip3  install pygame
'''
