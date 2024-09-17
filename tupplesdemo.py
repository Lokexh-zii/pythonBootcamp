# Tuples can store the multiple data and data can't change 
# myTuple = ("Ekta", "Harsh", "Astha","Astha")
# print(type(myTuple))
# print(myTuple)

# # To access a particular value 
# print(myTuple[1])

# # can tupple change ?
# # myTuple[1] = "Maninder"
# # print(myTuple)

# for x in myTuple:
#     print(x)


# Dictionary = It can store multiple data in key value pair
# myDict = {
#     "name" : "Ekta",
#     "age" : 20,
#     "Mobile" : 8882508299
# }

# print(type(myDict))
# print(myDict)

# # printing the values by for loop :-
# for item in myDict:
#     print(myDict[item])

# # To print the specific key :- 
# print(myDict.get("name"))

# # To change the value of any key 
# myDict["name"] = "Lokesh"
# print(myDict)

# We use list for similar info. & use dictionary for different infos.

# oops :-
# Class :- it is blueprint of objects or real world entity./collection of functions and objects 

# class Mca:
#     age = 20
#     print("2024-26")

# # create object and class properties :-
# x = Mca()
# print(x.age)

# Q) create a class of name "age calculator", and take input of user dob and calculate the age in years.

# class AgeCalculator:
#     dob = int(input("Enter your year of birth : "))
#     cd = int(input("Enter the current year : "))
#     realage = cd - dob
# n = AgeCalculator()
# print("Your age is :", n.realage)

# POLYMORPHISM :- 
# Method overloading :- 

def age(dob1):
    print(dob1)

def age(dob,name):
    print(dob,name)

# x = age("19 oct 1991")
y = age("19 oct 1991", "Ekta")






