# game.py
'''
Title: Asteroid avoider
Author: Jako
Date-created: April 11 2022
'''

from window import Window
from text import Text
from image_sprite import ImageSprite
import pygame
import random

class Game:
    pygame.init()

    def __init__(self):
        # --- SETUP --- #
        self.__WINDOW = Window("Asteroid Avoider")

        self.__SCORE = 0
        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE}")
        self.__HEALTH = 3
        self.__HEALTH_TEXT = Text(f"Health: {self.__HEALTH}")
        self.__HEALTH_TEXT.setX(self.__WINDOW.getVirtualWidth()-self.__HEALTH_TEXT.GET_WIDTH()) 

        self.__PLAYER = ImageSprite("e_space/assets/ship.png")
        self.__PLAYER.setX(self.__WINDOW.getVirtualWidth()-self.__PLAYER.GET_WIDTH())
        self.__PLAYER.setY(self.__WINDOW.getVirtualHeight()//2 - self.__PLAYER.GET_HEIGHT()//2)

        self.__ASTEROIDS = []
        for i in range(4):
            self.__ASTEROIDS.append(ImageSprite("e_space/assets/asteroid.png"))
            self.__ASTEROIDS[-1].setScale(3.5)
            self.__placeItemRandom(self.__ASTEROIDS[-1])



    def run(self):
        ## --- Main Program Loop --- ##
        while True:
            # --- INPUTS --- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYS_PRESSED = pygame.key.get_pressed()

            # --- PROCESSING --- #
            self.__PLAYER.wasdMove(KEYS_PRESSED)

            self.__PLAYER.checkBoundaries(self.__WINDOW.getVirtualWidth(), self.__WINDOW.getVirtualHeight(), 0, self.__SCORE_TEXT.GET_HEIGHT())

            ### COLLISIONS
            for ast in self.__ASTEROIDS:
                if self.__getSpriteCollision(self.__PLAYER, ast):
                    self.__placeItemRandom(ast)
                    self.__HEALTH -= 1
                    self.__HEALTH_TEXT.SET_TEXT(f"HEALTH: {self.__HEALTH}")

            if self.__SCORE > 19:
                pygame.quit()
                exit()

            if self.__HEALTH <= 0:
                pygame.quit()
                exit()


            # --- OUTPUTS --- #
            self.__WINDOW.CLEAR_SCREEN()

            self.__WINDOW.GET_SCREEN().blit(self.__SCORE_TEXT.GET_SCREEN(), self.__SCORE_TEXT.GET_POS())
            self.__WINDOW.GET_SCREEN().blit(self.__HEALTH_TEXT.GET_SCREEN(), self.__HEALTH_TEXT.GET_POS())
            self.__WINDOW.GET_SCREEN().blit(self.__PLAYER.GET_SCREEN(), self.__PLAYER.GET_POS())

            for ast in self.__ASTEROIDS:
                self.__WINDOW.GET_SCREEN().blit(ast.GET_SCREEN(), ast.GET_POS())
                ast.setX(ast.GET_X() + ast.GET_SPEED())
                if ast.GET_X() > self.__WINDOW.getVirtualWidth() + ast.GET_WIDTH():
                    self.__placeItemRandom(ast)
                    self.__SCORE += 1
                    self.__SCORE_TEXT.SET_TEXT(f"SCORE: {self.__SCORE}")


            self.__WINDOW.UPDATE_FRAME()

    

    def __placeItemRandom(self, ITEM):
        MAX_WIDTH = self.__WINDOW.getVirtualWidth()
        MAX_HEIGHT = self.__WINDOW.getVirtualHeight()
        ITEM.setX(random.randrange(MAX_WIDTH*2+ITEM.GET_WIDTH())*-1)
        ITEM.setY(random.randrange(self.__SCORE_TEXT.GET_HEIGHT(), MAX_HEIGHT-ITEM.GET_HEIGHT()))

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