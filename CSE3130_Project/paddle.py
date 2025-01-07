# paddle.py

'''
Title: Paddle Class
Author: Jako
Date-created: April 13, 2022
'''

from my_sprite import MySprite

class Paddle(MySprite):
    """The paddle class

    Args:
        MySprite (OBJ): The parent class
    """
    def __init__(self,X=0,Y=0):
        super().__init__(180,20,X,Y,COLOR=(255,255,255))

    
        