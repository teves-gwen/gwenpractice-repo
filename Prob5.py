# Write a program that takes a character and tells whether it is consonant or vowel.

char = input("Enter a character: ")

if char in "aeiouAEIOU":
    print("The character is a vowel.")
elif char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
    print("The character is a consonant.")
else:
    print("Invalid input. Please enter a letter.")