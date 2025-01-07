# image_sprite.py
'''
Title: Image Sprites
Author: Jako
Date-created: April 12, 2022
'''

import pygame
from my_sprite import MySprite

class ImageSprite(MySprite):
    """The class makes an image a sprite

    Args:
        MySprite (OBJ): The parent class
    """
    def __init__(self,IMAGE_FILE):
        """Gets the file path and creates an image sprite

        Args:
            IMAGE_FILE (STR): The path to the image file
        """
        super().__init__()
        self.__FILE_LOCATION = IMAGE_FILE
        self._SCREEN = pygame.image.load(self.__FILE_LOCATION).convert_alpha()

    # --- MODIFIER METHODS --- #
    def setScale(self,SCALE_X,SCALE_Y=0):
        """Sets the scale of the image

        Args:
            SCALE_X (INT): The X value
            SCALE_Y (int, optional): The Y value. Defaults to 0.
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SCREEN = pygame.transform.scale(self._SCREEN, (int(self.GET_WIDTH()/SCALE_X), int(self.GET_HEIGHT()/SCALE_Y)))

