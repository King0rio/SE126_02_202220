






from http.client import FOUND


name = ["adam", "april", "betty", "bill", "carl", "cathy"]
#          0       1        2        3       4       5
'''
index
name[3] = bill
                         carl^2            carl^4
                       if(name[2#2 is guess]<target):
                              min = guess + 1
                       else:
                           max = guess - 1 
                        guess = int((min+max)/2)
'''


min = 0
max = len(list)-1
guess = int((min + max)/2)
#what are you looking for in the list? prompt the user = target(carl) input ("        ")

'''
1st guess = int(0+5)/2 = 2 | compare name[2] = carl
2nd guess = int(3+5)/2 = 4 | compare name[4] = carl


while (min - max) and (name[guess]!= target)

'''

'''
if(name[guess] == target):
    #FOUND
    print("")
else:
    #not found
    print("")
'''
