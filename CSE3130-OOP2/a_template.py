# a_template.py
'''
Title: Pygame Template File
Author: Jako
Date-created: March 21, 2022
'''

import pygame

class Window:
    """Create the window that will load pygame
    """

    def __init__(self,TITLE,WIDTH,HEIGHT,FPS):
        self.TITLE = TITLE
        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCREEN_DIMENSIONS = (self.WIDTH, self.HEIGHT)
        self.FRAME = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMENSIONS)
        self.SCREEN.fill((50,50,50))
        self.CAPTION = pygame.display.set_caption(self.TITLE)
    
    def updateFrame(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def getScreen(self):
        return self.SCREEN

class Text:
    def __init__(self,TEXT):
        self.TEXT = pygame.font.SysFont("Arial",48)
        self.SCREEN = self.TEXT.render(TEXT, 1, (255,255,255))

    def getText(self):
        return self.SCREEN
    
if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("Template",1280,720,30)
    TEXT = Text("Hello World!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.getScreen().blit(TEXT.getText(),(1280//2.5,720//2.2))
        WINDOW.updateFrame()
            
