#Isaiah Diiorio
#2/28/2022
#Lab 8

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: 

#VARIABLE DICTIONARY:
#varName        description of data it will hold


#NOTES: like the plane seating 

#imports------------------------------------------------
#functions----------------------------------------------
from sqlalchemy import literal


def fillRows():
    '''Fills all of the arrays'''
    x = ["", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", ]

    return x

def seatMap():
    '''Displays the seating in the theater'''
    
    print("Row  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4")
    for col in range(1,16):
        print(" {0:2}  {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30}".format(col, cA[col], cB[col], cC[col], cD[col], cE[col], cF[col], cG[col], cH[col], cI[col], cJ[col], cK[col], cL[col], cM[col], cN[col], cO[col], cP[col], cQ[col], cR[col], cS[col], cT[col], cU[col], cV[col], cW[col], cX[col], cY[col], cZ[col], c1[col], c2[col], c3[col], c4[col]))

def seatChoice():
    '''yo'''
    userInput1 = "c" + input("What Column Would You Like To Be Seated In : ")
    userInput2 = input("What Row Would You Like Your Seat To Be In : ")

    print(userInput1)
    userInput1[userInput2] = "X" 


def seatsTaken(column):
    '''yo'''
    seatsTaken = 0
    seatsAvailable = 0
    for row in range(1, 16):
        if column[row] == "X":
            seatsTaken += 1
        elif column[row] == "#":
            seatsAvailable += 1
    
    return seatsTaken, seatsAvailable

def seatsTakenTotal():
    '''yo'''
    seatsTakenTotal = 0
    seatsAvailableTotal = 0

    temp1, temp2 = seatsTaken(cA)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cB)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cC)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cD)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cE)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cF)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cG)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cH)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cI)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cJ)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cK)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cL)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cM)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cN)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cO)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cP)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cQ)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cR)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cS)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cT)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cU)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cV)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cW)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cX)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cY)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(cZ)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(c1)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(c2)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(c3)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2
    temp1, temp2 = seatsTaken(c4)
    seatsTakenTotal += temp1
    seatsAvailableTotal += temp2

    return seatsTakenTotal, seatsAvailableTotal

#Main---------------------------------------------------

cA = fillRows()
cB = fillRows()
cC = fillRows()
cD = fillRows()
cE = fillRows()
cF = fillRows()
cG = fillRows()
cH = fillRows()
cI = fillRows()
cJ = fillRows()
cK = fillRows()
cL = fillRows()
cM = fillRows()
cN = fillRows()
cO = fillRows()
cP = fillRows()
cQ = fillRows()
cR = fillRows()
cS = fillRows()
cT = fillRows()
cU = fillRows()
cV = fillRows()
cW = fillRows()
cX = fillRows()
cY = fillRows()
cZ = fillRows()
c1 = fillRows()
c2 = fillRows()
c3 = fillRows()
c4 = fillRows()

seatsSold = 0 
seatsUnsold = 0
seatsSold, seatsUnsold= seatsTakenTotal()
print(seatsUnsold, seatsSold)
seatMap()
seatChoice()
seatMap()


