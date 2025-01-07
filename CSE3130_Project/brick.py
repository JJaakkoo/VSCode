7# brick.py

'''
Title: Brick Class
Author: Jako
Date-created: April 13, 2022
'''

from my_sprite import MySprite

class Brick(MySprite):
    """The Brick class

    Args:
        MySprite (OBJ): The parent class
    """
    def __init__(self,X=0,Y=0,HEALTH=1):
        super().__init__(130,50,X,Y,COLOR=(255,255,255))
        self.__HEALTH = HEALTH

# --- ACCESSOR METHODS --- #
    def getHealth(self):
        """Returns the Health of the brick

        Returns:
            INT: The current health of the brick
        """
        return self.__HEALTH

# --- MODIFIER METHODS --- #
    def setHealth(self,HEALTH):
        """Updates the health

        Args:
            HEALTH (INT): The new value for health
        """
        self.__HEALTH = HEALTH

    def addHealth(self,HEALTH):
        """Updates the health

        Args:
            HEALTH (INT): The Value that is added to health
        """
        self.__HEALTH += HEALTH
