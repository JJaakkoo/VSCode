# g_deck.py
'''
Title: Deck class
Author: Jako
date-created: March 8, 2022
'''

from d_card import Card
from random import randint
from random import shuffle

class Deck:

    def __init__(self):
        self.DECK = []
        for i in range(1,5):
            for j in range(1,14):
                self.DECK.append(f"{i},{j}")

# --- MODIFIER --- #
    
    def shuffleDeck(self):
        shuffle(self.DECK)

        

# --- ACCESSOR --- #

    def getDeck(self):
        for i in range(len(self.DECK)):
            print(self.DECK[i])

if __name__ == "__main__":

    DECK = Deck()

    DECK.shuffleDeck()
    DECK.getDeck()
    
