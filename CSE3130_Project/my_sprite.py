# my_sprite.py
'''
Title: Abstract Sprite Class
Author: Jako
Date-created: April 12, 2022
'''

import pygame

class MySprite:
    """The main abstract class of the Brick Breaker game
    """
    def __init__(self,WIDTH=0,HEIGHT=0,X=0,Y=0,COLOR=(255,255,255)):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__XSPEED = 6
        self.__YSPEED = -6
        self.__COLOR = COLOR
        self._SCREEN = pygame.Surface(self.__DIMENSIONS, pygame.SRCALPHA, 32)
        self._SCREEN.fill(self.__COLOR)

# --- Modifier Methods --- #
    def setXSpeed(self,SPEED):
        self.__XSPEED = SPEED

    def addXSpeed(self,SPEED):
        self.__XSPEED += SPEED

    def setYSpeed(self,SPEED):
        self.__YSPEED = SPEED

    def addYSpeed(self,SPEED):
        self.__YSPEED += SPEED

    def addX(self,X):
        self.__X += X
        self.__updatePOS()

    def addY(self,Y):
        self.__Y += Y
        self.__updatePOS()
    
    def setWidth(self,WIDTH):
        self.__WIDTH = WIDTH 
        self.__DIMENSIONS = (self.__WIDTH,self.__HEIGHT)

    def setHeight(self,HEIGHT):
        self.__HEIGHT = HEIGHT
        self.__DIMENSIONS = (self.__WIDTH,self.__HEIGHT)

    def __updatePOS(self):
        self.__POS = (self.__X,self.__Y)

    def setPOS(self,X,Y):
        self.__X = X
        self.__Y = Y
        self.__updatePOS()

    def setX(self,X):
        self.__X = X
        self.__updatePOS()

    def setY(self,Y):
        self.__Y = Y
        self.__updatePOS()

    def setColor(self,COLOR):
        self.__COLOR = COLOR
        self._SCREEN.fill(self.__COLOR)

    def adMove(self, KEY_PRESSES):
        if KEY_PRESSES[pygame.K_d] == 1:
            self.__X += self.__XSPEED
        if KEY_PRESSES[pygame.K_a] == 1:
            self.__X -= self.__XSPEED
        self.__updatePOS()

    def checkBoundaries(self,MAX_WIDTH,MAX_HEIGHT,MIN_WIDTH=0,MIN_HEIGHT=0):
        if self.GET_X() > MAX_WIDTH - self.GET_WIDTH():
            self.setX(MAX_WIDTH - self.GET_WIDTH())
        elif self.GET_X() < MIN_WIDTH:
            self.setX(MIN_WIDTH)
        
        if self.GET_Y() > MAX_HEIGHT - self.GET_HEIGHT():
            self.setY(MAX_HEIGHT - self.GET_HEIGHT())
        elif self.GET_Y() < MIN_HEIGHT:
            self.setY(MIN_HEIGHT)
    
# --- ACCESSOR METHODS --- #
    def GET_XSPEED(self):
        return self.__XSPEED

    def GET_YSPEED(self):
        return self.__YSPEED

    def GET_SCREEN(self):
        return self._SCREEN

    def GET_POS(self):
        return self.__POS
    
    def GET_X(self):
        return self.__X
    
    def GET_Y(self):
        return self.__Y
    
    def GET_WIDTH(self):
        return self._SCREEN.get_rect().width

    def GET_HEIGHT(self):
        return self._SCREEN.get_rect().height

    def GET_DIMENSIONS(self):
        return self.__DIMENSIONS
