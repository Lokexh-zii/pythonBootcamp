#To print your Name 
#print("Hello zii")

#To print your name using user input
#name = input("Enter your name = ")
#print(name)

# WAP to find the current age
#currentYear = int(input("Enter the current year = "))
#bornYear = int(input("Enter the born year = "))
#ageInYear = currentYear - bornYear
#print(ageInYear)

# WAP for curremcy convertor
# Converting rupee into dollar
#print("Convert rupees into Dollars ")
#rupee = int(input("Enter the amount in rupees = "))
#rsIntoDollar = (rupee / 84)
#print(rupee , "Convert into dollar" , rsIntoDollar)

#coverting dollar into rupee
#print("Convert dollar into rupee")
#dollar = int(input("Enter the amount in dollars = "))
#dollarIntoRs = (dollar * 84)
#print(dollar, "Convert into rupees", dollarIntoRs) 

# Wap to check wheather you are eligible for voting or not 

#userAge=int(input("Enter your age :"))
#if (userAge>17):

 #   print("you are eligible for vote")

#else:
    
 #       print("yor are not eligible for vote")

# Wap to check the user eligible for job application
# if gender is female and age is greater than 17
# if gender is male then they can apply for private job

# userAge=int(input("Enter your age :"))
# gender = input("Enetr your gender = ")
# if (userAge > 17 and gender == "f"):
#     print("You are eligible for govt. job")
# elif(userAge > 17 and gender == "m"):
#     print("You are eligible for private job")
# else:
#     print("You are not eligible for any job")

# Wap to check the greatest no among 3 no

# a=int(input("Enter your first no: "))
# b=int(input("Enter your second no: "))
# c=int(input("Enter your third no: "))

# if(a > b):
#     if(a > c):
#         print(a," is greatest among all three no.")
# elif(b > c):
#     print(b," is greater among all three no.")
# else:
#     print(c, " is greatest among all three no.") 


# TASK :- sir ji ka number = 8527657955, see all videos 

# Switch condition is replacement of multiple if else block 
# List, Tupple, dictionary, are all similar in same conditions
# List :- 
# friendName = ["harsh","ekta","astha"]
# print("before",(friendName) )

# To add the new friend name 
# friendName.append("Maninder") 
# print("after",(friendName))
# print(type(friendName))

# To add the name in specific place
# friendName.insert(0,"pawan") 
# print(friendName)
# friendName.remove("pawan") 
# print(friendName)

# to clear the list
# friendName.clear()

# To sort the list
# friendName.sort()
# print(friendName)


# Loops :- 
# (We use loops for doing repeated tasks)
# 2 types of for loops :- 1. for loops, 2. foreach loop

# friendName = ["harsh","ekta","astha"]
# for names in friendName:
#     print(names) 

# To print the number 1 to 10 :-
# for i in range(10):
#     print(i+1)
# OR
# for i in range(1,11):
#     print(i)

# To print even number from 1 to 10
# for i in range(1,11):
#     if(i%2==0):
#         print(i) 

# SETS USED TO STORE THE DATA AND DATA IS CHANGEABLE
# sets = {"ekta", "harsh", "aastha", "harsh"}
# sets.add("neha")
# sets.remove("neha")
# print(type(sets))  
# print(sets) 

# friendName = ["harsh","ekta","astha","lokesh","maninder","ankur"]
# friendName.sort()
# print(friendName)
# friendName.reverse()
# print(friendName) 


# Exception Handling :- 


# Datetime
# import datetime
# x = datetime.datetime.now()
# print(x) 
# print(x.year)

# Q) Calculate your current age in days (using datetime)
# import datetime
# currentDate = datetime.date.today()
# print(currentDate)
# bornDate = int(input("Enetr your Date of birth"))
# bornMonth = int(input("Enter your born month"))
# nornYear = int(input("Eneter your born year"))

# print(age)


# File handeling :-

# name = input("Enter your name")
# email = input("Enetr your email")
# collegeName = input("Enter your college name")
# data = name + email + collegeName

# f = open("lokesh.txt","w")

# f.close()
# import os 
# os.remove("lokesh.txt")

#Q) add data in json,excel, csv and read it 
# Creating the json file
f = open("lokesh.json","w")
f.close()

# Creating the excel file
f = open("lokesh.xlsx","w")
f.close()

# Creating the csv file
f = open("lokesh.csv","w")
f.close()

# while loop print 1 to 10
# i = 10
# while i > 0:
#     print(i)
#     i = i-1 


# Function in python
# def myFunction():
#     print("my function called")
#     myFunction()  

# def area(x,y):
#     z = x*y
#     print("area is : ", z)

# w = int(input("Eneter the value of x :"))
# h = int(input("Eneter the value of y :"))

# area2 = area(w,h)

# Q) Make a function for the n'factorial.
# number = int(input("Enetr the number of which you want a factorial :- "))
# factorial = 1
# i = 1
# while i != number+1 :
#     factorial = i*factorial
#     i = i + 1
# print("The Factorial of ",number," is ",factorial)



 

    
     