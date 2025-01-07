# a_person.py
'''
Title: Person Class
Author: Jako
date-created: March 9 2022
'''

class Person:

    def __init__(self):
        self.NAME = ""
        self.DATE = ""
        self.JOB = ""

# --- Accessor --- #

    def printInfo(self):
        print(f"{self.NAME}, {self.DATE}, {self.JOB}")

    def getName(self):
        return self.NAME

    def getDate(self):
        return self.DATE

    def getJob(self):
        return self.JOB

# --- Modifier --- #

    def addPerson(self,NAME,DATE,JOB):
        self.NAME = NAME
        self.DATE = DATE
        self.JOB = JOB

    def getInfo(self):
        NAME = input("What is the name of this person?> ")
        DATE = input("When was this person alive?> ")
        JOB = input("What was the occupation of this person?> ")
        return NAME, DATE, JOB

if __name__ == "__main__":
    PERSON = Person()
    NAME,DATE,JOB = PERSON.getInfo()
    PERSON.addPerson(NAME,DATE,JOB)

    PERSON.printInfo()

    print(PERSON.getName())
    print(PERSON.getDate())
    print(PERSON.getJob())
    
