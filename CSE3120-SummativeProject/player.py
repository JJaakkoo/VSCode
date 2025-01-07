# player.py
'''
Title: Player Class
Author: Jako
Date-created: March 11, 2022
'''

from die import Die

class Player:
    """The class that holds the player
    """
    
    def __init__(self): # The variables needed for the player
        self.ACTIVEDIE = [Die(), Die(), Die(), Die(), Die()]
        self.DICEHELD = []
        self.CANNONDIE = Die() # --- Extra feature - Cannon Die --- #
        self.CANNONCOOLDOWN = 0 

        self.CHANGE = 0 # Checks for changes in diceactive

    # Variables that make sure there is only 1 of either 6,5 or 4 in the dice held
        self.SHIPCHANGE = False
        self.CAPTAINCHANGE = False
        self.CREWCHANGE = False

        self.SHIP = True
        self.CAPTAIN = True
        self.CREW = True

        self.COINS = 0 # The coins that the player has

        self.NAME = "" # The name of the player

# --- Accessors --- #
    # Prints the Name, Coins, diceheld, and activedice
    def printName(self):
        print(self.NAME)
    
    def printCoins(self):
        print(self.COINS)
    
    def printDiceHeld(self):
        for i in range(len(self.DICEHELD)):
            print(self.DICEHELD[i])
    
    def printActiveDie(self):
        for i in range(len(self.ACTIVEDIE)):
            self.ACTIVEDIE[i].showDie()

    # Returns the Name, Coins, and Diceheld
    def returnName(self):
        return self.NAME

    def returnCoins(self):
        return self.COINS

    def returnDiceHeld(self):
        return self.DICEHELD

    def returnCannonDie(self): # --- Extra feature - Cannon Die --- #
        return self.CANNONDIE.returnDie()

    def returnCannonCD(self):
        return self.CANNONCOOLDOWN                

