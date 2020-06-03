import pygame
from pygame.locals import *
from setting.setting import *
from object.player.player import *
from object.enemy.enemy import *
from object.button.endbutton import *

#游戏幕布 绘制在主屏幕上
class GameScreen(object):
    def __init__(self):
        self.load()

     #生成幕布
    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)

    #初始化加载
    def load(self):
        self.load_image()
        self.player = Player()#创建游戏玩家
        self.enemy = Enemy()#创建敌人
        self.end_button = EndButton()#创建回合结束按钮

    #绘制幕布
    def draw(self, screen):
        self.load_image()
        self.player.draw(self.image)#绘制游戏玩家
        self.enemy.draw(self.image)#绘制敌人
        self.end_button.draw(self.image)#绘制回合结束按钮
        self.player.card.draw(self.image)#绘制玩家卡牌 未做循环
        self.enemy.card.draw(self.image)#绘制玩家卡牌 未做循环
        screen.blit(self.image, (0, 0))