# f_game.py
'''
Title: Game class
Author: Jako
Date-created: March 8, 2022
'''

from d_card import Card, checkInt
from e_player import Player
from g_deck import Deck

class Game:

    def __init__(self):
        self.DECK = Deck()
        print(self.DECK.getDeck())
        self.DECK = Deck.shuffleDeck(self.DECK)
        self.PLAYER = []

    def setUp(self):
        print("Welcome to Black Jack!")

    def getMaxPlayer(self):
        self.MAXPLAYER = checkInt(input("How many players are playing?(Max 10): "),1,10)
        for i in range(self.MAXPLAYER):
            self.PLAYER.append(Player())
        return self.MAXPLAYER

    def run(self,MAXPLAYER):
        LOOP = True
        while LOOP:
            for i in range(MAXPLAYER-1):
                print("hi")
    

    def showDeck(self):
        print(self.DECK.getDeck())
            

if __name__ == "__main__":
    GAME = Game()
    GAME.setUp()
    MAXPLAYER = GAME.getMaxPlayer()
    GAME.showDeck()
