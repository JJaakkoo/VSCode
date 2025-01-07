# box.py
'''
title: box class 
author: Jako
date-created: March 24, 2022
'''

import pygame
from my_sprite import MySprite

class Box(MySprite):

    def __init__(self, WIDTH = 1, HEIGHT = 1, X = 0, Y = 0, COLOR = (255,255,255)):
        super().__init__()
        self.setX(X)
        self.setY(Y)
        self.setWidth(WIDTH)
        self.setHeight(HEIGHT)
        self.__COLOR = COLOR
        self._SCREEN = pygame.Surface(self.GET_DIMENSIONS(), pygame.SRCALPHA, 32)
        self._SCREEN.fill(self.__COLOR)

    # --- MODIFIER METHOD --- #
    def setWidth(self,WIDTH):
        super().setWidth(WIDTH)
        self._SCREEN = pygame.Surface(self.GET_DIMENSIONS(), pygame.SRCALPHA, 32)
        self._SCREEN.fill(self.__COLOR)

    def setHeight(self,HEIGHT):
        super().setHeight(HEIGHT)
        self._SCREEN = pygame.Surface(self.GET_DIMENSIONS(), pygame.SRCALPHA, 32)
        self._SCREEN.fill(self.__COLOR)

if __name__ == "__main__":
    
    pygame.init()

    from window import Window
    
    WINDOW = Window()
    BOX = Box(50,50)
    BOX.setWidth(100)
    BOX.setHeight(200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        BOX.wasdMove(PRESSED_KEYS)
        BOX.checkBoundaries(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())


        WINDOW.CLEAR_SCREEN()
        WINDOW.GET_SCREEN().blit(BOX.GET_SCREEN(), BOX.GET_POS())
        WINDOW.UPDATE_FRAME()