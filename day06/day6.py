# 📅 Day 6: Strings in Python
# Lesson:
# - Concatenation: "Hello " + "World"
# - Repetition: "Ha" * 3
# - Indexing & slicing: text[0], text[-1], text[0:4], text[::-1]
# - String methods: .upper(), .lower(), .strip(), .replace(), .split(), .count()
# - f-strings: f"Hello {name}"
#
# Exercise:
# 1. Ask user for first and last name
#    - Print "Hello, FIRST LAST" in uppercase
# 2. Ask user for a word
#    - Print first char, last char, and the reversed word
# 3. Replace "Python" with "coding" in "I am learning Python"
# 4. Bonus: Ask user for a string
#    - Print number of characters, number of words, and count of "a"
#
# 👉 Write your solution below:

#1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello, {first_name} {last_name}")

#2
word = input("Enter a word: ")
word_reverse = word[::-1]
print(f"The first character of the word is {word[0]} and the last is {word[-1]}\n The reverse of {word} is {word_reverse}")

#3
python = "I am learning Python"
print(python.replace("Python", "coding"))

