# basicFunctions.py
'''
Title: File for basic functions
Author: Jako
Date-created: March 11, 2022
'''

from random import randint

# Small extra feature to program to prevent bugs caused by input by user

def checkInt(VALUE,LOW,HIGH):
    RUNTEST = False # For testing the game
    """Makes sure that VALUE is an integer and that it is within a range

    Args:
        VALUE (int): The value that is entered into the check
        LOW (int): the bottom part of the range
        HIGH (int): the top part of the range

    Returns:
        int: Returns a value that is within the range and is an integer
    """
    if RUNTEST:
        return randint(LOW,HIGH) # for testing only
    else:
        try:
            VALUE = int(VALUE)
            if VALUE > HIGH or VALUE < LOW:
                print(f"'{VALUE}' number is not an option")
                return checkInt(getBasicInput(),LOW,HIGH)
            else:
                return VALUE
        except TypeError:
            print(f"Error1: '{VALUE}' is not a number!")
            return checkInt(getBasicInput(),LOW,HIGH)
        except ValueError:
            print(f"Error2: '{VALUE}' is not a number!")
            return checkInt(getBasicInput(),LOW,HIGH)

def checkYN(VALUE):
    RUNTEST = False # For testing the game
    """Checks to make sure the VALUE is y, ye, yes, n, or no

    Args:
        VALUE (str): the string that is entered into the check

    Returns:
        Bool: returns either a true or a false
    """
    # For testing only
    if RUNTEST:
        RETURN = randint(1,2)
        if RETURN == 1:
            return True
        else:
            return False
    else:
        try:
            if VALUE.lower() == "y" or VALUE.lower() == "yes" or VALUE.lower() == "ye":
                return True
            if VALUE.lower() == "n" or VALUE.lower() == "no":
                return False
            else:
                print("Please enter either Y or N")
                return checkYN(getBasicInput())
        except TypeError:
            print("Please enter either Y or N")
            return checkYN(getBasicInput())
        except ValueError:
            print("Please enter either Y or N")
            return checkYN(getBasicInput())
    
def getBasicInput():
    """Gets a basic input for the other checkers and makes sure the user doesn't cause an error

    Returns:
        str: returns a string
    """
    try:
        return input("> ")
    except KeyboardInterrupt:
        print("AYO STOP THAT!")
        return getBasicInput()
    except EOFError:
        print("BAD! STOP THAT!")
        return getBasicInput()
    except TypeError:
        print("Please enter a proper value")
        return getBasicInput()
    except KeyError:
        print("Key is not found in the set of existing keys!")
        return getBasicInput()
    

if __name__ == "__main__":

    while True:
        TEST = checkInt((getBasicInput()),1,1)
        print(TEST)
        