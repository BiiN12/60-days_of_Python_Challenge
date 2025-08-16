# 📅 Day 2 – Variables & User Input
# Lesson:
# - Variables in Python are created with = (no let/const like JS)
# - input() is used to get user input, and always returns a string
# - int(), float(), str() are used for type casting
#
# Exercise:
# 1. Ask the user for:
#    - Their name
#    - Their age
#    - Their favorite programming language
# 2. Print a friendly sentence:
#    "Hello BiiN! You are 23 years old and your favorite language is Python."
# 3. Print how old they’ll be in 10 years
# 4. If their favorite language is Python, print:
#    "You're on the right track!"

# 👉 Write your solution below:

name = input("What is your name: ")
age = int(input(f"How old are you, {name}: "))
fav_programming_language = input("What is your favorite programming language: ")

print(f"Hello {name}! You are {age} years old and your favorite language is {fav_programming_language}")

print(f"In 10 years, you will be {age+10} years old!")

if fav_programming_language.lower() == "python":
    print("You're on the right track 💪")