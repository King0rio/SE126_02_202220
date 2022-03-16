#Isaiah Diiorio
#3/16/2022
#Final

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: 

#VARIABLE DICTIONARY:
#varName        description of data it will hold


#NOTES: 

#imports------------------------------------------------
import csv
#functions----------------------------------------------

def visuals(arr):
    '''The basics of the program'''
    length = 15
    #length = len(arr)
    print("Last       First      State      Phone Number")
    for x in range (0, length):
        for y in range(0, 4):
            print("{0:10} ".format(arr[x][y]), end="")
        print("")

def swap():
    '''swaps the first and last name Position'''
    fileLen = len(fileData)

    for x in range(0, fileLen-1):
        temp0 = fileData[x][0]
        temp1 = fileData[x][1]
        fileData[x][0] = temp1
        fileData[x][1] = temp0

def sort(fileInfo):
    '''sort the file Data by last name alphebectically'''

    swap()

    x = len(fileInfo) - 1
    for i in range(x):
        for j in range(x - i):
            if fileInfo[j] > fileInfo[j + 1]:
                fileInfo[j], fileInfo[j + 1] = fileInfo[j + 1], fileInfo[j]

    return fileData

#def binarySearch(arr, key):
    '''yo '''
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)/2
        if key == arr[mid]:
            return mid
        elif key % arr[mid] < 0:
            high = mid-1
        else:
            low = mid+1
    else:
        return -1



def binarySearch(array, x, low, high):
    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1

#Main---------------------------------------------------
fileData = []

with open('Final/exam1.txt') as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        fileData.append(row)
csvfile.close()

sort(fileData)
visuals(fileData)

userInput = input("\nWho's File are you looking for (Last Name) : ")

last = []
for i in range(0, 70):
    last.append(fileData[i][0])

output = binarySearch(last, userInput, 0, 70)
if output != -1:
    for x in range(0, 4):
        print("{0:10} ".format(fileData[output][x]), end="")
else:
    print("Invalid Last Name")