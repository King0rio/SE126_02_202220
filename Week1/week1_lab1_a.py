#Isaiah Diiorio
#Lab 1
#1/31/2022

#Program Essentials with Python, SE116, and .21
#PROGRAM PROMPT: Write a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. 

#VARIABLE DICTIONARY:
#varName        description of data it will hold
#anwser         the condition to keep the program running 
#capacity       the total ammount of people the room can handle 
#attendees      the total ammount of people that want to attend the confrence 
#register       the value needed to print eather the excess people or the ammount that can still be invited 

#NOTES: 

#imports------------------------------------------------
#functions----------------------------------------------
#Main---------------------------------------------------

print("Hello And Welcome To My Meeting Fire and Safety Caculator!")

anwser = "y"


while anwser.lower() == "y":

    capacity = int(input("\nWhat is the Capacity of the room? "))
    attendees = int(input("How many people want to attend the event? "))

    if capacity > attendees:
        register = capacity - attendees
        print("\nThe Coffrence can be Held. {0} more people can attend.\n".format(register))
    else:
        register = attendees - capacity
        print("\n{0} people have to be told they can not attend the meeting.\n".format(register))
    
    anwser = input("Do you Want to check any more rooms? [Y/N]: ")