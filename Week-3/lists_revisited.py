#!usr/bin/env python3
#This is a single line comment
#python program on lists revisited
#Name : Moses Wachira
#Email : wachiramoses519@gmail.com
#Date : 21st Feb 2023
#File : lists_revisited.py


myFavouriteFruits = ["banana","apple","mango","lime","avocado"]

for fruit in myFavouriteFruits:
    print(fruit)

print(len(myFavouriteFruits))

friends = ["wachira","mose","jayden","kelvin","paul"]
print(friends)
friends[5] = "mary"
print(friends)
print("-----------------------------------------------------")
new_friends = friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)