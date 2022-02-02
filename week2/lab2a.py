#Isaiah Diiorio
#
#

#Program Essentials with Python, SE116, and .21
#PROGRAM PROMPT: 

#VARIABLE DICTIONARY:
#varName        description of data it will hold


#NOTES: 

#imports------------------------------------------------
import csv
#functions----------------------------------------------
#Main---------------------------------------------------


records = 0
overMax = 0 

print("Room\t\t\t     Max\t     Min\t     Over")

with open("week2\lab2a.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        room = row[0]
        max = int(row[1])
        min = int(row[2])
        over = 0
        records += 1

        if min > max:
            over = min - max
            print("{0:20}\t{1:8}\t{2:8}\t{3:8}".format(room, max, min, over))
            overMax += 1
        
print("\nProcessed {0:3} records.".format(records))
print("There are {0:3} rooms over the limit.".format(overMax))

anyKey = input("\nPress the ENTER key to continue . . .")