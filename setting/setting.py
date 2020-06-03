import pygame
from pygame.locals import *

FPS = 60
transparent = 0, 0, 0, 0#透明颜色
white = 255, 255, 255#测试主屏幕颜色
red = 255, 0, 0#测试玩家颜色
green = 0, 255, 0#测试敌人颜色
blue = 0, 0, 255#测试回合结束按钮颜色
black = 0, 0, 0#测试卡片颜色

#屏幕设置
screen_width = 1000
screen_height = 700

#玩家设置
player_width = 100
player_height = 100

#敌人设置
enemy_width = 100
enemy_height = 100

#结束回合按钮设置
end_button_width = 80
end_button_height = 40

#卡片设置
car_width = 100
car_height = 140