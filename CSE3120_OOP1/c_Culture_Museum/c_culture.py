# c_culture.py
'''
Title: Culture Class
Author: Jako
Date-created: March 9, 2022
'''

from a_person import Person
from b_date import Date

class Culture:

    def __init__(self):
        self.PEOPLE = []
        self.DATE = []
        self.NAME = ""


if __name__ == "__main__":
    CULT = Culture()

    CULT.PEOPLE.append(Person())

    CULT.PEOPLE[0].NAME = "John"

    print(CULT.PEOPLE[0].getName())