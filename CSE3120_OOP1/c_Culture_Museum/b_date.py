# b_date.py
'''
Title: Date Class
Author: Jako
Date-created: March 9, 2022
'''

class Date:

    def __init__(self):
        self.EVENT = ""
        self.TIME = ""

# --- Accessor --- #

    def getEvent(self):
        return self.EVENT
    
    def getTime(self):
        return self.TIME

    def printInfo(self):
        print(f"{self.EVENT}: {self.TIME}")

# --- Modifier --- #

    def addDate(self,EVENT,TIME):
        self.EVENT = EVENT
        self.TIME = TIME
        
    def getInfo(self):
        TIME = input("When was this event?> ")
        EVENT = input("What happened during this time?> ")
        return TIME,EVENT

if __name__ == "__main__":
    DATE = Date()
    TIME,EVENT = DATE.getInfo()
    DATE.addDate(EVENT,TIME)

    DATE.printInfo()

    print(DATE.getEvent())
    print(DATE.getTime())
