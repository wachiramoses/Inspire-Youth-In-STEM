#create an empty list of vavourite musicians
#using for loop add 5 new musicians
#copy the list to a new list calledcelebs
#sort the listpop out 2 celebrity to the list
#count the remaining celebs


#!usr/bin/env python3
#This is a single line comment
#python assignment
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 20th Feb 2023
#File : assignment.py



#create an empty list of favourite musicians
fav_musicians = []

#using for loop add five new musicians
print("Enter five names of your favourite musicians:")
for musician in range(0,5):
    the_musicians = input("Enter name:")
    fav_musicians.append(the_musicians)
print(fav_musicians)

#copy the list to a new list called celebs 
celebs = fav_musicians.copy()
print(celebs)

#sort the list
celebs.sort()
print(celebs)

#pop out two celebrities
celebs.pop()
celebs.pop()
print(celebs)

#count the remaining celebrities in the list
print(len(celebs))

