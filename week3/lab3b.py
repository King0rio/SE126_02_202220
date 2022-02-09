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
from numpy import append
#functions----------------------------------------------
#Main---------------------------------------------------

year = 22
replaceDesktop = 0
replaceLabtop = 0
desktop = 0
labtop = 0

col0 = []
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []


with open("week3\lab3a.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        col0.append(row[0])#desktop or labtop
        col1.append(row[1])#dell or hp or gateway
        col2.append(row[2])#processor
        col3.append(row[3])#ammount of Ram in GB
        col4.append(row[4])# size of hard drive
        col5.append(row[5])#number of hard drives
        temp = row[5]
        if temp == "1":
            col6.append("     ")
            col7.append(row[6])
            col8.append(row[7])
        else:
            col6.append(row[6])
            col7.append(row[7])
            col8.append(row[8])

print("To Replace {0:2} It Will Cost: ${1:8}\nTo Replace {2:2} It Will Cost: ${3:8}".format(desktop, replaceDesktop, labtop, replaceLabtop))

        