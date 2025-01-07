# topbar.py

'''
Title: Topbar Class
Author: Jako
Date-created: April 16, 2022
'''

from my_sprite import MySprite

class TopBar(MySprite):
    """Pretty sure I didn't need to make this but, the class for the bar at the top of the screen

    Args:
        MySprite (OBJ): The parent class
    """
    def __init__(self,WIDTH=0):
        super().__init__(WIDTH,40,0,0,COLOR=(20,20,20))

