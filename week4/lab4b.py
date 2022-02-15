#Isaiah Diiorio
#lab4b
#2/14/202

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows.

#VARIABLE DICTIONARY:
#varName        description of data it will hold
#col1
#col2
#col3
#col4
#taken          String that holds the taken seat output 
#booked         String that holds the booked seat output
#loop           alows the user to enter more seats and loops the program 
#userRow        the passed value from seatChoice() represents the users input for row 
#userCol        the passed value from seatChoice() represents the users input for column
#
#
#
#
#


#NOTES: 

#imports------------------------------------------------
from os import system, name 
def clear(): 
  
  if name == 'nt': 
      _ = system('cls') 

  else: 
      _ = system('clear')
#functions----------------------------------------------

def seatMap():
    '''Displays the seating arangements on the plane'''
    print("Row")

    for col in range(1,8):
        print("{0:2}  {1}  {2}    {3}  {4}".format(col, col1[col], col2[col], col3[col], col4[col]))

def correctTest1(input2):
    '''this tests that the user has enterd the correct col value A, B, C, D'''
    
    input2 = str(input2)

    if input2.upper() == "A":
        test1 = "y"
    elif input2.upper() == "B":
        test1 = "y"
    elif input2.upper() == "C":
        test1 = "y"
    elif input2.upper() == "D":
        test1 = "y"
    else:
        test1 = "n"

    return test1

def correctTest2(input1):
    '''this tests that the user has enterd the correct row value 1-7 '''
    
    if input1 == "1":
        test2 = "y"
    elif input1 == "2":
        test2 = "y"
    elif input1 == "3":
        test2 = "y"
    elif input1 == "4":
        test2 = "y"
    elif input1 == "5":
        test2 = "y"
    elif input1 == "6":
        test2 = "y"
    elif input1 == "7":
        test2 = "y"
    else:
        test2 = "n"

    return test2

def seatChoice():
    '''User is promped to make a choice on there seat and is tested for corect input from user'''

    seatMap()

    input1 = input("What row would you like to be seated in: ")
    input2 = input("What column would you like to be seated in (ex:A,B,C,D): ")

    test1 = str(correctTest1(input2))
    test2 = str(correctTest2(input1))

    while test1 == "n" or test2 == "n":
        clear()
        seatMap()

        print("ERROR! Please Enter Valid Choice")
        input1 = input("What row would you like to be seated in: ")
        input2 = input("What column would you like to be seated in (ex:A,B,C,D): ")

        test1 = str(correctTest1(input2))
        test2 = str(correctTest2(input1))

        

    return int(input1), input2

def usrContinue():
    '''asks the user if they would like to continue the program and returns y or n'''

    userInput = input("Woud you like to book another seat?\n[Y/N]: ")

    while userInput.lower() != "y" and userInput.lower() != "n":
        
        print("ERROR! Please Enter Valid Choice")
        userInput = input("Woud you like to book another seat?\n[Y/N]: ")
    
    clear()
    return str(userInput)

def maxSeat():
    '''Tests for all seats being filled '''
    totalSeat = 28 

    for row in range(1, 8):
        if col1[row] == "X":
            totalSeat -= 1

        if col2[row] == "X":
            totalSeat -= 1

        if col3[row] == "X":
            totalSeat -= 1

        if col4[row] == "X":
            totalSeat -= 1
    
    return totalSeat

#Main---------------------------------------------------

col1 = ["", "A", "A", "A", "A", "A", "A", "A"]
col2 = ["", "B", "B", "B", "B", "B", "B", "B"]
col3 = ["", "C", "C", "C", "C", "C", "C", "C"]
col4 = ["", "D", "D", "D", "D", "D", "D", "D"]

taken = "That seat has already been taken!\n"
booked = "Your Seat Has Been Booked!\n"
loop = "y"

while loop.lower() == "y" and maxSeat() > 0:

    userRow, userCol = seatChoice()

    if userCol.upper() == "A":
        if col1[userRow] == "A":
            col1[userRow] = "X"
            clear()
            print(booked)
            seatMap()
        else:
            clear()
            print(taken)
            seatMap()

    elif userCol.upper() == "B":
        if col2[userRow] == "B":
            col2[userRow] = "X"
            clear()
            print(booked)
            seatMap()
        else:
            clear()
            print(taken)
            seatMap()

    elif userCol.upper() == "C":
        if col3[userRow] == "C":
            col3[userRow] = "X"
            clear()
            print(booked)
            seatMap()
        else:
            clear()
            print(taken)
            seatMap()

    elif userCol.upper() == "D":
        if col4[userRow] == "D":
            col4[userRow] = "X"
            clear()
            print(booked)
            seatMap()
        else:
            clear()
            print(taken)
            seatMap()

    loop = usrContinue()

if maxSeat() == 0:
    print("There are no more seats on the plane!")
else:
    print("Have a Safe flight!")