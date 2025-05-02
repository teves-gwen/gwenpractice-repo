
total_score = 0

print("\nWelcome to GWN10's team quiz!")
print("You will be asked 10 questions. Please answer them correctly.")

print("\n(Gwen Teves) Who is known as the Father of the Philippine Revolution?")
print("a) Jose Rizal             c) Andres Bonifacio")
print("b) Emilio Aguinaldo       d) Antonio Luna")

your_answer1 = input("Enter your answer: ")

if your_answer1 == "c" or your_answer1 == "C":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer1} is incorrect. The correct answer is C.")

print("\n(Gwen Teves) Who was the first president of the Philippines?")
print("a) Manuel L. Quezon      c) Jose P. Laurel")
print("b) Emilio Aguinaldo      d) Ferdinand Marcos")

your_answer6 = input("Enter your answer: ")

if your_answer6 == "b" or your_answer6 == "B":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer6} is incorrect. The correct answer is B.")

print("\n(Gwen) What is the capital of South Korea? ")
print("a) Seoul         c) Incheon")
print("b) Busan         d) Gwangju")

your_answer3 = input("Enter your answer: ")

if your_answer3 == "a" or your_answer3 == "A":
    print("Your answer is correct!")
    total_score += 1
else:
    print(f"{your_answer3} is incorrect. The correct answer is A.")

print(f"\nCongratulations! You got {total_score} out of 10 items.")


    