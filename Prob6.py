num = int(input("Enter a two-digit number: "))

digit1 = num // 10  # First digit
digit2 = num % 10   # Second digit

sum_digits = digit1 + digit2
print(f"The sum of the digits is {sum_digits}.")
