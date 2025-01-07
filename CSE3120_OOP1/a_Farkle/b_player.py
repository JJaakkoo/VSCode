# b_player.py
'''
Title: Player class for Dice Games
Author: Jako
Date: Feb 28, 2022
'''


from a_diceroll import Die, checkInt
class Player:
    """The player for a gmae of Farkle
    :attributes:
    - SCORE
    - NAME
    - DICE

    :behaviours:
    - rollDice()
    - holdDice()
    """
    def __init__(self):
        """Create a player ojbect
        """

        self.DICE = [Die(), Die(), Die(), Die(), Die(), Die()]
        self.HELD = []
        self.SCORE = 0
        self.NAME = ""

# --- Modifiers --- #

    def rollDice(self):
        """Rolls all dice in DICE
        """
        for die in self.DICE:
            die.rollNum()

    def holdDice(self):
        """User selects die to save
        """
        print("Select a die to hold")
        for i in range(len(self.DICE)):
            print(f"{i+1}. {self.DICE[i].DIE_NUM}")
        DIE = checkInt(input("> "),1,len(self.DICE))
        self.HELD.append(self.DICE.pop(DIE-1))
        for die in self.DICE:
            die.display()
        print("Dice Held: ")
        for die in self.HELD:
            die.display()

        # Ask to hold more dice
        AGAIN = input("Hold more? (Y/n): ")
        if AGAIN == "" or AGAIN.upper() == "Y":
            return self.holdDice()

    def addScore(self, POINTS):
        """adds POINTS to a player's Score

        Args:
            POINTS (int): added points
        """
        self.SCORE += POINTS

    def resetDice(self):
        """Move all dice from HELD into DICE
        """
        self.DICE += self.HELD
        self.HELD = []

# --- Accessors --- #
    def getScore(self):
        """Returns the players score
        """
        print(f"Score: {self.SCORE}")

    def getDice(self):
        """Shows us the players dice
        """
        for die in self.DICE:
            die.display()

if __name__ == "__main__":
    PLAYER = Player()
    PLAYER.rollDice()
    for die in PLAYER.DICE:
        die.display()

    PLAYER.addScore(500)
    PLAYER.addScore(200)
    PLAYER.getScore()