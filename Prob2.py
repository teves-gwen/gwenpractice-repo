# Write a program that takes a number and tell whether the number is odd, even, or zero.

num = (input("Enter a number: "))
num1 = int(num)

if num1 == 0:
    print("The number is zero.")
elif num1 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

