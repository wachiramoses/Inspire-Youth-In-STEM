#Advanced Data types

#Mutable and Immutables
#Muatables Data types that can be edited during program life cycle you can add / remove elements
#Immutables - Data types that cannot be edited during programs life cycle

# 1)List(Mutable) 
friends = ["food","sleep"]
print(friends)
# or friends = [] for empty list
# add ---> append(), extend()

students = ["Marie","Kigen","Serphine"]
friends.extend(students)
friends.append("james")
friends.sort()
friends.reverse()
print(friends)

# 2)Tuples(Immutable)
#Type of list that are immutable

stationarys = ("pens","ink","sharpener")

#replace the whole tuple
stationarys = ("ruler","clipboard","pencil")
print(stationarys)
#for stationarys in stationary:
for stationary in stationarys:
    print(stationary)

#numbers = (1,2,3,4,5)
#3)Dictionaries aka dict
#dictionaries uses key and value pair
student = {"name" : "Wachira","age":24,"gender":"male","is_tall":True}
#"name" : "Wachira" --->name(key) wachira(value)
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])
print(student.values())
print(student.keys())

friend = {"fav_color" : "Grey","hobby" : "Playing_video_games", "course": "Engineering", "weight": 90,"height":250}
print(friend["fav_color"])
print(friend["hobby"])
print(friend["course"])
print(friend["weight"])
print(friend["height"])
print(friend.values())
print(friend.keys())