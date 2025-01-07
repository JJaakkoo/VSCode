# text.py
'''
Title: Text Class
Author: Jako
Date-created: March 23, 2022
'''

import pygame
from my_sprite import MySprite

class Text(MySprite):
    """The Text Class creates text sprites and inherits from the MySprite Class

    Args:
        MySprite (class): abstract sprite class
    """

    def __init__(self,TEXT = "Hello World", COLOR = (255,255,255)):
        super().__init__() #bring in the parent class constructor (MySprite)
        self.__TEXT = TEXT
        self.__COLOR = COLOR
        self.__FONT = pygame.font.SysFont("Arial", 36)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self.__COLOR)

    def SET_TEXT(self, NEW_TEXT):
        self.__TEXT = str(NEW_TEXT)
        self._SCREEN = self.__FONT.render(self.__TEXT, True, self.__COLOR)

if __name__ == "__main__":
    from window import Window
    pygame.init()
    WINDOW = Window()
    TEXT1 = Text()
    NUMBERS = 0
    
    while True:
        NUMBERS += 1
        TEXT1.SET_TEXT(NUMBERS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit

        WINDOW.CLEAR_SCREEN()
        WINDOW.GET_SCREEN().blit(TEXT1.GET_SCREEN(), TEXT1.GET_POS())
        WINDOW.UPDATE_FRAME()
