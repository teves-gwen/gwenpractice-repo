char = input("Enter a character: ").lower()

if char in "aeiou":
    print("The character is a vowel.")
elif char.isalpha():
    print("The character is a consonant.")
else:
    print("Invalid input. Please enter a letter.")  