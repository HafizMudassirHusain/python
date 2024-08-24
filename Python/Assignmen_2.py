#====================================Program No 1============================
#1. Write a program to Print First 10 natural numbers.

for i in range(1, 11):
    print(i)

#====================================Program No 2============================
#2. Write a program to Calculate the sum of all numbers from 1 to a given number.

n = int(input("Enter a number: "))
sum_numbers = sum(range(1, n+1))
print("Sum of numbers from 1 to " + str(n) + "  =  " + str(sum_numbers))


#====================================Program No 3============================
#3. Write a program to print multiplication table of a given number.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

#====================================Program No 4============================
#4. Write a program to display only those numbers from a list (numbers = [12, 75, 150,
#180, 145, 525, 50]) that satisfy the following conditions:
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0:
        if num > 500:
            break
        elif num > 150:
            continue
        print(num)



#====================================Program No 5============================
#5. Write a program to Print list in reverse order using a loop.

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])


#====================================Program No 6============================
# 6. Write a program to display all prime numbers within a range.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(f"Prime numbers between {start} and {end}:")
for i in range(start, end+1):
    if is_prime(i):
        print(i)


#====================================Program No 7============================
# 7. Write a program to Find the factorial of a given number.

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is: {factorial}")



#====================================Program No 8============================
#8. Write a program to find the sum of the series up to n terms.
 
n = int(input("Enter the number of terms: "))
sum_series = sum(range(1, n+1))
print(f"The sum of the series up to {n} terms is: {sum_series}")


#====================================Program No 9============================
#9. Write a Python program to guess a number between 1 and 9.
#Note: User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random

number_to_guess = random.randint(1, 9)

while True:
    guess = int(input("Guess the number between 1 and 9: "))
    if guess == number_to_guess:
        print("Well guessed!")
        break
    else:
        print("Try again.")



#====================================Program No 10============================
#10. Write a Python program that accepts a word from the user and reverses it.

word = input("Enter a word: ")
reversed_word = word[::-1]
print(f"Reversed word: {reversed_word}")



#====================================Program No 11============================
#11. Write a Python program that accepts a string and calculates the number of digits and letters.
#Sample Data: Python 3.2
#Expected Output:
#Letters 6
#Digits 2

input_string = input("Enter a string: ")
letters_count = sum(c.isalpha() for c in input_string)
digits_count = sum(c.isdigit() for c in input_string)

print(f"Letters {letters_count}")
print(f"Digits {digits_count}")



#====================================Program No 12============================
#12. Write a program to calculate the length of string provide input by user (without using len)

input_string = input("Enter a string: ")
length = 0

for _ in input_string:
    length += 1

print(f"Length of the string: {length}")


#====================================Program No 13============================
#13. Write a Python program to print the number of vowels and consonant in your full
#name.

full_name = input("Enter your full name: ").lower()
vowels_count = sum(c in 'aeiou' for c in full_name)
consonants_count = sum(c.isalpha() and c not in 'aeiou' for c in full_name)

print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")



#====================================Program No 14============================
#14. Write a Python program that generates list of values. The values must be taken from user as input.

num_values = int(input("Enter the number of values: "))
user_values = [input(f"Enter value {i + 1}: ") for i in range(num_values)]
print("User values:", user_values)


#====================================Program No 15============================
#15. Write a Python program to copy elements from one list to another.

original_list = [1, 2, 3, 4, 5]
new_list = []

for element in original_list:
    new_list.append(element)

print("Original List:", original_list)
print("Copied List:", new_list)


#====================================Program No 16============================
#16. Write a python program to select the maximum value from list (without using maximum function).

numbers = [3, 7, 1, 9, 4, 5]
max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print("Maximum value:", max_value)


#====================================Program No 17===========================
#17. Write a Python program to count the number of even and odd numbers from a series of numbers. Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = sum(num % 2 == 0 for num in numbers)
odd_count = sum(num % 2 != 0 for num in numbers)

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)




#====================================Program No 18============================
#18. Find the sum of squares of each element of the list using for loop. numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8

numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]
sum_squares = sum(num**2 for num in numbers)

print("Sum of squares:", sum_squares)


#====================================Program No 19============================
#19. From given list: gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]
#a) Create separate lists of strings and numbers.
#b) Sort the strings list in ascending order
#c) Sort the strings list in descending order
#d) Sort the number list from lowest to highest e) Sort the number list from highest to lowest

gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

strings_list = [item for item in gadgets if isinstance(item, str)]
numbers_list = [item for item in gadgets if isinstance(item, (int, float))]

# Sort strings in ascending and descending order
strings_list_asc = sorted(strings_list)
strings_list_desc = sorted(strings_list, reverse=True)

# Sort numbers from lowest to highest and highest to lowest
numbers_list_asc = sorted(numbers_list)
numbers_list_desc = sorted(numbers_list, reverse=True)

print("Strings List (Ascending):", strings_list_asc)
print("Strings List (Descending):", strings_list_desc)
print("Numbers List (Ascending):", numbers_list_asc)
print("Numbers List (Descending):", numbers_list_desc)


