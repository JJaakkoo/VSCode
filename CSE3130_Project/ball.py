#ball.py

'''
Title: Ball Class
Author: Jako
Date-created: April 17, 2022
'''

from my_sprite import MySprite

class Ball(MySprite):
    """The ball class

    Args:
        MySprite (OBJ): The parent class
    """
    def __init__(self,X=0,Y=0):
        super().__init__(10,10,X,Y,COLOR=(255,255,255))

# --- MODIFIER METHODS --- #
    def bounceX(self, MIN_WIDTH=0, MAX_WIDTH=0):
        """Makes the ball bounce off the sides of the screen

        Args:
            MIN_WIDTH (int, optional): The measurements of the screen. Defaults to 0.
            MAX_WIDTH (int, optional): The measurements of the screen. Defaults to 0.
        """
        if self.GET_X() > MAX_WIDTH-self.GET_WIDTH():
            self.flipXSpeed()
        if self.GET_X() < MIN_WIDTH:
            self.flipXSpeed()

    def bounceY(self,MIN_HEIGHT=0,MAX_HEIGHT=0):
        """Makes the ball bounce off the top of the screen

        Args:
            MIN_HEIGHT (int, optional): The measurements of the screen. Defaults to 0.
            MAX_HEIGHT (int, optional): The measurements of the screen. Defaults to 0.
        """
        if self.GET_Y() < MIN_HEIGHT:
            self.flipYSpeed()

    def flipXSpeed(self):
        """Flips the X speed of the ball
        """
        self.setXSpeed(self.GET_XSPEED()*-1)

    def flipYSpeed(self):
        """Flips the Y speed of the ball
        """
        self.setYSpeed(self.GET_YSPEED()*-1)