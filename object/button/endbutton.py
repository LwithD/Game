import pygame
from pygame.locals import *
from setting.setting import *

class EndButton(object):
    def __init__(self):
        self.load()

    #生成幕布
    def load_image(self):
        self.image = pygame.Surface((end_button_width, end_button_height)).convert_alpha()
        self.image.fill(blue)

    #初始化加载
    def load(self):
        self.load_image()

    #绘制幕布
    def draw(self, screen):
        self.load_image()
        screen.blit(self.image, (screen_width-end_button_width-50, screen_height/2-end_button_height/2))