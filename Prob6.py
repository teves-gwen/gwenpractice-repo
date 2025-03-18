# Write a program that takes a 2 digit number and returns the sum of the 2 digits. Ex. 24 -> 6

num = (input("Enter a two-digit number: "))
num = int(num)

digit1 = num // 10  
digit2 = num % 10   

sum_digits = digit1 + digit2
print(f"The sum of the digits is {sum_digits}.")