# --- Modifiers --- #

    def rollCannonDie(self): # --- Extra feature - Cannon Die --- #
        self.CANNONDIE.rollDie()
    
    def setCannonCD(self,VALUE):
        self.CANNONCOOLDOWN = VALUE

    def addCannonCD(self,VALUE):
        self.CANNONCOOLDOWN += VALUE

    def rollDice(self): # Rolls all 6 of the dice
        for i in range(len(self.ACTIVEDIE)):
            self.ACTIVEDIE[i].rollDie()

    # Resets Active Dice, Player, Coins, and Dice Held
    def resetActiveDie(self):
        self.ACTIVEDIE = [Die(), Die(), Die(), Die(), Die()]

    def resetPlayer(self):
        self.CHANGE = 0

        self.SHIPCHANGE = False
        self.CAPTAINCHANGE = False
        self.CREWCHANGE = False

        self.SHIP = True
        self.CAPTAIN = True
        self.CREW = True
        self.resetActiveDie()
        self.resetDiceHeld()
    
    def removeCoins(self):
        self.COINS = 0

    def resetDiceHeld(self):
        self.DICEHELD = []

    # Adds Coins and Name to the player
    def addCoins(self,ADDEDCOINS):
        self.COINS += ADDEDCOINS

    def addName(self,NAME):
        self.NAME = NAME

    def checkActiveDie(self,ROLL):
        """Checks the Active Dice for 4,5, or 6

        Args:
            ROLL (int): the roll number
        """
        for i in range(len(self.ACTIVEDIE)):
            try: # Makes sure that the program doesn't get an index error resulted from popping a die
                if self.ACTIVEDIE[i].returnDie() > 3:
                    if self.SHIP and self.ACTIVEDIE[i].returnDie() == 6: # checks if 6, and no 6 inside DICEHELD
                        self.DICEHELD.append(self.ACTIVEDIE[i].returnDie()) # Puts the die into the DICEHELD
                        self.ACTIVEDIE.pop(i) # Removes the die from ACTIVEDIE
                        self.SHIP = False # Tells the program that there is now a 6 in the DICEHELD
                        self.CHANGE = 1 # Allows for the SHIP, CAPTAIN, and CREW to stay until the end of 3 rolls                       
                        print(f"Found a Ship on roll {ROLL+1}!")
                        self.checkActiveDie(ROLL) # Checks for if there was a 5 before the 6
                    if self.CAPTAIN and self.ACTIVEDIE[i].returnDie() == 5 and self.SHIP == False: # checks if 5, and no 5 inside DICEHELD
                        self.DICEHELD.append(self.ACTIVEDIE[i].returnDie())
                        self.ACTIVEDIE.pop(i)
                        self.CAPTAIN = False
                        self.CHANGE = 2
                        print(f"Found a Captain on roll {ROLL+1}!")
                        self.checkActiveDie(ROLL) # Checks for if there was a 4 before the 5
                    if self.CREW and self.ACTIVEDIE[i].returnDie() == 4 and self.CAPTAIN == False: # checks if 4, and no 4 inside DICEHELD
                        self.DICEHELD.append(self.ACTIVEDIE[i].returnDie())
                        self.ACTIVEDIE.pop(i)
                        self.CREW = False
                        self.CHANGE = 3
                        print(f"Found a Crew on roll {ROLL+1}!")
            except IndexError:
                pass

    def checkDiceHeld(self,ROLL):
        """Checks for if the player got any coins or not

        Args:
            ROLL (int): the roll number

        Returns:
            int: the amount of coins that the player has gotten
        """
        COINS = 0
        if len(self.DICEHELD) == 3: # If the player has 6,5, and 4, it will
            for i in range(len(self.ACTIVEDIE)): # get the rest of the numbers in the ACTIVEDIE and get a coin amount
                COINS += self.ACTIVEDIE[i].returnDie()
            print(f"Found {COINS} Coins on roll {ROLL+1}!")
            return COINS
        else:
            if self.CHANGE != 0: # Checks if the player has gotten any ships, captains, or crews which leads to small extra feature
                if self.CHANGE == 1:
                    self.SHIPCHANGE = True
                elif self.CHANGE == 2:
                    self.SHIPCHANGE = True
                    self.CAPTAINCHANGE = True
                elif self.CHANGE == 3:
                    self.SHIPCHANGE = True
                    self.CAPTAINCHANGE = True
                    self.CREWCHANGE = True
                self.CHANGE = 0
            else:
                if self.SHIPCHANGE == False: # Small extra feature to show what roll the player went through
                    print(f"A ship was not found on roll {ROLL+1}!")
                elif self.CAPTAINCHANGE == False:
                    print(f"A captain was not found on roll {ROLL+1}!")
                elif self.CREWCHANGE == False:
                    print(f"A crew was not found on roll {ROLL+1}!")
        return COINS

if __name__ == "__main__":
    """PLAYER = Player()
    COINS = 0
    for i in range(3):
        if COINS == 0:
            print(f'''
COINS: {PLAYER.returnCoins()} - Roll {i+1}:''')
            PLAYER.rollDice()
            PLAYER.checkActiveDie(i)
            COINS = PLAYER.checkDiceHeld()

    PLAYER.resetPlayer()
    PLAYER.addCoins(COINS)
    PLAYER.resetActiveDie()
    PLAYER.resetDiceHeld()
    COINS = 0
    for i in range(3):
        if COINS == 0:
            print(f'''
COINS: {PLAYER.returnCoins()} - Roll {i+1}:''')
            PLAYER.rollDice()
            PLAYER.checkActiveDie(i)
            COINS = PLAYER.checkDiceHeld()

    PLAYER.addCoins(COINS)

    PLAYER.resetPlayer()
    PLAYER.resetActiveDie()
    PLAYER.resetDiceHeld()
    COINS = 0
    print(f'''
COINS: {PLAYER.returnCoins()}''')"""
    

    
