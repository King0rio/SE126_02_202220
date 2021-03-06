#Isaiah Diiorio
#Lab3a
#2/9/2022

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: 

#VARIABLE DICTIONARY:
#varName        description of data it will hold
#year           the current year
#desktop        the total number of desktops being replaced 
#labtop         the total number of labtops being replaced
#replaceDesktop the total cost of replacing all of the desktops 
#replaceLabtop  the total cost of replacing all of the labtops 
#col0           the column that holds the D or L value to deside if something is a desktop or a labtop 
#col5           the column that holds the number of HDD it effects where the age is stored 
#age            the column that holds the year the computer was created 
#file           is the file stored in the location defined in open
#row            is used to read one row at a time from file
#row            represents a row in the csv file

#NOTES: 

#imports------------------------------------------------
import csv
#functions----------------------------------------------
#Main---------------------------------------------------

year = 22
replaceDesktop = 0
replaceLabtop = 0
desktop = 0
labtop = 0

with open("week3\lab3a.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        col0 = row[0]#desktop or labtop
        col5 = row[5]#number of hard drives
        if col5 == "1":
            age = int(row[7])
        else:
            age = int(row[8])
        
        if age <= (year - 2):
            if col0 == "D":
                replaceDesktop += 2000
                desktop += 1
            else:
                replaceLabtop += 1500
                labtop += 1

print("To Replace {0:2} It Will Cost: ${1:8}\nTo Replace {2:2} It Will Cost: ${3:8}".format(desktop, replaceDesktop, labtop, replaceLabtop))

        