# 📅 Day 7: Functions in Python
# Lesson:
# - Define with def: def my_function():
# - Call with: my_function()
# - Parameters let you pass data
# - return gives back a value
#
# Exercises:
# 1. square(number)
# 2. is_even(number)
# 3. greet_user(name)
# 4. calculate_average(numbers)
# 5. Bonus: simple calculator with +, -, *, /
#
# 👉 Write your solutions below:


#1
def square(number):
    return number**2

print(square(7))

#2
def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False

print(is_even(2))

#3
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

greet_user("John")

#4
def calculate_average(numbers):
    total = int()
    for i in numbers:
        total += i
    return total/len(numbers)

print(calculate_average([3, 7, 21, 9, 4]))

#Bonus:
def calculator(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    
print(calculator(7, 3, '+'))