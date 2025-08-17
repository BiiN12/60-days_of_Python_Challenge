# 📅 Day 3 – Operators in Python
# Lesson:
# - Arithmetic operators: +, -, *, /, //, %, **
# - Comparison operators: ==, !=, <, >, <=, >=
# - Assignment operators: +=, -=, *=, etc.
# - Logical operators: and, or, not
#
# Exercise:
# 1. Create variables a = 9, b = 2
#    - Print results of all arithmetic operators
# 2. Compare a and b with all comparison operators
# 3. Start with x = 5
#    - Update it step by step using +=, -=, *=, printing after each
# 4. Mini login check:
#    - username = "admin", password = "1234"
#    - Ask user for username & password
#    - Print "Login successful" if both match, else "Access denied"
#
# 👉 Write your solution below:


#1 
a = 9
b = 2


print(a + b)   # 19  (addition)
print(a - b)   # 11  (subtraction)
print(a * b)   # 60  (multiplication)
print(a / b)   # 3.75 (division, always float)
print(a // b)  # 3   (floor division – no decimals)
print(a % b)   # 3   (remainder)
print(a ** b)  # 50625 (power)

#2
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= 9) # True
print(b <= 2)  # True

#3
x = 5

x += 2
x -= 2
x *= 2
print(x) #10

#4
username = "admin"
password = "1234"

username_in = input("Enter your username: ")
password_in = input("Enter your password: ")

if username_in == username and password_in == password:
    print("Login successful")
else:
    print("Access denied")