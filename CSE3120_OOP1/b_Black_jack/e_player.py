# e_player.py
'''
Title: Player Class
Author: Jako
Date-created: Mar 7, 2022
'''

from d_card import Card
from g_deck import Deck
class Player:

    def __init__(self):
        self.HELD = []
        self.NAME = ""