#Isaiah Diiorio
#lab4a
#2/14/2022

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: place all the data from the file into lists.. Once all the data has be loaded into arrays you must search the array to determine how many computers have more than 8GB of RAM.

#VARIABLE DICTIONARY:
#varName        description of data it will hold
#ram            stores all of the ram value's for computers in the csv file 
#ramCheck       is used to save the number of computers with more than 8GB of ram 
#row            is used to read one row at a time from file
#row            represents a row in the csv file
#col            represents a column in the csv file
#ram[col]       used to pull data from that colum of the csv file

#NOTES: 

#imports------------------------------------------------
import csv
#functions----------------------------------------------
#Main---------------------------------------------------

ram = []
ramCheck = 0

with open("week4\lab4a.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        
        ram.append(row[3])


for col in range(29):
    if (int(ram[col]) > 8):
        ramCheck += 1

print("there are {0} Computers that have more than 8GB of ram ".format(ramCheck))