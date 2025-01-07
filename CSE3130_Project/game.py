# game.py

'''
Title: Game class
Author: Jako
Date-created: April 13, 2022
'''

import pygame
from image_sprite import ImageSprite
from text import Text
from brick import Brick
from window import Window
from paddle import Paddle
from topbar import TopBar
from ball import Ball
from random import randrange
from playsound import playsound

class Game:
    """The game class that puts everything together
    """
    pygame.init()
    def __init__(self):
        self.__resetGame()

# --- Initiate Fucntion --- #
    # Where the attributes are created
    def __resetGame(self,HEALTH=7,SOUND=False):
        """The function that creates all the attributes

        Args:
            HEALTH (int, optional): the health chosen. Defaults to 7.
            SOUND (bool, optional): if the volume is on or off. Defaults to False.
        """
        self.__SOUND = SOUND # Variable for if sound is on or off

        self.__WINDOW = Window("Brick Breaker") # The window attribute

## --- All the text attributes
        self.__SCORE = 0
        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE}")
        self.__SCORE_TEXT.addY(5)

        self.__GAME_TITLE = Text("BRICK BREAKER")
        self.__GAME_TITLE.setX(self.__WINDOW.getVirtualWidth()//2-self.__GAME_TITLE.GET_WIDTH()//2)
        self.__GAME_TITLE.addY(5)
        
        self.__START = Text("Press Space to start!")
        self.__START.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__START.GET_WIDTH()//2),
                             (self.__WINDOW.getVirtualHeight()-self.__START.GET_HEIGHT()-120))

        self.__DEATH_TEXT = Text("Press Space to continue!")
        self.__DEATH_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__DEATH_TEXT.GET_WIDTH()//2),-1000) # -1000 puts it out of the screen

        self.__GAMEOVER_TEXT = Text("GAME OVER",SIZE=50)
        self.__GAMEOVER_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__GAMEOVER_TEXT.GET_WIDTH()//2),-1000)

        self.__WINNING_TEXT = Text("WINNER",SIZE=100)
        self.__WINNING_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__WINNING_TEXT.GET_WIDTH()//2),-1000)

        self.__STARTING_TEXT = Text("BRICK BREAKER",SIZE=100)
        self.__STARTING_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__STARTING_TEXT.GET_WIDTH()//2),
                                    (self.__WINDOW.getVirtualHeight()//2-self.__STARTING_TEXT.GET_HEIGHT()//2-50))

        self.__START_TEXT = Text("START",SIZE=50)
        self.__START_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//4-self.__START_TEXT.GET_WIDTH()//2),
                                 (self.__WINDOW.getVirtualHeight()//2+150))

        self.__SETTINGS = Text("SETTINGS",SIZE=50)
        self.__SETTINGS.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__SETTINGS.GET_WIDTH()//2),
                               (self.__WINDOW.getVirtualHeight()//2+150))

        self.__EXIT_TEXT = Text("EXIT",SIZE=50)
        self.__EXIT_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//4*3-self.__EXIT_TEXT.GET_WIDTH()//2),
                                (self.__WINDOW.getVirtualHeight()//2+150))

        self.__PAUSE_TEXT = Text("PAUSED",SIZE=100)
        self.__PAUSE_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__PAUSE_TEXT.GET_WIDTH()//2),
                                (self.__WINDOW.getVirtualHeight()//2+100-1000))

        self.__HEALTH_TEXT = Text("HEALTH",SIZE=30)
        self.__HEALTH_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2-175),
                                  (self.__WINDOW.getVirtualHeight()//2-self.__HEALTH_TEXT.GET_HEIGHT()//2))
        self.__HEALTH_TEXT.addY(-1000)
        
        self.__RESET_TEXT = Text("Press ESC to return to Main Menu",SIZE=30)
        self.__RESET_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__RESET_TEXT.GET_WIDTH()//2),
                                 (self.__WINDOW.getVirtualHeight()//2+200-1000))

        self.__RIGHTARROW = Text(">",SIZE=30)
        self.__RIGHTARROW.setPOS((self.__WINDOW.getVirtualWidth()//2+self.__RIGHTARROW.GET_WIDTH()-30),
                                 (self.__WINDOW.getVirtualHeight()//2-self.__RIGHTARROW.GET_HEIGHT()//2))

        self.__LEFTARROW = Text("<",SIZE=30)
        self.__LEFTARROW.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__RIGHTARROW.GET_WIDTH()-30),
                                (self.__WINDOW.getVirtualHeight()//2-self.__RIGHTARROW.GET_HEIGHT()//2))

        self.__SOUND_TEXT = Text("SOUND",SIZE=30)
        self.__SOUND_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2-175),
                                 (self.__WINDOW.getVirtualHeight()//2-self.__SOUND_TEXT.GET_HEIGHT()//2+5+self.__SOUND_TEXT.GET_HEIGHT()))

        self.__OFF_TEXT = Text("OFF",SIZE=26)
        self.__OFF_TEXT.setX(self.__WINDOW.getVirtualWidth()//2+55)
        if SOUND:
            self.__OFF_TEXT.setY(self.__WINDOW.getVirtualHeight()//2-self.__OFF_TEXT.GET_HEIGHT()//2-self.__OFF_TEXT.GET_HEIGHT())
        else:
            self.__OFF_TEXT.setY(self.__WINDOW.getVirtualHeight()//2-self.__OFF_TEXT.GET_HEIGHT()//2)

        self.__ON_TEXT = Text("ON",SIZE=26)
        self.__ON_TEXT.setPOS((self.__WINDOW.getVirtualWidth()//2+55),
                              (self.__OFF_TEXT.GET_Y()+self.__OFF_TEXT.GET_HEIGHT()+5))

        self.__BOTTOMRIGHT_TEXT = Text("Controls: WASD to move, ESC to pause, SPACE to choose",SIZE=10) # A manipulated tiny text attribute for the bottom right
        self.__BOTTOMRIGHT_TEXT.setPOS((self.__WINDOW.getVirtualWidth()-self.__BOTTOMRIGHT_TEXT.GET_WIDTH()),
                                       (self.__WINDOW.getVirtualHeight()-self.__BOTTOMRIGHT_TEXT.GET_HEIGHT()))

## --- Main Attributes
        self.__PADDLE = Paddle()
        self.__PADDLE.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__PADDLE.GET_WIDTH()//2),
                             (self.__WINDOW.getVirtualHeight()-self.__PADDLE.GET_HEIGHT()-30))

        self.__TOP_BAR = TopBar(self.__WINDOW.getVirtualWidth())

        self.__HEALTH = HEALTH
        self.__HEALTH_POINTS = []
        for i in range(self.__HEALTH):
            self.__HEALTH_POINTS.append(ImageSprite("assets/Heart.png")) # Personally drawn hearts :))
            self.__HEALTH_POINTS[i].setScale(1.5)
            self.__HEALTH_POINTS[i].setX(self.__WINDOW.getVirtualWidth()-self.__HEALTH_POINTS[i].GET_WIDTH()*(i+1))
            self.__HEALTH_POINTS[i].addY(self.__TOP_BAR.GET_HEIGHT()//2-self.__HEALTH_POINTS[i].GET_HEIGHT()//2)

        self.__HEALTHNUMBERS = []
        for i in range(10):
            self.__HEALTHNUMBERS.append(Text(f"{i+1}",SIZE=26))
            self.__HEALTHNUMBERS[i].setPOS(self.__WINDOW.getVirtualWidth()//2-self.__HEALTHNUMBERS[i].GET_WIDTH()//2+60,
                                    (i*self.__HEALTHNUMBERS[i].GET_HEIGHT()+3+self.__WINDOW.getVirtualHeight()//2-self.__HEALTHNUMBERS[i].GET_HEIGHT()//2)-((self.__HEALTH-1)*(self.__HEALTHNUMBERS[i].GET_HEIGHT()))) # Makes sure the hearts are right beside each other

        self.__BRICKS = []
        for i in range(6): # row
            for j in range(6): # collumn
                self.__BRICKS.append(Brick(j*135+130+(15*checkEven(i)),i*55+95))
                # (row * (width of the brick + distance inbetween bricks)) + (distance from wall) + (15 * -1/1 (odd/even)), (collumn * (height of the brick + distance inbetween bricks)) + (distance from ceiling  )

        self.__BALL = Ball()
        self.__OGBALLXSPEED = self.__BALL.GET_XSPEED()
        self.__BALL.setPOS((self.__WINDOW.getVirtualWidth()//2-self.__BALL.GET_WIDTH()//2),
                           (self.__WINDOW.getVirtualHeight()-self.__BALL.GET_HEIGHT()-80))
        if CoinFlip(2): # Make the ball either go left or right based on a coin flip
            self.__BALL.flipXSpeed()

# --- Functions/Modifiers --- #
    def __getSpriteCollision(self,SPRITE1,SPRITE2):
        """Checks if 2 sprites collide or not

        Args:
            SPRITE1 (OBJ): SPRITE1
            SPRITE2 (OBJ): SPRITE2

        Returns:
            BOOL: If its a hit, returns true, vice versa
        """
        if (SPRITE2.GET_X() >= SPRITE1.GET_X() - SPRITE2.GET_WIDTH() 
        and SPRITE2.GET_X() <= SPRITE1.GET_X() + SPRITE1.GET_WIDTH() 
        and SPRITE2.GET_Y() >= SPRITE1.GET_Y() - SPRITE2.GET_HEIGHT()
        and SPRITE2.GET_Y() <= SPRITE1.GET_Y() + SPRITE1.GET_HEIGHT()):
            return True
        else:
            return False

    def __blitObj(self):
        """Blits all of the objects that are needed for a specific section of the game
        """
        self.__WINDOW.CLEAR_SCREEN()
        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE}")
        self.__WINDOW.GET_SCREEN().blit(self.__WINNING_TEXT.GET_SCREEN(),self.__WINNING_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__START.GET_SCREEN(),self.__START.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__DEATH_TEXT.GET_SCREEN(),self.__DEATH_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__BALL.GET_SCREEN(),self.__BALL.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__PADDLE.GET_SCREEN(), self.__PADDLE.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__TOP_BAR.GET_SCREEN(),self.__TOP_BAR.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__SCORE_TEXT.GET_SCREEN(),self.__SCORE_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__GAME_TITLE.GET_SCREEN(),self.__GAME_TITLE.GET_POS())
        for bricks in self.__BRICKS:
            self.__WINDOW.GET_SCREEN().blit(bricks.GET_SCREEN(),bricks.GET_POS())
        for healthPoints in self.__HEALTH_POINTS:
            self.__WINDOW.GET_SCREEN().blit(healthPoints.GET_SCREEN(),healthPoints.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__GAMEOVER_TEXT.GET_SCREEN(),self.__GAMEOVER_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__PAUSE_TEXT.GET_SCREEN(),self.__PAUSE_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__RESET_TEXT.GET_SCREEN(),self.__RESET_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__BOTTOMRIGHT_TEXT.GET_SCREEN(),self.__BOTTOMRIGHT_TEXT.GET_POS())

    def __blitStartObj(self):
        """Blits all of the objects that are needed for the start screen section of the game
        """
        self.__WINDOW.CLEAR_SCREEN()
        self.__WINDOW.GET_SCREEN().blit(self.__BOTTOMRIGHT_TEXT.GET_SCREEN(),self.__BOTTOMRIGHT_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__TOP_BAR.GET_SCREEN(),self.__TOP_BAR.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__STARTING_TEXT.GET_SCREEN(),self.__STARTING_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__START_TEXT.GET_SCREEN(),self.__START_TEXT.GET_POS())        
        self.__WINDOW.GET_SCREEN().blit(self.__SETTINGS.GET_SCREEN(),self.__SETTINGS.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__EXIT_TEXT.GET_SCREEN(),self.__EXIT_TEXT.GET_POS())

    def __blitSetObj(self,CHOICE=1):
        """Blits all of the objects that are needed for the setting section of the game

        Args:
            CHOICE (int, optional): information on what subsetting is needed to be blitted. Defaults to 1.
        """
        self.__WINDOW.CLEAR_SCREEN()
        self.__WINDOW.GET_SCREEN().blit(self.__RIGHTARROW.GET_SCREEN(),self.__RIGHTARROW.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__LEFTARROW.GET_SCREEN(),self.__LEFTARROW.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__HEALTH_TEXT.GET_SCREEN(),self.__HEALTH_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__SOUND_TEXT.GET_SCREEN(),self.__SOUND_TEXT.GET_POS())
        self.__WINDOW.GET_SCREEN().blit(self.__BOTTOMRIGHT_TEXT.GET_SCREEN(),self.__BOTTOMRIGHT_TEXT.GET_POS())
        if CHOICE == 1:
            for number in self.__HEALTHNUMBERS:
                self.__WINDOW.GET_SCREEN().blit(number.GET_SCREEN(),number.GET_POS())
        if CHOICE == 2:
            self.__WINDOW.GET_SCREEN().blit(self.__OFF_TEXT.GET_SCREEN(),self.__OFF_TEXT.GET_POS())
            self.__WINDOW.GET_SCREEN().blit(self.__ON_TEXT.GET_SCREEN(),self.__ON_TEXT.GET_POS())

    def __checkExit(self):
        """checks if pygame closes or not
        """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def __ballDir(self):
        """Sets the ball going in the same direction as the paddle
        """
        if pygame.key.get_pressed()[pygame.K_d] == 1:
                    if self.__BALL.GET_XSPEED() < 0:
                        self.__BALL.setXSpeed(self.__BALL.GET_XSPEED()*-1)
        if pygame.key.get_pressed()[pygame.K_a] == 1:
                    if self.__BALL.GET_XSPEED() > 0:
                        self.__BALL.setXSpeed(self.__BALL.GET_XSPEED()*-1)

# --- Expiremental --- #
    def __playSound(self,SOUND): # Has some issues that are explained in the README file
        if self.__SOUND:
            #if SOUND == 1:
                #playsound("assets/1blipSelect.mp3")
            if SOUND == 2:
                playsound("assets/2blipSelect2.mp3")
            if SOUND == 3:
                playsound("assets/3death.mp3")
            if SOUND == 4:
                playsound("assets/4brickBreak.mp3")
            if SOUND == 5:
                playsound("assets/5bounce.mp3")     

            """if SOUND == 1:
                pygame.mixer.Sound("assets/1blipSelect.mp3").play()
            if SOUND == 2:
                pygame.mixer.Sound("assets/2blipSelect2.mp3").play()
            if SOUND == 3:
                pygame.mixer.Sound("assets/3death.mp3").play()
            if SOUND == 4:
                pygame.mixer.Sound("assets/4brickBreak.mp3").play()
            if SOUND == 5:
                pygame.mixer.Sound("assets/5bounce.mp3").play()"""

    def Run(self):
        """The main function of the game that pulls everything together
        """
## --- Variables I used for the game
        LOOP = False
        DIED = False      
        TODEATH = False 
        GAMEOVER = False
        FLASH = 0 # the variable that allows for the objects to appear to blink
        NEXTLEVEL = False
        LEVEL = 1 
        STARTSCREEN = True
        PAUSE = False
        PAUSEGAP = 0 # Variable that stops the game from checking for input every frame, which makes pressing button hard
        CHOICE = self.__START_TEXT 
        STARTCHOICE = 1
        SETTINGS = False
        GAME = True
        RESET = False
        
# --- Starting Screen --- #        
        while STARTSCREEN:
            self.__checkExit()
            self.__blitStartObj()
            self.__WINDOW.UPDATE_FRAME()
    ## --- Variables that I use for the START SCREEN 
            HPSUBCHOICE = self.__HEALTH # makes sure that the HP is the same even after reseting
            VOLSUBCHOICE = self.__SOUND # makes sure that the VOLUME
            PAUSEGAP += 1
            if pygame.key.get_pressed()[pygame.K_d] == 1 and STARTCHOICE < 3 and PAUSEGAP >= 10: # Checks for a d key input
                STARTCHOICE += 1
                self.__playSound(1)
                PAUSEGAP = 0
                if CHOICE.GET_Y() < 0:
                    CHOICE.addY(1000) # Moves obj out of the screen
            if pygame.key.get_pressed()[pygame.K_a] == 1 and STARTCHOICE > 1 and PAUSEGAP >= 10: # Checks for an a key input
                STARTCHOICE -= 1
                self.__playSound(1)
                PAUSEGAP = 0
                if CHOICE.GET_Y() < 0:
                    CHOICE.addY(1000) # Moves obj out of the screen
    ## -- chooses the text that blinks
            if STARTCHOICE == 1:
                CHOICE = self.__START_TEXT
            if STARTCHOICE == 2:
                CHOICE = self.__SETTINGS
            if STARTCHOICE == 3:
                CHOICE = self.__EXIT_TEXT
    ## -- Makes the text blink
            FLASH+=1
            if FLASH > 15:
                if CHOICE.GET_Y() > 0:
                    CHOICE.addY(-1000)
                else:
                    CHOICE.addY(1000)
                FLASH = 0

            if pygame.key.get_pressed()[pygame.K_SPACE] == 1: # Checks for a space key input
                self.__playSound(2)
                if STARTCHOICE == 1: # Starts the game
                    STARTSCREEN = False
                    PAUSEGAP = 0
                    self.__BOTTOMRIGHT_TEXT.setText("")
                    self.__BOTTOMRIGHT_TEXT.setX(self.__WINDOW.getVirtualWidth()-self.__BOTTOMRIGHT_TEXT.GET_WIDTH())
                if STARTCHOICE == 2: # Goes into the settings
                    self.__BOTTOMRIGHT_TEXT.setText("*Sound is WIP, WASD to move, ESC to apply")
                    self.__BOTTOMRIGHT_TEXT.setX(self.__WINDOW.getVirtualWidth()-self.__BOTTOMRIGHT_TEXT.GET_WIDTH())
                    SETTINGS = True
                    self.__HEALTH_TEXT.addY(1000)
                    SETTINGCHOICE = 1
                    SETHEIGHT = 0
                    SUBCHOICE = False
                    if VOLSUBCHOICE == False:
                        VOLSUBCHOICE = 2
                    else:
                        VOLSUBCHOICE = 1

                    while SETTINGS: # the looping for the setting
                        self.__checkExit()
                        PAUSEGAP += 1
                        if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1: # Checks for an escape key input 
                            self.__playSound(2)
                            if VOLSUBCHOICE == 1: 
                                VOLSUBCHOICE = True
                            else:
                                VOLSUBCHOICE = False
                            self.__resetGame(HPSUBCHOICE,VOLSUBCHOICE) # makes sure the setting stays the same
                            SETTINGS = False

                        if pygame.key.get_pressed()[pygame.K_s] == 1 and SETTINGCHOICE < 2 and PAUSEGAP >= 5: # Checks for a s key input
                            SETTINGCHOICE += 1
                            self.__playSound(1) 
                            PAUSEGAP = 0
                            CURRENT = self.__SOUND_TEXT.GET_Y()
                            SETHEIGHT = self.__SOUND_TEXT.GET_HEIGHT()+5
                            while self.__SOUND_TEXT.GET_Y() > CURRENT - SETHEIGHT: # animation part of the setting
                                self.__SOUND_TEXT.addY(-5)
                                self.__HEALTH_TEXT.addY(-5)
                                self.__WINDOW.UPDATE_FRAME()
                                self.__blitSetObj(SETTINGCHOICE)
                        
                        if pygame.key.get_pressed()[pygame.K_w] == 1 and SETTINGCHOICE > 1 and PAUSEGAP >= 5: # Checks for a w key input
                            SETTINGCHOICE -= 1
                            self.__playSound(1)
                            PAUSEGAP = 0
                            CURRENT = self.__SOUND_TEXT.GET_Y()
                            SETHEIGHT = self.__SOUND_TEXT.GET_HEIGHT()+5
                            while self.__SOUND_TEXT.GET_Y() < CURRENT + SETHEIGHT: # animation part of the setting
                                self.__SOUND_TEXT.addY(5)
                                self.__HEALTH_TEXT.addY(5)
                                self.__WINDOW.UPDATE_FRAME()
                                self.__blitSetObj(SETTINGCHOICE)
                        
                        if pygame.key.get_pressed()[pygame.K_d] == 1 and PAUSEGAP >= 5: # Checks for a d key input
                            PAUSEGAP = 0
                            self.__playSound(2)
                            PAUSEGAP = 0
                            CURRENT = self.__RIGHTARROW.GET_X()
                            while self.__RIGHTARROW.GET_X() < CURRENT + 35:
                                self.__RIGHTARROW.addX(5)
                                self.__LEFTARROW.addX(5)
                                self.__WINDOW.UPDATE_FRAME()
                                self.__blitSetObj(SETTINGCHOICE)
                            SUBCHOICE = True
                            
                            while SUBCHOICE:
                                PAUSEGAP += 1
                                self.__checkExit()
                                
                                if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1 and PAUSEGAP >= 10: # Checks for an escape key input
                                    PAUSEGAP = 0
                                    self.__playSound(2)
                                    if VOLSUBCHOICE == 1: # Changes the variable to a boolian which works for the game class initiate
                                        VOLSUBCHOICE = True
                                    else:
                                        VOLSUBCHOICE = False
                                    SETTINGS = False
                                    SUBCHOICE = False
                                    self.__resetGame(HPSUBCHOICE,VOLSUBCHOICE)

                                if pygame.key.get_pressed()[pygame.K_a] == 1 and PAUSEGAP >= 10: # Checks for an a key input
                                    PAUSEGAP = 0
                                    self.__playSound(2)
                                    CURRENT = self.__RIGHTARROW.GET_X()
                                    while self.__RIGHTARROW.GET_X() > CURRENT - 35: 
                                        self.__RIGHTARROW.addX(-5)
                                        self.__LEFTARROW.addX(-5)
                                        self.__WINDOW.UPDATE_FRAME()
                                        self.__blitSetObj(SETTINGCHOICE)
                                        SUBCHOICE = False
                                    break

                                if pygame.key.get_pressed()[pygame.K_s] == 1 and PAUSEGAP >= 2: # Checks for a s key input
                                    PAUSEGAP = 0
                                    self.__playSound(1)
                                    if SETTINGCHOICE == 1 and HPSUBCHOICE < 10:
                                        CURRENT = self.__HEALTHNUMBERS[HPSUBCHOICE-1].GET_Y()
                                        HPSUBCHOICE += 1  
                                        while self.__HEALTHNUMBERS[HPSUBCHOICE-1].GET_Y() > CURRENT:
                                            for num in self.__HEALTHNUMBERS:
                                                num.addY(-5) 
                                            self.__blitSetObj(SETTINGCHOICE)
                                            self.__WINDOW.UPDATE_FRAME() 

                                    if SETTINGCHOICE == 2 and VOLSUBCHOICE > 1: 
                                        VOLSUBCHOICE -= 1
                                        CURRENT = self.__OFF_TEXT.GET_Y() 
                                        SETHEIGHT = self.__OFF_TEXT.GET_HEIGHT()+5
                                        while self.__OFF_TEXT.GET_Y() > CURRENT - SETHEIGHT:  # Animation
                                            self.__OFF_TEXT.addY(-5)
                                            self.__ON_TEXT.addY(-5)
                                            self.__WINDOW.UPDATE_FRAME()
                                            self.__blitSetObj(SETTINGCHOICE)
                                
                                if pygame.key.get_pressed()[pygame.K_w] == 1 and PAUSEGAP >= 2: # Checks for a w key input
                                    PAUSEGAP = 0
                                    self.__playSound(1)
                                    if SETTINGCHOICE == 1 and HPSUBCHOICE > 1:
                                        CURRENT = self.__HEALTHNUMBERS[HPSUBCHOICE-1].GET_Y()
                                        HPSUBCHOICE -= 1
                                        while self.__HEALTHNUMBERS[HPSUBCHOICE-1].GET_Y() < CURRENT:
                                            for num in self.__HEALTHNUMBERS:
                                                num.addY(5)
                                            self.__blitSetObj(SETTINGCHOICE)
                                            self.__WINDOW.UPDATE_FRAME()

                                    if SETTINGCHOICE == 2 and VOLSUBCHOICE < 2:
                                        VOLSUBCHOICE += 1
                                        CURRENT = self.__OFF_TEXT.GET_Y()
                                        SETHEIGHT = self.__OFF_TEXT.GET_HEIGHT()+5
                                        while self.__OFF_TEXT.GET_Y() < CURRENT + SETHEIGHT: # Animation
                                            self.__OFF_TEXT.addY(5)
                                            self.__ON_TEXT.addY(5)
                                            self.__WINDOW.UPDATE_FRAME()
                                            self.__blitSetObj(SETTINGCHOICE)

                                self.__blitSetObj(SETTINGCHOICE)
                                self.__WINDOW.UPDATE_FRAME()

                        self.__blitSetObj(SETTINGCHOICE)
                        self.__WINDOW.UPDATE_FRAME()
                if STARTCHOICE == 3: # Exits the game
                    exit()

# --- The Main Part of the game --- #
        while GAME:
            self.__checkExit()
            self.__blitObj()
            PAUSEGAP += 1
            if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1 and PAUSEGAP >= 10 and LOOP: # Checks for an escape key input and makes sure the game is looping
                self.__playSound(2)
                PAUSE = True
                self.__PAUSE_TEXT.addY(1000) # puts the pause text into the screen   
                self.__RESET_TEXT.addY(1000) # puts the rest text into the screen
                PAUSEGAP = 0
                self.__BOTTOMRIGHT_TEXT.setText("ESC to leave, SPACE to continue")
                self.__BOTTOMRIGHT_TEXT.setX(self.__WINDOW.getVirtualWidth()-self.__BOTTOMRIGHT_TEXT.GET_WIDTH())
            while PAUSE:
                self.__checkExit()
                FLASH+=1
                if FLASH > 20: # Makes the text blink
                    if self.__PAUSE_TEXT.GET_Y() > 0: 
                        self.__PAUSE_TEXT.addY(-1000)
                    else:
                        self.__PAUSE_TEXT.addY(1000)
                    FLASH = 0
                self.__blitObj()
                self.__WINDOW.UPDATE_FRAME()
                PAUSEGAP += 1
                if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1 and PAUSEGAP >= 10: # Checks for an escape key input 
                    self.__playSound(3)
                    GAME = False
                    RESET = True
                    PAUSE = False

                if pygame.key.get_pressed()[pygame.K_SPACE] == 1 and PAUSEGAP >= 10: # Checks for a space key input
                    self.__playSound(2)
                    PAUSE = False
                    PAUSEGAP = 0
                    if self.__PAUSE_TEXT.GET_Y() > 0:
                        self.__PAUSE_TEXT.addY(-1000)
                    self.__RESET_TEXT.addY(-1000)

            if RESET: # Checks if the game is going to reset
                self.__resetGame(HPSUBCHOICE,VOLSUBCHOICE)
                break

            if LOOP == False: # Allows for you to move the paddle around before the game starts
                self.__BALL.setX((self.__PADDLE.GET_X())+(self.__PADDLE.GET_WIDTH()//2)-(self.__BALL.GET_WIDTH()//2)) # keeps the ball right above the paddle
                self.__START.setX((self.__PADDLE.GET_X())+(self.__PADDLE.GET_WIDTH()//2)-(self.__START.GET_WIDTH()//2))
                self.__PADDLE.adMove(pygame.key.get_pressed())
                self.__ballDir()

            if pygame.key.get_pressed()[pygame.K_SPACE] == 1 and PAUSEGAP >= 10: # Checks for a space key input
                if LOOP == False or PAUSE == True:
                    self.__playSound(5)
                PAUSEGAP = 0
                LOOP = True # Makes the game start running
                self.__START.setPOS(-1000,-1000) # Sends the START text out of the screen

# --- Main part of the code that runs brick breaker itself --- #
            if LOOP:
                self.__PADDLE.adMove(pygame.key.get_pressed()) # Paddle movement
                
# --- Collisions part of the code --- #
                if DIED == False:
                    self.__BALL.bounceX(0,self.__WINDOW.getVirtualWidth())
                    self.__BALL.bounceY(self.__TOP_BAR.GET_HEIGHT(),self.__WINDOW.getVirtualHeight())
                    self.__BALL.addX(self.__BALL.GET_XSPEED())
                    self.__BALL.addY(self.__BALL.GET_YSPEED())
                    if self.__getSpriteCollision(self.__PADDLE,self.__BALL):
                        self.__playSound(5)
                        if self.__BALL.GET_Y() + self.__BALL.GET_HEIGHT() < self.__PADDLE.GET_Y() + 6:
                            self.__BALL.flipYSpeed()
                            if self.__BALL.GET_XSPEED() > 0:
                                self.__BALL.addXSpeed(randrange(0,1))
                            if self.__BALL.GET_XSPEED() < 0:
                                self.__BALL.addXSpeed(randrange(-1,0))
                        else:
                            if not TODEATH:
                                self.__BALL.flipXSpeed()
                                TODEATH = True
                    for brick in self.__BRICKS: # checks the collision for the bricks
                        if self.__getSpriteCollision(self.__BALL,brick):
                            self.__playSound(4)
                            self.__SCORE += 20
                            brick.addHealth(-1)
                            if self.__BALL.GET_Y() > brick.GET_Y() + brick.GET_HEIGHT() + self.__BALL.GET_YSPEED(): # bottom
                                if self.__BALL.GET_YSPEED() < 0:
                                    self.__BALL.flipYSpeed()
                            elif self.__BALL.GET_Y() + self.__BALL.GET_HEIGHT() < brick.GET_Y() + self.__BALL.GET_YSPEED(): # top
                                if self.__BALL.GET_YSPEED() > 0:
                                    self.__BALL.flipYSpeed()
                            
                            elif self.__BALL.GET_XSPEED() < 0: # right
                                    self.__BALL.flipXSpeed()
                            elif self.__BALL.GET_XSPEED() > 0: # left
                                self.__BALL.flipXSpeed()
                            
                            if brick.getHealth() == 1: # Changes the color of the brick from green to white to signify its health
                                brick.setColor((255,255,255))

                            if brick.getHealth() <= 0: # Sends the brick out of the screen once its health is depleted
                                brick.addY(-1000)

# --- Score checking Code --- #
            if self.__SCORE >= 720 and LEVEL == 1: # sends the player to the next level if they have reached the requirements
                NEXTLEVEL = True
                LEVEL = 2
                for brick in self.__BRICKS:
                    brick.addY(1000)
                    brick.addHealth(2)
                    brick.setColor((50,255,50)) # changes the color to darkish green

            if self.__SCORE  >= 2160: # checks if the player has won or not
                self.__WINNING_TEXT.setY(self.__WINDOW.getVirtualHeight()//2-self.__WINNING_TEXT.GET_HEIGHT()//2)
                self.__BOTTOMRIGHT_TEXT.setText("Press ESC to return to the Main Menu")
                self.__BOTTOMRIGHT_TEXT.setX(self.__WINDOW.getVirtualWidth()-self.__BOTTOMRIGHT_TEXT.GET_WIDTH()) # mini instructions
            while self.__SCORE >= 2160:
                self.__checkExit()
                self.__PADDLE.adMove(pygame.key.get_pressed()) # allows for paddle movement
                self.__PADDLE.checkBoundaries(self.__WINDOW.getVirtualWidth(),self.__WINDOW.getVirtualHeight()) 
                FLASH+=1 
                if FLASH > 10: # Makes the text blink
                    if self.__WINNING_TEXT.GET_Y() > 0:
                        self.__WINNING_TEXT.addY(-1000)
                    else:
                        self.__WINNING_TEXT.addY(1000)
                    FLASH = 0

                if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1: # Checks for an escape key input
                    self.__playSound(2)
                    self.__resetGame(HPSUBCHOICE,VOLSUBCHOICE)
                
                self.__blitObj()
                self.__WINDOW.UPDATE_FRAME()

            while NEXTLEVEL: # Goes to the next level
                self.__checkExit()
                self.__PADDLE.adMove(pygame.key.get_pressed())
                self.__PADDLE.checkBoundaries(self.__WINDOW.getVirtualWidth(),self.__WINDOW.getVirtualHeight())
                self.__BALL.setPOS((self.__PADDLE.GET_X())+(self.__PADDLE.GET_WIDTH()//2)-(self.__BALL.GET_WIDTH()//2),
                                       (self.__WINDOW.getVirtualHeight()-self.__BALL.GET_HEIGHT()-80)) # Makes sure the ball is right above the paddle
                self.__DEATH_TEXT.setPOS((self.__PADDLE.GET_X())+(self.__PADDLE.GET_WIDTH()//2)-(self.__DEATH_TEXT.GET_WIDTH()//2),
                                         (self.__WINDOW.getVirtualHeight()-self.__START.GET_HEIGHT()-120))

                self.__ballDir() # Makes sure the ball goes in the direction of the paddle

                if pygame.key.get_pressed()[pygame.K_SPACE] == 1: # Checks for a space key input
                    NEXTLEVEL = False # Begins the next level
                    self.__DEATH_TEXT.setY(-1000)

                self.__blitObj()
                self.__WINDOW.UPDATE_FRAME()

# --- Checks for if the ball goes out of bounds --- #
            if self.__BALL.GET_Y() >= self.__WINDOW.getVirtualHeight()-self.__BALL.GET_HEIGHT(): # if the ball is below the screen
                self.__playSound(3)
                self.__BALL.setXSpeed(self.__OGBALLXSPEED)
                self.__HEALTH -= 1 # Gets rid of a life
                if self.__HEALTH == 0: # Checks if you have run out of lives yet
                    LOOP = False # stop the game
                    GAMEOVER = True # Game lost
                self.__HEALTH_POINTS[self.__HEALTH].setY(-100)
                self.__BALL.flipYSpeed()
                if GAMEOVER == False: # Game lost
                    self.__DEATH_TEXT.setPOS((self.__PADDLE.GET_X())+(self.__PADDLE.GET_WIDTH()//2)-(self.__DEATH_TEXT.GET_WIDTH()//2),
                                         (self.__WINDOW.getVirtualHeight()-self.__START.GET_HEIGHT()-120))
                DIED = True

# --- The loop that deals with death --- #
                while DIED:
                    self.__checkExit()
                    self.__PADDLE.adMove(pygame.key.get_pressed())
                    self.__PADDLE.checkBoundaries(self.__WINDOW.getVirtualWidth(),self.__WINDOW.getVirtualHeight())
                    self.__DEATH_TEXT.setX((self.__PADDLE.GET_X())+(self.__PADDLE.GET_WIDTH()//2)-(self.__DEATH_TEXT.GET_WIDTH()//2))
                    self.__ballDir()
                    if pygame.key.get_pressed()[pygame.K_SPACE] == 1 and GAMEOVER == False: # Checks for a space key input
                        self.__playSound(5)
                        self.__DEATH_TEXT.setY(-1000)
                        DIED = False
                        TODEATH = False
                    if GAMEOVER == False: 
                        self.__BALL.setPOS((self.__PADDLE.GET_X())+(self.__PADDLE.GET_WIDTH()//2)-(self.__BALL.GET_WIDTH()//2),
                                       (self.__WINDOW.getVirtualHeight()-self.__BALL.GET_HEIGHT()-80))
                    else: # If the player is out of health the game is over
                        DIED = False
                        TODEATH = False
                        self.__BALL.setY(-1000)
                        self.__RESET_TEXT.addY(1000)
                   
                    self.__blitObj()
                    self.__WINDOW.UPDATE_FRAME()

# --- GAME OVER LOOP --- #
            while GAMEOVER:
                self.__checkExit()
                FLASH+=1
                if FLASH > 10:
                    if self.__GAMEOVER_TEXT.GET_Y() > 0:
                        self.__GAMEOVER_TEXT.setY(-1000)
                    else:
                        self.__GAMEOVER_TEXT.setY(self.__WINDOW.getVirtualHeight()-300)
                    FLASH = 0
                
                if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1: # Checks for an escape key input to restart the game
                    self.__playSound(3)
                    GAME = False
                    RESET = True
                    GAMEOVER = False

                self.__blitObj()
                self.__WINDOW.UPDATE_FRAME()      
                       
            self.__PADDLE.checkBoundaries(self.__WINDOW.getVirtualWidth(), self.__WINDOW.getVirtualHeight()) # Makes sure that the paddle is not leaving the screen
            self.__WINDOW.UPDATE_FRAME()

def checkEven(NUM):
    """Checks if the number is even or not

    Args:
        NUM (INT): The integer that is entered into the function

    Returns:
        INT: 1 if its even, -1 if its odd
    """
    if NUM^1 == NUM+1:
        return 1
    else:
        return -1

def CoinFlip(OUTOF):
    """returns a True or False based on a 1 out of 2 chance

    Args:
        OUTOF (INT): the denominator

    Returns:
        BOOL: True if you hit the odds, False if you did not
    """
    VALUE = randrange(1,OUTOF)
    if VALUE == 1:
        return True
    else: 
        return False

if __name__ == "__main__":
    GAME = Game()
    while True:
        GAME.Run()