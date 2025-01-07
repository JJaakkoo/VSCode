#CSE3310 - Superhero Sort and Search.py

'''
title: Superhero search and sort
author: jako zeng
date-created: 2022-02-15
'''

from sys import exit

### --- sort and search functions
## merge sort functions

def mergeSort(LIST):
    """Recursive split of the list

    Args:
        LIST (list): unsorted numbers
    """
    if len(LIST) <= 1:
        return LIST
    else:
        MIDPOINT = len(LIST) // 2
        LEFT = LIST[:MIDPOINT]
        RIGHT = LIST[MIDPOINT:]
        return mergeSortedLists(mergeSort(LEFT), mergeSort(RIGHT))

def mergeSortedLists(LIST_LEFT, LIST_RIGHT):
    """merge 2 sorted lists together

    Args:
        LIST_LEFT (list): sorted numbers
        LIST_RIGHT (list): sorted numbers
    """

    if len(LIST_LEFT) == 0:
        return LIST_RIGHT
    elif len(LIST_RIGHT) == 0:
        return LIST_LEFT

    INDEX_LEFT = 0
    INDEX_RIGHT = 0
    LIST_MERGED = []
    LIST_LEN_TOTAL = (len(LIST_LEFT) + len(LIST_RIGHT))
    while len(LIST_MERGED) < LIST_LEN_TOTAL:
        if LIST_LEFT[INDEX_LEFT] <= LIST_RIGHT[INDEX_RIGHT]:
            LIST_MERGED.append(LIST_LEFT[INDEX_LEFT])
            INDEX_LEFT += 1
        else: 
            LIST_MERGED.append(LIST_RIGHT[INDEX_RIGHT])
            INDEX_RIGHT += 1

        if INDEX_RIGHT == len(LIST_RIGHT):
            LIST_MERGED = LIST_MERGED + LIST_LEFT[INDEX_LEFT:]
            break
        elif INDEX_LEFT == len(LIST_LEFT):
            LIST_MERGED = LIST_MERGED + LIST_RIGHT[INDEX_RIGHT:]
            break
    return LIST_MERGED
    
##gets the user's input of ID

def getChoice():
    """Gets the id from the user and makes sure it is an actual id

    Returns:
        string: the id that has been entered
    """
    ID = input("What is the superhero ID? ")
    try:
        if ID[0] == "M" or ID[0] == "m" or ID[0] == "D" or ID[0] == "d":
            if len(ID) >= 5:
                print("Entry is invalid!")
                return getChoice()
            else:
                try:
                    int(ID[1:])
                except ValueError:
                    print("Entry is invalid!")
                    return getChoice()
                return ID
        else:
            print("Entry is invalid!")
            return getChoice()
    except IndexError:
        print("Entry is invalid!")
        return getChoice()

##checks and returns the correct data set to look in

def configSelection(MADATA, DCDATA, ID):
    """Returns the right data set

    Args:
        MADATA (List): Marvel Data
        DCDATA (List): DC Data
        ID (String): The id that has been entered

    Returns:
        List: The correct dataset
    """
    if ID[0] == "M" or ID[0] == "m":
        return MADATA
    else:
        return DCDATA

## merge search function

def getData(DATA, ID):     
    """finds the correct id in the data

    Args:
        DATA (list): the data set
        ID (int): the id

    Returns:
        list: the character information
    """
    MIDPOINT = len(DATA) // 2

    try:
        if DATA[MIDPOINT][0] == ID:
            return DATA[MIDPOINT]
        else:
            if ID < DATA[MIDPOINT][0]:
                return getData(DATA[:MIDPOINT], ID)
            else:
                return getData(DATA[MIDPOINT + 1:], ID)
    except IndexError:
        print("Entry was not found in the database!")
        return 1

##prints out the data

