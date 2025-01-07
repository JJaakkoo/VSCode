# game.py - Glues together the objects and rules for the game

'''
title: game engine
author: Jako
date-created: 2022-04-05
'''

from window import Window
from text import Text
from image_sprite import ImageSprite
import pygame
import random

class Game:

    pygame.init()

    def __init__(self):
        ## --- SETUP
        self.__WINDOW = Window("Egg Hunt")
        self.__PLAYER = ImageSprite("d_egg_hunt/assets/bunny.png")
        self.__PLAYER.setScale(2)
        self.__PLAYER.setPOS((self.__WINDOW.getVirtualWidth()-self.__PLAYER.GET_WIDTH())//2,(self.__WINDOW.getVirtualHeight() - self.__PLAYER.GET_HEIGHT())//2)
        self.__score = 0
        self.__score_text = Text(f"SCORE: {self.__score}")
        self.__EGGS = []
        for i in range(1,3):
            self.__EGGS.append(ImageSprite(f"d_egg_hunt/assets/egg{i}.png"))
            self.__EGGS[-1].setScale(3)
            self.__placeItemRandom(self.__EGGS[-1])

        # --- SHRUBS --- #
        self.__SHRUBS = []
        for i in range(6):
            self.__SHRUBS.append(ImageSprite("d_egg_hunt/assets/shrubs.png"))
            self.__SHRUBS[-1].setScale(4.5)
            self.__placeItemRandom(self.__SHRUBS[-1])



    def run(self):
        ## --- Main Program Loop of Game
        while True:
            # --- INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYS_PRESSED = pygame.key.get_pressed()

            # --- PROCESSING
            self.__PLAYER.wasdMove(KEYS_PRESSED)
            self.__PLAYER.checkBoundaries(self.__WINDOW.getVirtualWidth(), self.__WINDOW.getVirtualHeight(),0,self.__score_text.GET_HEIGHT())

            ### Collisions
            for egg in self.__EGGS:
                if self.__getSpriteCollision(self.__PLAYER,egg):
                    self.__placeItemRandom(egg)
                    self.__score += 1
                    self.__score_text.SET_TEXT(f"SCORE: {self.__score}")

            ### Test for game End
            '''
            if self.__score > 9:
                pygame.quit()
                exit()
            '''

            # --- OUTPUTS 
            self.__WINDOW.CLEAR_SCREEN()
            for egg in self.__EGGS:
                self.__WINDOW.GET_SCREEN().blit(egg.GET_SCREEN(), egg.GET_POS())
            self.__WINDOW.GET_SCREEN().blit(self.__PLAYER.GET_SCREEN(), self.__PLAYER.GET_POS())
            for shrubs in self.__SHRUBS:
                self.__WINDOW.GET_SCREEN().blit(shrubs.GET_SCREEN(), shrubs.GET_POS())
            self.__WINDOW.GET_SCREEN().blit(self.__score_text.GET_SCREEN(), self.__score_text.GET_POS())

            self.__WINDOW.UPDATE_FRAME()
            

    def __placeItemRandom(self, ITEM):
        MAX_WIDTH = self.__WINDOW.getVirtualWidth()
        MAX_HEIGHT = self.__WINDOW.getVirtualHeight()
        ITEM.setX(random.randrange(MAX_WIDTH-ITEM.GET_WIDTH()))
        ITEM.setY(random.randrange(self.__score_text.GET_HEIGHT(), MAX_HEIGHT-ITEM.GET_HEIGHT()))

    def __getSpriteCollision(self, SPRITE1, SPRITE2):
        # SPRITE2 is redBox and SPRITE1 is PinkBox
        if (SPRITE2.GET_X() >= SPRITE1.GET_X() - SPRITE2.GET_WIDTH() 
        and SPRITE2.GET_X() <= SPRITE1.GET_X() + SPRITE1.GET_WIDTH() 
        and SPRITE2.GET_Y() >= SPRITE1.GET_Y() - SPRITE1.GET_HEIGHT()
        and SPRITE2.GET_Y() <= SPRITE1.GET_Y() + SPRITE1.GET_HEIGHT()):
            return True
        else:
            return False

if __name__ == "__main__":
    GAME = Game()
    GAME.run()
    