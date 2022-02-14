#Isaiah Diiorio
#lab4b
#2/14/202

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: Write a Python program to assign passengers seats in an airplane.  Assume a small airplane with seat numbering as follows.

#VARIABLE DICTIONARY:
#varName        description of data it will hold


#NOTES: 

#imports------------------------------------------------

#functions----------------------------------------------
def seatMap():
    '''Displays the seating arangements on the plane'''
    print("Row")

    for col in range(1,8):
        print("{0:2}  {1}  {2}    {3}  {4}".format(col, col1[col], col2[col], col3[col], col4[col]))

def seatChoice():
    '''User is promped to make a choice on there seat'''
    userInput = 0
#Main---------------------------------------------------


col1 = ["", "A", "A", "A", "A", "A", "A", "A"]
col2 = ["", "B", "B", "B", "B", "B", "B", "B"]
col3 = ["", "C", "C", "C", "C", "C", "C", "C"]
col4 = ["", "D", "D", "D", "D", "D", "D", "D"]




seatMap()