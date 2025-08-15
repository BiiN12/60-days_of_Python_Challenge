# This is a comment in Python
print("Hello, Python!")  # Printing text

# Variables
name = "BiiN"
age = 23
print(f"My name is {name} and I am {age} years old.")

# Difference from JS:
# - No let/const/var, just name = value
# - Strings can use single or double quotes

# Today's Key Concept: Indentation
# In Python, indentation is part of the syntax, not just style.

# Example:
if age > 18:
    print("You're an adult")  # Must be indented



#############################

# Exercise (Day 1)

# Print:
# 1. Your name
# 2. Your favorite programming language
# 3. Your age in 5 years (calculated, not hardcoded)
# 4. Add a conditional that prints "That's awesome!" if your favorite language is Python.

fav_programming_language = "Python"

print(name)
print(f"My favorite programming language is {fav_programming_language}!")
print(f"In 5 years, I will be {age + 5} years old")

if fav_programming_language == "Python":
    print("That's awesome!")
