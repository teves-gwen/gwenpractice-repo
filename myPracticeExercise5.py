# QUIZ
total_score = 0

print("Welcome to GWN10's team quiz!")

print("(Gwen) What is the capital of the Philippines? ")
print("a. Cebu")
print("b. Manila")
print("c. Davao")
print("d. Quezon City")

question1 = input("Enter your answer: ")

if question1 == "b" or question1 == "B":
    print("Correct!")
    total_score += 1
else:
    print(f" {question1} is incorrect. The correct answer is B.")

print("(Gwen) What is the capital of Japan? ")
print("a. Tokyo")
print("b. Kyoto")
print("c. Osaka")
print("d. Nagoya")

question2 = input("Enter your answer: ")

if question2 == "a" or question2 == "A":
    print("Correct!")
    total_score += 1
else:
    print(f" {question2} is incorrect. The correct answer is B.")

print("(Gwen) What is the capital of South Korea? ")
print("a. Seoul")
print("b. Busan")
print("c. Incheon")
print("d. Daegu")

question3 = input("Enter your answer: ")

if question3 == "a" or question3 == "A":
    print("Correct!")
    total_score += 1
else:
    print(f" {question3} is incorrect. The correct answer is A.")

print("You're now done with the quiz. Thank you for participating!")
print("Your total score is: ", total_score)


    