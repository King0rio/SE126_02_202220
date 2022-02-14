#Isaiah Diiorio
#lab4b
#2/14/202

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows.

#VARIABLE DICTIONARY:
#varName        description of data it will hold


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

def correctTest(input2):
    '''this tests that the user has enterd the correct col value A, B, C, D'''
    

    if input2.upper() == "A":
        test = "y"
    elif input2.upper() == "B":
        test = "y"
    elif input2.upper() == "C":
        test = "y"
    elif input2.upper() == "D":
        test = "y"
    else:
        test = "n"

    return test

def seatChoice():
    '''User is promped to make a choice on there seat'''

    seatMap()

    input1 = int(input("What row would you like to be seated in: "))
    input2 = input("What column would you like to be seated in (ex:A,B,C,D): ")

    if input2.upper() == "A":
        test = "y"
    elif input2.upper() == "B":
        test = "y"
    elif input2.upper() == "C":
        test = "y"
    elif input2.upper() == "D":
        test = "y"
    else:
        test = "n"

    while input1 != [1-7] or test != "y":
        clear()
        seatMap()

        print("ERROR! Please Enter Valid Choice")
        input1 = int(input("What row would you like to be seated in: "))
        input2 = input("What column would you like to be seated in (ex:A,B,C,D): ")
        
        if input2.upper() == "A":
            test = "y"
        elif input2.upper() == "B":
            test = "y"
        elif input2.upper() == "C":
            test = "y"
        elif input2.upper() == "D":
            test = "y"
        else:
            test = "n"
        

    return input1, input2

 

#Main---------------------------------------------------

col1 = ["", "A", "A", "A", "A", "A", "A", "A"]
col2 = ["", "B", "B", "B", "B", "B", "B", "B"]
col3 = ["", "C", "C", "C", "C", "C", "C", "C"]
col4 = ["", "D", "D", "D", "D", "D", "D", "D"]


userRow, userCol = seatChoice()

if userCol.upper() == "A":
    if col1[userRow] == "A":
        print("hello dose thes work ")
elif userCol.upper() == "B":
    print()
elif userCol.upper() == "C":
    print()
elif userCol.upper() == "D":
    print()
else:
    print()