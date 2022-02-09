#Isaiah Diiorio
#lab 2b
#2/7/2022

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: You have been asked to produce a report that lists all the computers in the csv file Lab2b.csv.

#VARIABLE DICTIONARY:
#varName        description of data it will hold


#NOTES: 

#imports------------------------------------------------
import csv
from email.utils import collapse_rfc2231_value

from pyrsistent import v
#functions----------------------------------------------
#Main---------------------------------------------------

print("Type\tBrand\tCPU\tRAM\t1st Disk      No. HDD\t 2nd Disk  OS   YR")

with open("week2\lab2b.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        col0 = row[0]#desktop or labtop
        col1 = row[1]#dell or hp or gateway
        col2 = row[2]#processor
        col3 = row[3]#ammount of Ram in GB
        col4 = row[4]# size of hard drive
        col5 = row[5]#number of hard drives
        if col5 == "1":
            col6 = "     "
            col7 = row[6]
            col8 = row[7]
        else:
            col6 = row[6]
            col7 = row[7]
            col8 = row[8]
        
        print("{0}\t{1}\t{2}\t{3}\t{4}\t       {5:2}\t {6}\t   {7}  {8}".format(col0, col1, col2, col3, col4, col5, col6, col7, col8))
