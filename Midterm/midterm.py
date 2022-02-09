#Isaiah Diiorio
#2/9/2022
#Midterm

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT: Write a program in Python that reads the data stored in the “midterm.csv” file and stores its data into separates lists. Once the lists have all been populated, process the lists to display all records that have 40 or more points. Next, process the lists again to determine the average number of hits. Last, display all records, one record per line.

#VARIABLE DICTIONARY:
#varName        description of data it will hold
#plrName        this holds a list of all the player names 
#plrRace        this holds a list of all the player races
#plrChar        this holds a list of all the player charter names 
#numHits        this holds a list of all the player hits 
#hits40         this holds the total amount of player hits >= 40 
#avgHit         this holds the avg number of hits between all of the players 

#NOTES: there are 12 rows 

#imports------------------------------------------------
import csv
from numpy import append

#functions----------------------------------------------
def hitTest():
    '''This Function caculates the total number of players whos hits are 40 or higher '''
    hits40 = 0

    for col in range(12):
        if (int(numHits[col]) >= 40):
            
            print("{0:10}\t{1:15}\t{2:10}\t{3:3}".format(plrName[col], plrRace[col], plrChar[col], numHits[col]))
            hits40 += 1

    print("Number of players with 40 or more hits: {0:2}".format(hits40))

def avgHitTest():
    '''This function caculates the average number of hits'''
    avgHit = 0

    for col in range(12):
        avgHit += int(numHits[col])

    avgHit /= 12

    print("\nThe average number of Hits: {0:5.2f}".format(avgHit))

#Main---------------------------------------------------

plrName = []
plrRace = []
plrChar = []
numHits = []

with open("Midterm\Midterm.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:

        plrName.append(row[0])
        plrRace.append(row[1]) 
        plrChar.append(row[2]) 
        numHits.append(row[3])

hitTest()
avgHitTest()