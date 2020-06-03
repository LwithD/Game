import pygame
from pygame.locals import *
from setting.setting import *
from screen.gamescreen import *

#主屏幕 绘制在屏幕上
class MainScreen(object):
    def __init__(self):
        self.load()

    #生成幕布
    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(white)

    #初始化加载
    def load(self):
        self.load_image()
        self.game_screen = GameScreen()#创建游戏幕布

    #绘制幕布
    def draw(self, screen):
        self.load_image()
        self.game_screen.draw(self.image)#绘制游戏幕布
        screen.blit(self.image, (0, 0))