# # Assignment 1 :-

# # Find the Age in Year using python when birt year given 

# currentYear = int(input("Enter the current year :"))
# myBirthYear = int(input("Enter your birth year : "))
# print(f"Your Age according {currentYear} is ", (currentYear - myBirthYear))



# # Assignment 2:-

# # Create BMI calculator in Python

# height = float(input("Enter the height in cm: "))  
# weight = float(input("Enter the weight in kg: "))  
# # function for BMI  
# BMI = weight / (height/100)**2  


# print("Your Body Mass Index is", BMI)
  
# if BMI <= 18.5:  
#     print("Oops! You are underweight.")  
# elif BMI <= 24.9:  
#     print("Awesome! You are healthy.")  
# elif BMI <= 29.9:  
#     print("Eee! You are over weight.")  
# else:  
#     print("Seesh! You are obese.")  



# # Assignment 3 :-

# # Create Currency Convertor in Python

# # 1st convert Ruppes into Dollars :-

# print(" Convert Ruppes into Dollars ")
# rsAmount = int(input("Enter the amount in Rs. : "))
# rsIntoDollar = (rsAmount / 84)
# print(rsAmount, " convert into dollar ", rsIntoDollar)


# # 2nd Convert Dollar into Ruppes :-

# print(" Convert Dollar into Ruppes ")
# dollarAmount = int(input("Enter the amount in Dollar. : "))
# dollarIntoRs = (dollarAmount * 84)
# print(dollarAmount, " convert into ruppes ", dollarIntoRs)


String otp= new DecimalFormat("000000").format(new Random().nextInt(999999));
System.out.println(otp);