# image_sprite.py
'''
Title: Image Sprites
Author: Jako
Date-created: march 24, 2022
'''

import pygame 
from my_sprite import MySprite

class ImageSprite(MySprite):

    def __init__(self, IMAGE_FILE):
        super().__init__()
        self.__FILE_LOCATION = IMAGE_FILE
        self._SCREEN = pygame.image.load(self.__FILE_LOCATION).convert_alpha()
        self.__X_FLIP = False

    # --- MODIFIER MEHTOD --- #

    def setScale(self, SCALE_X, SCALE_Y = 0):
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SCREEN = pygame.transform.scale(self._SCREEN, (int(self.GET_WIDTH()/SCALE_X), int(self.GET_HEIGHT()/SCALE_Y)))

    def __flipImageX(self,KEY_PRESSES):
        if KEY_PRESSES[pygame.K_d] and self.__X_FLIP:
            self._SCREEN = pygame.transform.flip(self._SCREEN, True, False)
            self.__X_FLIP = False
        if KEY_PRESSES[pygame.K_a] and not self.__X_FLIP:
            self._SCREEN =  pygame.transform.flip(self._SCREEN, True, False)
            self.__X_FLIP = True

    def rotateImage(self,KEY_PRESSES):
        LR = 0
        if KEY_PRESSES[pygame.K_d]:
            LR = 1
        if KEY_PRESSES[pygame.K_a]:
            LR = -1

        ANGLE = 0
        ANGLE += 1*LR
        
        self._SCREEN = pygame.transform.rotate(self._SCREEN, ANGLE)



    def wasdMove(self, KEY_PRESSES):
        super().wasdMove(KEY_PRESSES)
        self.__flipImageX(KEY_PRESSES)
        #self.__rotateImage(KEY_PRESSES)


if __name__ == "__main__":
    from window import Window
    
    pygame.init()
    
    WINDOW = Window()
    BUNNY = ImageSprite("d_egg_hunt/assets/white3.jpg")
    BUNNY.setScale(25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        BUNNY.rotateImage(PRESSED_KEYS)

        #BUNNY.wasdMove(PRESSED_KEYS)
        #BUNNY.checkBoundaries(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        WINDOW.CLEAR_SCREEN()
        WINDOW.GET_SCREEN().blit(BUNNY.GET_SCREEN(), BUNNY.GET_POS())
        WINDOW.UPDATE_FRAME()