# Write a program that takes 3 numbers and prints the highest number.

num1 = (input("Enter first number: "))
num2 = (input("Enter second number: "))
num3 = (input("Enter third number: "))
number1 = int(num1)
number2 = int(num2)
number3 = int(num3)

temp_highest = number1 # Assume the first number is the highest

if number2 > temp_highest: 
    temp_highest = number2 
if number3 > temp_highest: 
    temp_highest = number3

print(f"The highest number is {temp_highest}.")

