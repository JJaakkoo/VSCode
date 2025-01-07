# c_game.py
'''
Title: game class with Farkle
Author: Jako 
Date: March 1, 2022
'''

from b_player import Player
from a_diceroll import checkInt

class Game:

    def setup(self):
        """Where data needs to be modified to start the game
        """
        print("Welcome to Farkle")
        

    def __init__(self):
        self.PLAYER = []
        self.MAXPLAYER = 0
        
    def getMaxPlayer(self):
        self.MAXPLAYER = checkInt(input("How many players are playing?(Max 10): "),1,10)
        for i in range(self.MAXPLAYER):
            self.PLAYER.append(Player())
        return self.MAXPLAYER
        

    def run(self,MAXPLAYER):
        """Where the majority of the game will happen
        """
        LOOP = True
        while LOOP:
            for i in range(0,self.MAXPLAYER):
                # --- Player Turn --- #
                if self.PLAYER[i].SCORE < 10000:
                    print(f"Player {i+1}'s turn")
                    TURN = True
                    while TURN == True:
                        if len(self.PLAYER[i].DICE) == 0:
                            self.PLAYER[i].resetDice()
                        self.PLAYER[i].rollDice()
                        self.PLAYER[i].holdDice()

                        AGAIN = input("Roll Again? (Y/n) ")
                        if AGAIN == "" or AGAIN.upper() == "Y":
                            pass
                        else:
                            TURN = False
            

                POINTS = checkInt(input(f"Player {i+1 } Points: "),0,10000)
                self.PLAYER[i].addScore(POINTS)
                self.PLAYER[i].getScore()

                self.PLAYER[i].resetDice()
            for i in range(MAXPLAYER):
                if self.PLAYER[i].SCORE > 100000:
                    LOOP = False

# --- Main Programming Code --- #
if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    MAXPLAYER = GAME.getMaxPlayer()
    GAME.run(MAXPLAYER)