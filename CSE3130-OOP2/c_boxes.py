# c_boxes.py
'''
Title: boxes
Author: Jako
Date-created: march 22, 2022
'''

import pygame

class Window:
    def __init__(self, TITLE="Pygame", WIDTH=640, HEIGHT=480, FPS=30):
        self.TITLE = TITLE
        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCREEN_DIMENSIONS = (self.WIDTH, self.HEIGHT)
        self.FRAME = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMENSIONS)
        self.SCREEN.fill((50,50,50))

    # --- Modifier (Setter) Methods --- #
    def UPDATE_FRAME(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    # --- Accessor (Getter) Methods --- #
    def GET_SCREEN(self):
        return self.SCREEN
    
    def getVirtualWidth(self):
        return self.SCREEN.get_rect().width

    def getVirtualHeight(self):
        return self.SCREEN.get_rect().height

    def CLEAR_SCREEN(self):
        self.SCREEN.fill((50,50,50))

class Box:
    """Creates a box that can be moved with WASD
    """
    def __init__(self,WIDTH=50,HEIGHT=50,X=0,Y=0,COLOR=(255,255,255)):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.X = X
        self.Y = Y
        self.COLOR = COLOR
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.POS = (self.X, self.Y)
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32) # make png with no backgrounds work
        self.SCREEN.fill(self.COLOR)
        self.SPEED = 10

    # --- Modifier Methods --- #
    def MOVE_BOX(self,KEY_PRESSES,MAX_WIDTH,MAX_HEIGHT):
        # check keypresses
        if KEY_PRESSES[pygame.K_d] == 1:
            self.X += self.SPEED

        if KEY_PRESSES[pygame.K_a] == 1:
            self.X -= self.SPEED

        if KEY_PRESSES[pygame.K_w] == 1:
            self.Y -= self.SPEED

        if KEY_PRESSES[pygame.K_s] == 1:
            self.Y += self.SPEED

        if self.X > MAX_WIDTH - self.SCREEN.get_rect().width:
            self.X = MAX_WIDTH - self.SCREEN.get_rect().width

        elif self.X < 0:
            self.X = 0

        if self.Y > MAX_HEIGHT - self.SCREEN.get_rect().height:
            self.Y = MAX_HEIGHT - self.SCREEN.get_rect().height

        elif self.Y < 0:
            self.Y = 0

        self.POS = (self.X, self.Y)


    # --- Accessor Methods --- #
    def GET_BOX(self):
        return self.SCREEN

    def GET_POS(self):
        return self.POS
        

if __name__ == "__main__":
    
    pygame.init()

    WINDOW = Window()
    #BOX = Box()
    #RED_BOX = Box(10,10,200,300,(255,0,0))
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        KEYS = pygame.key.get_pressed()

        #BOX.MOVE_BOX(KEYS, WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        WINDOW.CLEAR_SCREEN()
        #WINDOW.GET_SCREEN().blit(BOX.GET_BOX(), BOX.GET_POS())
        #WINDOW.GET_SCREEN().blit(RED_BOX.GET_BOX(), RED_BOX.GET_POS())
        WINDOW.UPDATE_FRAME()
