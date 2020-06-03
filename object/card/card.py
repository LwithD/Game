import pygame
from pygame.locals import *
from setting.setting import *

class Card(object):
    def __init__(self, x, y):
        self.load(x, y)

    #生成幕布
    def load_image(self):
        self.image = pygame.Surface((car_width, car_height)).convert_alpha()
        self.image.fill(black)

    #初始化加载
    def load(self, x, y):
        self.load_image()
        self.x = x
        self.y = y

    #绘制幕布
    def draw(self, screen):
        self.load_image()
        screen.blit(self.image, (self.x, self.y))