def printData(CHAR):
    """prints out the character information

    Args:
        CHAR (list): the information
    """
    charID = CHAR[0]

    if CHAR[10][0] == "M":
        CHAR[0] = f"M00{charID}"
    else:
        CHAR[0] = f"D00{charID}"

    try:
        if CHAR[3][0] == "G":
            ALIGNMENT = "SuperHero"

        if CHAR[3][0] == "B":
            ALIGNMENT = "SuperVillain"

        if CHAR[3][0] == "N" or CHAR[3][0] == "":
            ALIGNMENT = "Character"
    except IndexError:
        ALIGNMENT = "Character"

    try:
        if len(CHAR[0]) > 4:
            if CHAR[10][0] == "M":
                CHAR[0] = f"M0{charID}"
            else:
                CHAR[0] = f"D0{charID}"
    except IndexError:
        pass
    
    try:
        if len(CHAR[0]) > 4:
            if CHAR[10][0] == "M":
                CHAR[0] = f"M{charID}"
            else:
                CHAR[0] = f"D{charID}"
    except IndexError:
        pass

    print(f'''
{ALIGNMENT} ID: {CHAR[0]}
name: {CHAR[1]}
ID: {CHAR[2]}
ALIGN: {CHAR[3]}
EYE: {CHAR[4]}
HAIR: {CHAR[5]}
ALIVE: {CHAR[6]}
APPEARANCES: {CHAR[7]}
FIRST APPEARANCE: {CHAR[8]}
YEAR: {CHAR[9]}
Brand: {CHAR[10]}
''')

### --- General Functions
##sort data between marvel and dc

def splitData(DATA):
    """splits the data into DC

    Args:
        DATA (list): the list of heros
    """
    dataDC = []
    dataMA = []
    for i in range(len(DATA)):
        if DATA[i][0][0] == "D":
            DATA[i][0] = DATA[i][0][1:]
            DATA[i][0] = int(DATA[i][0])
            dataDC.append(DATA[i])

        else: 
            DATA[i][0][0] == "M"
            DATA[i][0] = DATA[i][0][1:]
            DATA[i][0] = int(DATA[i][0])
            dataMA.append(DATA[i])

    return dataMA, dataDC

# csv to array function

def getRawData(fileName):
	import csv
	tempLi = []
	fil = open(fileName)
	text = csv.reader(fil)
	for line in text:
		tempLi.append(line)
	var = tempLi.pop(0)
	return tempLi, var

def repeat():
    """checks if the user wants to rerun the search again
    """
    CHOICE = checkInt(input('''Press 1 to Search again
Press 2 to Go back to Main menu
Press 3 to Exit the Program
> '''))
    if CHOICE >= 4 or CHOICE <= 0:
        print("This is an invalid number!")
        return repeat()
    else:
        return CHOICE

def checkInt(VALUE):
    """Checks if the value is an integer or not

    Args:
        VALUE (string): the value that is entered

    Returns:
        int: the inted version of the string
    """
    try:
        return int(VALUE)
    except ValueError:
        print("This is not a number!")
        return checkInt(input("Please enter a number: "))

def checkIntRange(VALUE,LOW,HIGH):
    """Check if value is an integer, then checks if it is in the range

    Args:
        VALUE (string): the entered value
        LOW (int): from
        HIGH (int): to

    Returns:
        int: the number
    """
    try:
        if int(VALUE) <= HIGH and int(VALUE) >= LOW:
            return int(VALUE)
    except ValueError:
        print("This is not a number!")
        return checkIntRange(input("Please enter a number: "),LOW,HIGH)
    print("This is not a number!")
    return checkIntRange(input("Please enter a number: "),LOW,HIGH)

def mainMenu():
    CHOICE = checkInt(input('''
Press 1 to Search by ID
Press 2 to Search by Filter
Press 3 to Exit the Program
> '''))
    if CHOICE >= 4 or CHOICE <= 0:
        print("This is an invalid number!")
        return mainMenu()
    else:
        return CHOICE

### --- Filter Functions

