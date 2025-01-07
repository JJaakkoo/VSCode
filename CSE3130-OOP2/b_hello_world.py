# a_template.py
'''
Title: Working with text
Author: Jako
Date-created: March 21, 2022
'''

import pygame

class Color:
    WHITE = (255,255,255)
    GREY = (50,50,50)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)

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
        self.BACKGROUND = Color.GREY
        self.SCREEN.fill(self.BACKGROUND)
        self.CAPTION = pygame.display.set_caption(self.TITLE)
    
# --- MODIFIERS --- #

    def updateFrame(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def clearScreen(self):
        self.SCREEN.fill(self.BACKGROUND)

# --- ACCESSORS --- #

    def getScreen(self):
        return self.SCREEN

    def getVirtualWidth(self):
        return self.SCREEN.get_rect().width

    def getVirtualHeight(self):
        return self.SCREEN.get_rect().height


class Text:
    def __init__(self,TEXT, X = 0, Y = 0):
        self.TEXT = pygame.font.SysFont("Arial",48)
        self.SCREEN = self.TEXT.render(TEXT, 1, Color.GREEN)
        self.X = X
        self.Y = Y
        self.POS = (self.X, self.Y)
        self.DIRX = 1
        self.DIRY = 1
        self.SPEED = 10

    def bounceX(self,MAX_WIDTH):
        self.X += self.DIRX * self.SPEED
        self.POS = (self.X, self.Y)
        if self.X > MAX_WIDTH-self.SCREEN.get_rect().width:
            self.DIRX = -1
        elif self.X < 0:
            self.DIRX = 1

    def bounceY(self,MAX_HEIGHT):
        self.Y += self.DIRY * self.SPEED
        self.POS = (self.X, self.Y)
        if self.Y > MAX_HEIGHT:
            self.DIRY = -1
        elif self.Y < 0:
            self.DIRY = 1

    def getText(self):
        return self.SCREEN

    def getPOS(self):
        return self.POS
    
if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("Template",1280,720,30)
    TEXT = Text("Hello World!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        TEXT.bounceY(WINDOW.getVirtualHeight())
        TEXT.bounceX(WINDOW.getVirtualWidth())

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(TEXT.getText(),TEXT.getPOS())
        WINDOW.updateFrame()
            
