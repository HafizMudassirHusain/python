
#===============================Question No 1======================
#Write a python program to assigning grades(A,B,C) based on marks obtained by a student
#if the percentage is above 90, assign grades A 
#If the percentage is above 75, assign grades B 
#If the percentage is above 65, assign grades C

def marksheet_grade(obtained_marks):
    percentage = (obtained_marks / 100) * 100
    if percentage > 90:
        return 'A'
    elif percentage > 75:
        return 'B'
    elif percentage > 65:
        return 'C'
    else:
        return 'Below C'
# Taking input for marks
marks_obtained = float(input("Enter the marks obtained: "))
grade = marksheet_grade(marks_obtained)
print("The grade is: " + grade)

#=======================================Question no. 2==================================
#Write a program to check if the number entered by user is positive and negative. 

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative”)
else:
    print("The number is zero")

#======================================Question no. 3===================================
#Write a program to check if the number entered by user is even or odd?

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#=======================================================Question no. 4===============================
#Write a program to check if the number entered by user is prime or not?

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number: ")
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")




#Write a program to print hello if number is enters a number that us divisible by 7
#==========================================5=====================================
number = int(input("Enter a number: "))
if number % 7 == 0:
    print("Hello")
else:
    print("Number is not divisible by 7.")



#======================================6====================================
#write a program to print lowest number from the two values provided by the user?

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 < number2:
    print("The lowest number is: " + str(number1))
else:
    print("The lowest number is: " + str(number2))


#======================================7====================================
#write a program to check if the character entered by user is vowel or consonant

char = input("Enter the character: ")
char = char.lower()
if char.isalpha() and len(char) == 1:
    if char in 'aeiou':
        print(char + " is a vowel.")
    else:
        print(char + " is a consonant.")
else:
    print("Please enter a single alphabet character.")


#====================================8=========================================
#write the program that takes the dimensions (length of sides) of triangle to identify 
#if the triangle is right triangle.

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
sides = [side1, side2, side3]
sides.sort()
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("It is a right-angled triangle.")
else:
    print("It is not a right-angled triangle.")


#=====================================9=============================================
#write a program that solve quadratic equation and print  the output only if the roots are real

import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    print(f"The roots of the quadratic equation are real:")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
else:
    print("The roots are complex and not real.")

#===========================================10==================================================
#write a program that displays  .Kamran Akmal on output, if score>30, Shoaib Akhtar if 20< score<30,
#and Shahid Afridi if 10< score<20

score = int(input("Enter the score: "))
if score > 30:
    print(".Kamran Akmal")
elif 20 < score <= 30:
    print("Shoaib Akhtar")
elif 10 < score <= 20:
    print("Shahid Afridi")
else:
    print("Score is below 10.")


#===========================================11=========================================================
#write a program that takes password from user as input, validate the program on the following criteria:
#password length between 7 to 15 character which contain at least one numeric digit and  special character is acceptable

import re

def validate_password(password):
    if 7 <= len(password) <= 15:
        if re.search(r'\d', password):
            if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', password):
                return True
            else:
                print("Password must contain at least one special character.")
        else:
            print("Password must contain at least one numeric digit.")
    else:
        print("Password length must be between 7 and 15 characters.")
    return False

password = input("Enter your password: ")

# Validating the password
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")

#=================================================12===================================================
#write a program to check if user has entered  an upper_case character or lower-case character(use 'ord' fuction and ASCII codes).


character = input("Enter a character: ")

if len(character) == 1:
    ascii_code = ord(character)
    if 65 <= ascii_code <= 90:
        print("You entered an uppercase character.")
    elif 97 <= ascii_code <= 122:
        print("You entered a lowercase character.")
    else:
        print("You did not enter an alphabetical character.")
else:
    print("Please enter only one character.")

==========================================================13================================================
#Write a Python program to check if a character entered by the user is an alphabet or not. If the user enters more than one character as input, the program prints some appropriate error message and exit.

character = input("Enter a character: ")

if len(character) == 1 and character.isalpha():
    print("You entered an alphabet character.")
else:
    print("Please enter only one alphabet character.")


#=========================================================14=================================================
# Write a Python program that requests five integer values from the user. It then prints one of two things: if any of the values entered are duplicates, it prints "DUPLICATES"; otherwise, it prints "ALL UNIQUE".

values = []
for i in range(5):
    value = int(input(f"Enter integer value {i + 1}: "))
    values.append(value)

if len(values) == len(set(values)):
    print("ALL UNIQUE")
else:
    print("DUPLICATES")


#============================================================15===============================================
#Write a Python program that requests an integer value from the user. If the value is between 1 and 100 inclusive, print "OK"; otherwise, do not print anything

value = int(input("Enter an integer value: "))


if 1 <= value <= 100:
    print("OK")