def filterInfo(DATA):

    NEWDATA = []
    OLDDATA = []
    IDLOOP = 1
    ALIGLOOP = 1
    ALIVELOOP = 1
    BRANDLOOP = 1
    APPLOOP = 1
    EYELOOP = 1
    HAIRLOOP = 1
    ALLLOOP = 1

    while IDLOOP == 1 and ALLLOOP == 1:

        print('''
Type of Identity?''')
        CHOICE = checkIntRange(input('''Press 0 to skip
Press 1 if Public identity
Press 2 if Secret identity 
Press 3 if No Dual identity 
Press 4 if Known to authorities identity
Press 5 if No type of identity
> '''),0,5)
        if CHOICE == 0:
            OLDDATA = DATA
            IDLOOP = 2
        if CHOICE == 1:
            FILTEROP = '"Public Identity"'
            for i in range(len(DATA)):
                if DATA[i][2] == "Public Identity":
                    NEWDATA.append(DATA[i])
        if CHOICE == 2:
            FILTEROP = '"Secret Identity"'
            for i in range(len(DATA)):
                if DATA[i][2] == "Secret Identity":
                    NEWDATA.append(DATA[i])
        if CHOICE == 3:
            FILTEROP = '"No Dual Identity"'
            for i in range(len(DATA)):
                if DATA[i][2] == "No Dual Identity":
                    NEWDATA.append(DATA[i])
        if CHOICE == 4:
            FILTEROP = '"Known to Authorities Identity"'
            for i in range(len(DATA)):
                if DATA[i][2] == "Known to Authorities Identity":
                    NEWDATA.append(DATA[i])
        if CHOICE == 5:
            FILTEROP = '"No Type of Identity"'
            for i in range(len(DATA)):
                if DATA[i][2] == "":
                    NEWDATA.append(DATA[i])

        if CHOICE != 0:
            if len(NEWDATA) == 0:
                print(f"There were no characters found with the filter {FILTEROP}!")
                CHOICE = checkIntRange(input('''Press 1 to go back to filtering options
Press 0 to skip
> '''),0,1)
                if CHOICE == 0:
                    OLDDATA = DATA
                    IDLOOP = 2      
            else:
                OLDDATA = NEWDATA
                NEWDATA = []
                IDLOOP = 2                                 
    if len(OLDDATA) == 1:
        return OLDDATA
    print(f'{len(OLDDATA)} characters found')    
    while ALIGLOOP == 1 and ALLLOOP == 1:

        print('''
Type of Alignment?''')
        CHOICE = checkIntRange(input('''Press 0 to skip
Press 1 if Good Alignment
Press 2 if Bad Alignment
Press 3 if Neutral Alignment
Press 4 if No Alignment
> '''),0,4)
        if CHOICE == 0:
            ALIGLOOP = 2
        if CHOICE == 1:
            FILTEROP = '"Good Alignment"'
            for i in range(len(OLDDATA)):
                if OLDDATA[i][3] == "Good Characters":
                    NEWDATA.append(OLDDATA[i])
        if CHOICE == 2:
            FILTEROP = '"Bad Alignment"'
            for i in range(len(OLDDATA)):
                if OLDDATA[i][3] == "Bad Characters":
                    NEWDATA.append(OLDDATA[i])
        if CHOICE == 3:
            FILTEROP = '"Neutral Alignment"'
            for i in range(len(OLDDATA)):
                if OLDDATA[i][3] == "Neutral Characters":
                    NEWDATA.append(OLDDATA[i])
        if CHOICE == 4:
            FILTEROP = '"No Alignment"'
            for i in range(len(OLDDATA)):
                if OLDDATA[i][3] == "":
                    NEWDATA.append(OLDDATA[i])
        if CHOICE != 0:
            if len(NEWDATA) == 0:
                print(f"There were no characters found with the filter {FILTEROP}!")
                CHOICE = checkIntRange(input('''Press 1 to go back to filtering options
Press 0 to skip
> '''),0,1)
                if CHOICE == 0:
                    ALIGLOOP = 2
            else:
                OLDDATA = NEWDATA
                NEWDATA = []
                ALIGLOOP = 2   
    if len(OLDDATA) == 1:
        return OLDDATA
    print(f'{len(OLDDATA)} characters found')      
    while ALIVELOOP == 1 and ALLLOOP == 1:
        print('''
Dead or Alive?''')
        CHOICE = checkIntRange(input('''Press 0 to skip
Press 1 if they are Alive
Press 2 if they are Dead
> '''),0,2)
        if CHOICE == 0:
            ALIVELOOP = 2
        if CHOICE == 1:
            FILTEROP = '"Alive"'
            for i in range(len(OLDDATA)):
                if OLDDATA[i][6] == "Living Characters":
                    NEWDATA.append(OLDDATA[i])
        if CHOICE == 2:
            FILTEROP = '"Dead"'
            for i in range(len(OLDDATA)):
                if OLDDATA[i][6] == "Deceased Characters":
                    NEWDATA.append(OLDDATA[i])
        if CHOICE != 0:
            if len(NEWDATA) == 0:
                print(f"There were no characters found with the filter {FILTEROP}!")
                CHOICE = checkIntRange(input('''Press 1 to go back to filtering options
Press 0 to skip
> '''),0,1)
                if CHOICE == 0:
                    ALIVELOOP = 2
            else:
                OLDDATA = NEWDATA
                NEWDATA = []
                ALIVELOOP = 2    
    if len(OLDDATA) == 1:
        return OLDDATA
    print(f'{len(OLDDATA)} characters found')      
    while BRANDLOOP == 1 and ALLLOOP == 1:
        print('''
Brand?''')
        CHOICE = checkIntRange(input('''Press 0 to skip
Press 1 for Marvel
Press 2 for DC
> '''),0,2)
        if CHOICE == 0:
            BRANDLOOP = 2
        if CHOICE == 1:
            FILTEROP = '"Marvel"'
            for i in range(len(OLDDATA)):
                if OLDDATA[i][10] == "Marvel":
                    NEWDATA.append(OLDDATA[i])
        if CHOICE == 2:
            FILTEROP = '"DC"'
            for i in range(len(OLDDATA)):
                if OLDDATA[i][10] == "DC":
                    NEWDATA.append(OLDDATA[i])
        if CHOICE != 0:
            if len(NEWDATA) == 0:
                print(f"There were no characters found with the filter {FILTEROP}!")
                CHOICE = checkIntRange(input('''Press 1 to go back to filtering options
Press 0 to skip
> '''),0,1)
                if CHOICE == 0:
                    BRANDLOOP = 2
            else:
                OLDDATA = NEWDATA
                NEWDATA = []
                BRANDLOOP = 2   
    if len(OLDDATA) == 1:
        return OLDDATA
    print(f'{len(OLDDATA)} characters found')      
    while APPLOOP == 1 and ALLLOOP == 1:
        print('''
Amount of Appearances?''')
        CHOICE = checkIntRange(input('''Press 0 to skip
Press 1 for exact appearances input
Press 2 for range of appearances input
> '''),0,2)
        if CHOICE == 0:
            APPLOOP = 2
        if CHOICE == 1:
            APPS = checkIntRange(input("Exact amount of appearances?(Max is 99,999): "),0,99999)
            FILTEROP = f'"{APPS} Appearances"'
            for i in range(len(OLDDATA)):
                if int(OLDDATA[i][7]) == APPS:
                    NEWDATA.append(OLDDATA[i])
        if CHOICE == 2:
            APPLOW = checkIntRange(input("Range from?(Max is 99998): "),0,99998)
            APPHIGH = checkIntRange(input("Range to?(Max is 99999): "),APPLOW,99999)
            FILTEROP = f'"Range from {APPLOW} to {APPHIGH}"'
            for i in range(len(OLDDATA)):
                for j in range(APPLOW, APPHIGH+1):
                    if int(OLDDATA[i][7]) == j:
                        NEWDATA.append(OLDDATA[i])
        if CHOICE != 0:
            if len(NEWDATA) == 0:
                print(f"There were no characters found with the filter {FILTEROP}!")
                CHOICE = checkIntRange(input('''Press 1 to go back to filtering options
Press 0 to skip
> '''),0,1)
                if CHOICE == 0:
                    APPLOOP = 2
            else:
                OLDDATA = NEWDATA
                NEWDATA = []
                APPLOOP = 2 
    if len(OLDDATA) == 1:
        return OLDDATA
    print(f'{len(OLDDATA)} characters found')      
    while EYELOOP == 1 and ALLLOOP == 1:
        EYECOLORS = []
        EYECOLORS.append(OLDDATA[0][4])
        for i in range(1,len(OLDDATA)):
            EYEMATCH = 1
            for j in range(len(EYECOLORS)):
                if OLDDATA[i][4] == EYECOLORS[j]:
                    EYEMATCH = 0
            if EYEMATCH == 1:
                EYECOLORS.append(OLDDATA[i][4])
        print('''
Eye Color?
Press 0 to skip''')
        for i in range(len(EYECOLORS)):
            if EYECOLORS[i] == "":
                EYECOLORS[i] = "None Type"
                EYETEMP = i
            print(f"Press {i+1} for {EYECOLORS[i]}")
            try:
                EYECOLORS[EYETEMP] = ""
            except UnboundLocalError:
                continue
            except TypeError:
                continue
        CHOICE = checkIntRange(input("> "),0,len(EYECOLORS))
        if CHOICE == 0:
            EYELOOP = 2
        for i in range(1,len(EYECOLORS)+2):
            if int(CHOICE) == i-1:
                for j in range(len(OLDDATA)):
                    if OLDDATA[j][4] == EYECOLORS[i-2]:
                        NEWDATA.append(OLDDATA[j])
        if CHOICE != 0:
            OLDDATA = NEWDATA
            NEWDATA = []
            EYELOOP = 2
            EYETEMP = None
    if len(OLDDATA) == 1:
        return OLDDATA
    print(f'{len(OLDDATA)} characters found')     
    while HAIRLOOP == 1 and ALLLOOP == 1:
        HAIRCOLORS = []
        HAIRCOLORS.append(OLDDATA[0][5])
        for i in range(1,len(OLDDATA)):
            HAIRMATCH = 1
            for j in range(len(HAIRCOLORS)):
                if OLDDATA[i][5] == HAIRCOLORS[j]:
                    HAIRMATCH = 0
            if HAIRMATCH == 1:
                HAIRCOLORS.append(OLDDATA[i][5])
        print('''
Hair Color?
Press 0 to skip''')
        for i in range(len(HAIRCOLORS)):
            if HAIRCOLORS[i] == "":
                HAIRCOLORS[i] = "None Type"
                HAIRTEMP = i
            print(f"Press {i+1} for {HAIRCOLORS[i]}")
            try:
                HAIRCOLORS[HAIRTEMP] = ""
            except UnboundLocalError:
                continue
            except TypeError:
                continue
        CHOICE = checkIntRange(input("> "),0,len(HAIRCOLORS))
        if CHOICE == 0:
            HAIRLOOP = 2
        for i in range(1,len(HAIRCOLORS)+2):
            if int(CHOICE) == i-1:
                for j in range(len(OLDDATA)):
                    if OLDDATA[j][5] == HAIRCOLORS[i-2]:
                        NEWDATA.append(OLDDATA[j])
        if CHOICE != 0:
            OLDDATA = NEWDATA
            NEWDATA = []
            HAIRLOOP = 2
            HAIRTEMP = None
    
    return OLDDATA 

