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
def fillRows():
    '''Fills all of the arrays'''
    x = ["", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", ]

    return x

def seatMap():
    '''Displays the '''
    
    print("Row  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4")
    for col in range(1,16):
        print(" {0:2}  {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30}".format(col, cA[col], cB[col], cC[col], cD[col], cE[col], cF[col], cG[col], cH[col], cI[col], cJ[col], cK[col], cL[col], cM[col], cN[col], cO[col], cP[col], cQ[col], cR[col], cS[col], cT[col], cU[col], cV[col], cW[col], cX[col], cY[col], cZ[col], c1[col], c2[col], c3[col], c4[col]))

def inputTest1(input1):
    '''yo'''

def inputTest2(input2):
    '''yo'''

def seatChoice():
    '''yo'''

def seatsTaken():
    '''yo'''
    
    seatsTaken = 0
    seatsAvailable = 0
    this = [[seatsTaken, seatsAvailable], []]
    for row in range(1, 31):
        if cA[row] == "X":
            seatsTaken += 1
        elif cA[row] == "#":
            seatsAvailable += 1

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


seatMap()




