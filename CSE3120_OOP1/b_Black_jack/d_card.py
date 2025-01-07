# d_card.py
'''
Title: Card Class
Author: Jako
Date-created: March 7, 2022
'''

class Card:
    SUIT = {
        1: "Diamonds",
        2: "Clubs",
        3: "Hearts",
        4: "Spades"
    }
    
    VALUES = {
        1: "Ace",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Jack",
        10: "Queen",
        13: "King"        
    }

    def __init__(self,SUIT,VALUE):
        self.__SUIT = SUIT
        self.__VALUE = VALUE



# --- MODIFIER --- #

# --- ACCESSOR --- #

    def getCardValue(self):
        return self.__VALUE

    def getCardSuit(self):
        return self.__SUIT

    def __str__(self):
        return f"{Card.VALUES[self.__VALUE]} of {Card.SUIT[self.__SUIT]}"

def checkInt(VALUE,LOW,HIGH):
    try:
        VALUE = int(VALUE)
        if VALUE > HIGH or VALUE < LOW:
            print("This number is not an option")
            return checkInt(input("> "),LOW,HIGH)
        else:
            return VALUE
    except TypeError:
        print("This is not a number!")
        return checkInt(input("> "),LOW,HIGH)
    except ValueError:
        print("This is not a number!")
        return checkInt(input("> "),LOW,HIGH)

if __name__ == "__main__":
    CARD = Card(1,1)
    print(CARD.getCardValue())
    print(CARD.getCardSuit())

    print(CARD.__str__())