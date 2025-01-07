# window.py
'''
Title: Pygame Window Class 
Author: Jako
Date-created: March 23, 2022
'''

import pygame

class Window:
    
    def __init__(self, TITLE="pygame",WIDTH=640,HEIGHT=480,FPS=30):
        self.__TITLE = TITLE        
        self.__FPS = FPS
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__BACKGROUND = (50,50,50)
        self.__FRAME = pygame.time.Clock()
        self.__SCREEN = pygame.display.set_mode(self.__SCREEN_DIMENSIONS)
        self.__SCREEN.fill(self.__BACKGROUND)
        self.__CAPTION = pygame.display.set_caption(self.__TITLE)

    # --- MODIFIER METHODS --- #
    def SET_BG_COLOR(self, COLOR):
        """Chagnes the background color

        Args:
            COLOR (tuple): (r, g, b)
        """
        self.__BACKGROUND = COLOR

    def UPDATE_FRAME(self):
        self.__FRAME.tick(self.__FPS)
        pygame.display.flip()

    def CLEAR_SCREEN(self):
        self.__SCREEN.fill(self.__BACKGROUND)

    # --- ACCESSOR METHODS --- #
    def GET_SCREEN(self):
        return self.__SCREEN
    
    def getVirtualWidth(self):
        return self.__SCREEN.get_rect().width

    def getVirtualHeight(self):
        return self.__SCREEN.get_rect().height

if __name__ == "__main__":
    pygame.init()

    WINDOW = Window()
    WINDOW.SET_BG_COLOR((255,255,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        WINDOW.CLEAR_SCREEN()
        WINDOW.UPDATE_FRAME()







