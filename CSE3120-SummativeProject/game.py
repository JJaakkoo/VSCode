# game.py
'''
Title: Game class
Author: Jako
Date-created: March 14, 2022
'''

from sys import exit
from basicFunctions import checkInt, checkYN, getBasicInput
from player import Player

class Game:
    """The game class
    """
    def setUp(self): # Welcomes the player
        print("Welcome to Jako's Pirate Game!")
        print('''Rules:
1. The ship must be found first
2. The Captain is then commissioned next
3. The Captain will then approve the crew
4. If you have enough coins you can shoot a cannon at another player
5. When the ship, Captain and crew are assembled, they can look for loot!
''')

    def __init__(self): # Initiates the class, and adds the variables
        self.PLAYERS = []
        self.MAXPLAYERS = 0
        self.WINCON = 20 # The amount of coins needed to win the game
        self.REPEAT = True
        self.LOOP = True
        self.FOUNDCOINS = 0

    def gameReset(self): # resets all the changed variables of the game
        self.PLAYERS = []
        self.MAXPLAYERS = 0
        self.REPEAT = True
        self.LOOP = True
        self.FOUNDCOINS = 0

    def addPlayers(self): # adds the amount of players to the game plus their names
        print("How many players are playing? (2-10 Players)")
        self.MAXPLAYERS = checkInt(getBasicInput(),2,10)
        for i in range(self.MAXPLAYERS):
            self.PLAYERS.append(Player())
            print(f"What is Player {i+1}'s name?") 
            self.PLAYERS[i].addName(getBasicInput()) # asks for the name
            if self.PLAYERS[i].returnName() == "":
                self.PLAYERS[i].addName(f"Player {i+1}")

# Extra feature to change the win condition of the game

    def changeWinCon(self):
        print('''Would you like to:
1. Keep the default win condition? (20 coins)
2. Or select a custom win condition? (1-100 coins)''') 
        if checkInt(getBasicInput(),1,2) == 1:
            pass
        else:
            print("What would you like to set the win condition to?")
            self.WINCON = checkInt(getBasicInput(),1,100)

                
    def run(self):
        """Gets all the functions of the player and game, and runs the game
        """
        self.setUp() # Welcomes the player
        while self.REPEAT: # Makes sure the game continues running after someone has won
            self.gameReset()
            self.addPlayers()
            self.changeWinCon() # Extra feature
            while self.LOOP: # Makes sure the player continues rolling after 3 rolls
                for i in range(self.MAXPLAYERS): 
                    if self.LOOP:
                        print(f'''
{self.PLAYERS[i].returnName()}'s Turn! Gold: {self.PLAYERS[i].returnCoins()}''')
                        self.PLAYERS[i].resetPlayer() # Resets the player
                        if self.cannonFeature(i):
                            for j in range(3):
                                if self.LOOP:
                                    self.FOUNDCOINS = 0
                                    self.PLAYERS[i].rollDice()
                                    self.PLAYERS[i].checkActiveDie(j)
                                    self.FOUNDCOINS = self.PLAYERS[i].checkDiceHeld(j)
                                    if self.FOUNDCOINS > 0: # Checks if the player has found any coins or not
                                        print(f"Would {self.PLAYERS[i].returnName()} like to collect {self.FOUNDCOINS} Coins? (Y/n) - Current Coins: {self.PLAYERS[i].returnCoins()}")
                                        if checkYN(getBasicInput()):
                                            self.PLAYERS[i].addCoins(self.FOUNDCOINS)
                                            print(f'''{self.PLAYERS[i].returnName()} now has {self.PLAYERS[i].returnCoins()} Coins!''')
                                            self.PLAYERS[i].resetPlayer()
                                            if self.PLAYERS[i].returnCoins() >= self.WINCON: # Checks if the player has enough coins to win or not
                                                self.LOOP = False
                                                print(f'''
    {self.PLAYERS[i].returnName()} won!''')
                                                print("Would you like to play again? (Y/n)")
                                                if checkYN(getBasicInput()) == False:
                                                    self.REPEAT = False
                                                    print("Thanks for playing Jako's Pirate Game!")
                                                    exit()
                                            break # breaks out of the for j in range loop to stop rolling after collecting coins
   
# --- Extra feature - Cannon Die --- #
    def cannonFeature(self,i):
        """Rolls a dice to shoot a cannon to try and rid someone of some of their coins

        Args:
            i (int): the player array number

        Returns:
            bool: returns whether or not to skip a turn
        """
        MULTIPLIER = 1
        if self.WINCON > 20: 
            MULTIPLIER = 2
        if self.WINCON > 40:
            MULTIPLIER = 3
        if self.WINCON > 60:
            MULTIPLIER = 3
        if self.WINCON > 80:
            MULTIPLIER = 4
        if self.PLAYERS[i].returnCannonCD() > 0:
            self.PLAYERS[i].addCannonCD(-1)
            print(f"Your cannon is still on cool down: {self.PLAYERS[i].returnCannonCD()+1} more turns!")
            return True

        elif self.PLAYERS[i].returnCoins() >= 3*MULTIPLIER: # Checks if the player can afford a shot or not
            print("You have enough coins to afford a shot with the cannon!")
            print(f"Would you like to spend {3*MULTIPLIER} gold and lose a turn to rid someone of {1*MULTIPLIER}-{6*MULTIPLIER} of their coins? (Y/n)")
            if checkYN(getBasicInput()): # asks if the player wants to shoot or not
                self.PLAYERS[i].setCannonCD(4)
                PHIT = None
                OTHERPLAYERS = []
                PNUM = 0
                for k in range((self.MAXPLAYERS)):
                        try:
                            if k != i:
                                PNUM += 1
                                OTHERPLAYERS.append(f"{k},{PNUM},{self.PLAYERS[k].returnName()},{self.PLAYERS[k].returnCoins()}")  # makes an array of players who arent you                              
                        except IndexError:
                            pass   
                for j in range(len(OTHERPLAYERS)):
                    OTHERPLAYERS[j] = OTHERPLAYERS[j].split(",") # fixes up the data so it is easier to manage   
                if self.MAXPLAYERS > 2: # if theres more than 1 other player
                    print("Who are you going to try and hit?")
                    for j in range(len(OTHERPLAYERS)):
                        print(f"{OTHERPLAYERS[j][1]}. {OTHERPLAYERS[j][2]}: {OTHERPLAYERS[j][3]} Coins")
                    PHIT = checkInt(getBasicInput(),1,len(OTHERPLAYERS))
                else: # if theres only 1 other player
                    PHIT = 1

                DAMAGE = 0
                for j in range(MULTIPLIER):
                    self.PLAYERS[i].rollCannonDie()    
                    DAMAGE += self.PLAYERS[i].returnCannonDie()
                    for j in range(len(OTHERPLAYERS)): # checks the player that has been chosen to be hit
                        if PHIT == int(OTHERPLAYERS[j][1]): # checks who the player selected
                            self.PLAYERS[int(OTHERPLAYERS[j][0])].addCoins(0 - (self.PLAYERS[i].returnCannonDie())) # pulls some coins off the other player
                            
                print(f"Good Job! you hit {OTHERPLAYERS[j][2]} and they lost {DAMAGE} coins!") # lets the player what has happened
                if self.PLAYERS[int(OTHERPLAYERS[j][0])].returnCoins() < 0:
                                self.PLAYERS[int(OTHERPLAYERS[j][0])].removeCoins()
                return False # skips the players turn

            else:
                return True
        return True

if __name__ == "__main__":
    GAME = Game()
    GAME.run()

