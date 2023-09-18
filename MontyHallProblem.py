import random

winSwitch = 0
looseSwitch = 0
winKeep = 0
looseKeep = 0

switch = 0

# number of times to run the code!!!
run = 10000

def main():
    for x in range(run):
        runRound()
        printRound()
        resetRound()
    
    printTotal()
      
def runRound():
    global winSwitch
    global looseSwitch
    global winKeep
    global looseKeep
    
    door = tripleRandom()
    guessInit = tripleRandom()
    goat = findGoat(door, guessInit)
    
    print("initial guess is", guessInit)
    print("door is", door)
    print("goat is", goat)

    if (doubleRandom() == 1):
        print("switched")
        
        if (findRemaining(guessInit, goat) == door):
            winSwitch = winSwitch + 1
        else:
            looseSwitch = looseSwitch + 1
    else:
        print("stayed")
        if (door == guessInit):
            winKeep = winKeep + 1
        else:
            looseKeep = looseKeep + 1

def findGoat(door, guessInit):
    if(door == guessInit):
        if(door == 1):
            return doubleRandom() + 1
        if(door == 2):
            if(doubleRandom() == 1):
                return 1
            else:
                return 3
        if(door == 3):
            return doubleRandom()
    else:
        return findRemaining(door, guessInit)
    
def findSwitch(guessInit, goat):
    return findRemaining(guessInit, goat)
            
def findRemaining(num1, num2):
    if(num1 != 1 and num2 != 1):
        return 1
    elif(num1 != 2 and num2 != 2):
        return 2
    else:
        return 3

def tripleRandom():
    return random.randint(1, 3)

def doubleRandom():
    return random.randint(1, 2)

def printRound():
    print("Win Switch", winSwitch)
    print("Loose Switch", looseSwitch)
    print("Win Keep", winKeep)
    print("Loose Keep", looseKeep)
    
def printTotal():
    printRound()
    print("\n\n\n")
    print("The SWITCH win to loss ratio is", winSwitch, ":", looseSwitch, "=", winSwitch / looseSwitch)
    print("The SWITCH percent win is", (winSwitch / (winSwitch + looseSwitch)) * 100, "%")
    
    print("The KEEP win to loss ratio is", winKeep, ":", looseKeep, "=", winKeep / looseKeep)
    print("The KEEP percent win is", (winKeep / (winKeep + looseKeep)) * 100, "%")
    
def resetRound():
    print("\t*\t")
    global switch
    switch = 0

if __name__ == "__main__":
    main()