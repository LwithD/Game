import pygame, sys
from pygame.locals import *
from setting.setting import *
from screen.mainscreen import *
from function import *

pygame.init()
FPS_control = pygame.time.Clock()#设置FPS

screen = pygame.display.set_mode((screen_width, screen_height))#创建屏幕
main_screen = MainScreen()

while True:
    keys = pygame.key.get_pressed()#获取键盘事件
    #如何获取键盘事件
    #keys[K_a]就是a键，以此类推
    ticks = pygame.time.get_ticks()#获取游戏时间
    #如何设置时间间隔触发事件
    #类中设置self.last_tick = 0
    #if ticks > self.last_tick + time_interval(数值):
    #   执行语句
    #   self.last_tick = ticks
    mouse_position = pygame.mouse.get_pos()#获取鼠标位置
    #mouse_position[0-2] 左键 中键 右键 bool值
    get_event()#鼠标键盘事件

    #屏幕绘制
    main_screen.draw(screen)

    FPS_control.tick(FPS)
    pygame.display.update()