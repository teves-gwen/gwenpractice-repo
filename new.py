# print the prime numbers from n to m
"""
n = int(input("Enter n: "))
m = int(input("Enter m: "))

for number in range(n, m):
    if number == 1:
        continue # skip the number 1 lang
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number, end=', ')
"""
"""number = int(input("Enter a number: "))

first_number = number // 10
second_number = number % 10
sum = first_number + second_number

while number != 0:
    sum += number % 10
    print(sum)
    print(number // 10)
    number //= 10
print(sum)"""

#anything = ['apples', 'bananas', 'oranges', 1, 2, 3]

#print(anything[0]) #output: apples
#print(anything[3:6]) #output: [1, 2, 3]

#bool = True
#if not bool:
#    print("Yehey")
#else:
#    print("NO")

# output: NO

#word = "Hello"

#def greet(word):
#    word = "Hi"
#    print(word)

#greet(word)

# output: Hi

# --------------------------------------------

# List examples

"""
List = [1, 2, 3]
List.append(4) # magdagdagdag ng 4 sa list
print(List) # output: [1, 2, 3, 4]

List.insert(1, 5) # insert 5 at index 1
print(List) # output: [1, 5, 2, 3, 4]

List.remove(3) # alisin yung 3
print(List) # output: [1, 5, 2, 4] bale 3 yung natanggal

List.pop(1) # alisin yung index 1
print(List) # output: [1, 2, 4] 5 yung natanggal

List.clear() # clear the list
print(List) # output: []
"""
"""
fruits = ['apple', 'banana', 'cherry']
print(len(fruits) - 1) # length of fruits is 3 so 2 is the last index.
# output: 2

fruits[0] # this returns 'apple'
fruits[1] # this returns 'banana'

fruits[-1] # returns 'cherry'
fruits[-2] # returns 'banana'

fruits = ['Cherry', 'Apple', 'Orange', 'Mango', 'Pineapple']
print(fruits[3])
print(fruits[-4])
fruits[3] = 'Papaya'
fruits[-4] = 'Guava'

fruits = ['Cherry', 'Apple', 'Orange']
print(fruits)
fruits[1] = 'Durian'
print(fruits)"""

#fruits = ['Cherry', 'Apple', 'Orange', 'Mango']
#for fruit in fruits: 
#    print(fruit)

# another example

#for i in range(1,11): # kaya 11 yan tapos hanggang 10 lang ma print, kasi exclusive yung 11
#    print(i) # range is a built-in function thatt generates a sequence of numbers

# another example

"""
def number(n, m): 
    for i in range(n, m + 1): 
        print(i)

#main function
n = (input("Enter n: "))
int_n = int(n)
m = (input("Enter m: "))
int_m = int(m)

number(int_n, int_m)"""

#for number in range (5, 10, 2):
#    print(number)

#while True:
#    print("Hello")

"""message = "Starting loop"

while message != "Exit":
    print (message)
    message = input("Enter your message: ")
print("Loop Ended")

# magra-run sya unless i-type ko ang "exit"""

"""
for number in range (1, 11):
    if number == 7:
        continue # mawawala yung 7
    print(number)

for number in range (1, 11):
    if number == 7:
        break # titigil na siya sa 7
    print(number)"""
"""

message = "S a b r i n a"
def greet():
    message = "H i !"
    print(message)
greet()
print(message) # nauna ma print ung hi kasi naunang ma call yung function for that.

is_happy = True
# 
"""
"""
number = input("Enter a number: ")
float_number = float(number)

print(float_number)"""

# example of nested list
"""
fruits = ["Strawberries", "Spinach", "Kale"]
vegetables = ["Tomatoes", "Celery", "Potatoes"]
food = [fruits, vegetables]
print(food)"""

# repeating codes
"""fruits = ['Cherry', 'Apple', 'Orange']
print(fruits[0])
print(fruits[1])
print(fruits[2])"""

"""for number in range(10):
 print(number)
# output: 1 to 9

for number in range(5, 10):
 print(number)
# output: pprint lang yun 5 to 9"""

#for number in range (5, 10, 6):
#    print(number)

"""message = "S a b r i n a"
def greet():
    message = "H i !"
    print(message)

greet()
print(message) # nauna ma print ung hi kasi naunang ma call yung function for that.

message = "Hello World!" # global scope
def greet():
    message = "Hi There!" # local scope
    print(message)

greet()
print(message)"""

# precedence - pagkakasunod sunod

# global keyword

"""def greet():
 global message
 message = "YEy"
greet()
print(message)"""

# output: YEy

"""message = "Hello World!"
def greet():
    global message # dahil dito, nagiging iisang value na lang sila nung global at local
    message = "Hi There!"
    print(message)
greet()
print(message)"""

"""def greet(msg):
 print(f"Greetings: {msg}")
greet("Hello World!")"""

"""def greet(message, sender, receiver):
 print(f"To: {receiver}!")
 print(f"Message: {message}")
 print(f"From: {sender}")

greet("Welcome to the team!", "Steven", "John")"""

# output:
#To: John!
#Message: Welcome to the team!
#From: Steven

"""def celsius_to_fahrenheit(celsius):
 farenheit = (celsius * 9/5) + 32
 return farenheit

celsius = celsius_to_fahrenheit(36)
print(celsius)"""

def get_sum_of_digits(value):
    if not value.isdigit():
        print("Not a number.")
        return 0
    
    tens_digit = int(value[0])
    ones_digit = int(value[1])
    return tens_digit + ones_digit

user_input = input("Enter a 2 digit number: ")
print(get_sum_of_digits(user_input))
