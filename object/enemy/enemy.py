import pygame
from pygame.locals import *
from setting.setting import *
from object.card.card import *

class Enemy(object):
    def __init__(self):
        self.load()

    #生成幕布
    def load_image(self):
        self.image = pygame.Surface((enemy_width, enemy_height)).convert_alpha()
        self.image.fill(green)

    #初始化加载
    def load(self):
        self.load_image()
        self.card = Card(screen_width/2-car_width/2, 150)#创建卡牌 绘制需要在游戏界面

    #绘制幕布
    def draw(self, screen):
        self.load_image()
        screen.blit(self.image, (screen_width/2 - enemy_width/2, 10))