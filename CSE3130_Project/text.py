# text.py
'''
Title: Text Class
Author: Jako
Date-created: April 12, 2022
'''

import pygame
from my_sprite import MySprite

class Text(MySprite):
    """The Text sprite class

    Args:
        MySprite (OBJ): The parent class
    """
    def __init__(self,TEXT="Hello World",COLOR=(255,255,255),SIZE=25):
        super().__init__()
        self.__TEXT = TEXT
        self.__COLOR = COLOR
        self.__FONT = pygame.font.SysFont("Arial", SIZE)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self.__COLOR)

# --- MODIFIER METHODS --- #
    def setText(self,NEW_TEXT):
        self.__TEXT = str(NEW_TEXT)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self.__COLOR)