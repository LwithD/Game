import pygame, sys
from pygame.locals import *

def get_event():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit(0)