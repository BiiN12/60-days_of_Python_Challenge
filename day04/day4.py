# 📅 Day 4: Conditional Statements (if, elif, else)
# Lesson:
# - if statement: executes code only if condition is True
# - if...else: provides an alternative path
# - if...elif...else: multiple conditions checked in order
# - Logical operators: and, or, not
#
# Exercise:
# 1. Ask the user for their age:
#    - If under 13 → print "Child"
#    - If between 13 and 19 → print "Teenager"
#    - If 20 or above → print "Adult"
#
# 2. Ask the user for a number:
#    - Print if it’s "Positive", "Negative", or "Zero"
#
# 3. Mini login system:
#    - Preset: username = "admin", password = "1234"
#    - Ask the user for username & password
#    - Print "Login successful" if both match, otherwise "Access denied"
#
# 👉 Write your solution below:

#1
age = int(input("How old are you? "))

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20:
    print("Adult")
else:
    print("Please enter positive number!")

#2
num = int(input("Enter any number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#3
username = "admin"
password = "1234"

username_in = input("Enter your username: ")
password_in = input("Enter your password: ")

if username_in == username and password_in == password:
    print("Login successful")
else:
    print("Access denied")