def printFilteredData(FDATA):
    if len(FDATA) == 1:
        DATA = []
        for i in range(len(FDATA[0])):
            DATA.append(FDATA[0][i])
        print('''
Only 1 character was found with the filters:''')
        printData(DATA)
    else:
        print(f'''
{len(FDATA)} characters were found:''')
        for i in range(len(FDATA)):
            FDATAID = FDATA[i][0]
            if FDATA[i][10][0] == "M":
                FDATA[i][0] = f"M00{FDATAID}"
            else:
                FDATA[i][0] = f"D00{FDATAID}"

            if len(FDATA[i][0]) > 4:
                if FDATA[i][10][0] == "M":
                    FDATA[i][0] = f"M0{FDATAID}"
                else:
                    FDATA[i][0] = f"D0{FDATAID}"
            
            if len(FDATA[i][0]) > 4:
                if FDATA[i][10][0] == "M":
                    FDATA[i][0] = f"M{FDATAID}"
                else:
                    FDATA[i][0] = f"D{FDATAID}"
           
            print(f'''ID: {FDATA[i][0]}, NAME: {FDATA[i][1]}
''')
    
### --- MAIN PROGRAM CODE --- ###

if __name__ == "__main__":

    rawArr, headers = getRawData('comicBookCharData_mixed.csv')
    MADATA, DCDATA = splitData(rawArr)
    FULLDATA = rawArr
    DCDATA = mergeSort(DCDATA)
    for i in range(len(DCDATA)):
        print(DCDATA[i])
    MADATA = mergeSort(MADATA)
    FULLDATA = mergeSort(FULLDATA)

    while True:

        CHOICE = mainMenu()

        while CHOICE == 1:

            while True:
                CHAR = 1
                selectedID = getChoice()
                ID = int(selectedID[1:])

                DATA = configSelection(MADATA, DCDATA, selectedID)
                CHAR = getData(DATA, ID)

                if CHAR != 1:
                    break
            printData(CHAR)

            REPEAT = repeat()
            if REPEAT == 1:
                continue
            if REPEAT == 2:
                CHOICE = 0
            if REPEAT == 3:
                CHOICE = 3

        while CHOICE == 2:
            FILTEREDDATA = filterInfo(FULLDATA)
            printFilteredData(FILTEREDDATA)
            
            REPEAT = repeat()
            if REPEAT == 1:
                continue
            if REPEAT == 2:
                CHOICE = 0
            if REPEAT == 3:
                CHOICE = 3

        if CHOICE == 3:
            exit()

