# Day 10: Dictionaries - Practice Exercises

# Exercise 1:
# Create a dictionary called 'car' with keys: 'brand', 'model', 'year'.
# Fill it with any values you like, then print the dictionary.

car = {'brand': 'BMW', 'model': 'unknown', 'year': 2018}
print(car)

# -----------------------------------------

# Exercise 2:
# Access the value of 'brand' from the dictionary you created above
# and print it.

print(car['brand'])

# -----------------------------------------

# Exercise 3:
# Update the 'year' of the car dictionary to a newer year.
# Then print the updated dictionary.

car['year'] = 2022
print(car)
# -----------------------------------------

# Exercise 4:
# Add a new key called 'color' with a value of your choice.
# Then print the dictionary.

car['color'] = 'black'
print(car)
# -----------------------------------------

# Exercise 5:
# Remove the 'model' key from the dictionary.
# Then print the dictionary.

del car['model']
print(car)

# -----------------------------------------

# Exercise 6:
# Loop through the car dictionary and print all keys and values in this format:
# key -> value

for key, value in car.items():
    print(f"{key} -> {value}")

# -----------------------------------------

# Exercise 7:
# Create a dictionary called 'student' with:
#   - name: (string)
#   - age: (integer)
#   - subjects: (a list of 3 subject names)
# Print the whole dictionary.

student = {'name': 'John', 'age': 18, 'subjects': ['Biology', 'English', 'Chemistry']}
print(student)

# -----------------------------------------

# Exercise 8:
# From the 'student' dictionary above, print only the subjects one by one using a loop.

for subject in student['subjects']:
    print(subject)

# -----------------------------------------

# Exercise 9:
# Use the .get() method to safely access a key that doesn't exist (e.g. "grade").
# Print the result.

print(student.get("grade"))

# -----------------------------------------

# Exercise 10 (Challenge):
# Create a dictionary called 'phone_book' where keys are names and values are phone numbers.
# Example:
# {
#    "Alice": "12345",
#    "Bob": "67890"
# }
# 1. Add at least 3 people.
# 2. Print Bob's number.
# 3. Loop through the dictionary and print each person's name and phone number.

phone_book = {
   "Alice": "12345",
   "Bob": "67890"
}

phone_book["John"] = "78302"
phone_book["Tom"] = "35049"
phone_book["Kevin"] = "60532"

print(phone_book['Bob'])

for key, value in phone_book.items():
    print(f"{key}'s phone number is {value}")
