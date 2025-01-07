# my_sprite.py
'''
Title: Abstract Sprite Class
Author: Jako
Date-created: March 23, 2022
'''

import pygame

class MySprite:
    """This class is the building block of other sprite classes
    """

    def __init__(self):
        self.__WIDTH = 0
        self.__HEIGHT = 0
        self.__DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self._SCREEN = None
        self.__X = 0
        self.__Y = 0
        self.__POS = (self.__X, self.__Y)
        self.__SPEED = 10

    # --- Modifier Methods --- #

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
        self.__POS = (self.__X,self.__Y)
        self.__updatePOS()

    def setX(self, X):
        self.__X = X
        self.__updatePOS()

    def setY(self,Y):
        self.__Y = Y
        self.__updatePOS()

    def wasdMove(self, KEY_PRESSES):
        if KEY_PRESSES[pygame.K_d] == 1:
            self.__X += self.__SPEED
        if KEY_PRESSES[pygame.K_a] == 1:
            self.__X -= self.__SPEED
        if KEY_PRESSES[pygame.K_s] == 1:
            self.__Y += self.__SPEED
        if KEY_PRESSES[pygame.K_w] == 1:
            self.__Y -= self.__SPEED
        self.__updatePOS()

    def checkBoundaries(self, MAX_WIDTH,MAX_HEIGHT,MIN_WIDTH=0,MIN_HEIGHT=0):
        if self.GET_X() > MAX_WIDTH - self.GET_WIDTH():
            self.setX(MAX_WIDTH - self.GET_WIDTH())
        elif self.GET_X() < MIN_WIDTH:
            self.setX(MIN_WIDTH)
        
        if self.GET_Y() > MAX_HEIGHT - self.GET_HEIGHT():
            self.setY(MAX_HEIGHT - self.GET_HEIGHT())
        elif self.GET_Y() < MIN_HEIGHT:
            self.setY(MIN_HEIGHT)
        
    def adMove(self, KEY_PRESSES):
        if KEY_PRESSES[pygame.K_d] == 1:
            self.__X += self.__SPEED
        if KEY_PRESSES[pygame.K_a] == 1:
            self.__X -= self.__SPEED
        self.__updatePOS()
        
    # --- ACCESSOR METHODS --- #

    def GET_SPEED(self):
        return self.__SPEED

    def GET_SCREEN(self):
        return self._SCREEN

    def GET_POS(self):
        return self.__POS

    def GET_X(self):
        return self.__X
    
    def GET_Y(self):
        return self.__Y

    def getIntX(self):
        print (self.__X)
    def getIntY(self):
        print (self.__Y)

    def GET_WIDTH(self):
        return self._SCREEN.get_rect().width

    def GET_HEIGHT(self):
        return self._SCREEN.get_rect().height

    def GET_DIMENSIONS(self):
        return self.__DIMENSIONS    
