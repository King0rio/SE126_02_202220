#Isaiah Diiorio
#3/7/2022
#Lab9

#Intermediate Programming Using Python, SE126, and .02
#PROGRAM PROMPT:

#VARIABLE DICTIONARY:
#varName        description of data it will hold


#NOTES: 

#imports------------------------------------------------
import csv
#functions----------------------------------------------
def swap(list, num):
    '''swap'''
    temp = list[num]
    list[num] = list[num + 1]
    list[num + 1] = temp

def sort(list1, list2):
    '''sorts a list from lowest to highest'''
    lenOfList = len(list1)
    for y in range(0, lenOfList):
        for x in range (0, lenOfList-1):
            if (list1[x] > list1[x+1]):
                swap(list1, x)
                swap(list2, x)
#Main---------------------------------------------------
#fullName = []
lname = []
fname = []

with open('week9\Lab9.csv') as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        #fullName.append([row[1], row[0]])
        fname.append(row[0])
        lname.append(row[1])
csvfile.close()
#print(fullName)

sort(lname, fname)
with open('E:\Python126\Lab9BWrite.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(lname)
    writer.writerow(fname)
csvfile.close()
