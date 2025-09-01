# ---------------------------
# Day 14 – OOP Overview
# ---------------------------

# OOP = Object-Oriented Programming
# - Classes = Blueprints
# - Objects = Instances (things created from the blueprint)
# - Attributes = Variables inside a class
# - Methods = Functions inside a class
# - __init__ = Special constructor method that runs when creating an object

# Example:
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(f"{self.name} is barking!")

# dog1 = Dog("Buddy", 3)
# dog1.bark()

# ---------------------------
# Practice Exercises
# ---------------------------

# Exercise 1: Create a Car class
# - Attributes: brand, year
# - Method: display_info() → print details
# - Create 2 cars and display their info

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def display_info(self):
        print(f"Car: {self.brand}, Year: {self.year}")

print("=== Car Tests ===")
car1 = Car("Toyota", 2020)
car2 = Car("BMW", 2022)
car1.display_info()
car2.display_info()

# Exercise 2: Dog class
# - Attributes: name, breed
# - Method: bark() → "<name> is barking"
# - Create 2 dogs and make them bark

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} is barking"
    
print("\n=== Dog Tests ===")
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")
print(dog1.bark())
print(dog2.bark())

# Exercise 3: Student class
# - Attributes: name, grade
# - Method: is_passing() → "Passing" if grade >= 50 else "Failing"
# - Create 3 students and test

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def is_passing(self):
        return "Passing" if self.grade >= 50 else "Failing"
    
print("=== Student Tests ===")
s1 = Student("Alice", 85)
s2 = Student("Bob", 45)
s3 = Student("Charlie", 70)
print(f"{s1.name}: {s1.is_passing()}")
print(f"{s2.name}: {s2.is_passing()}")
print(f"{s3.name}: {s3.is_passing()}")

# Exercise 4: Book class
# - Attributes: title, author, pages
# - Method: summary() → "Title by Author, X pages"
# - Create 2 books and display summary

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

print("\n=== Book Tests ===")
b1 = Book("1984", "George Orwell", 328)
b2 = Book("Python Crash Course", "Eric Matthes", 544)
print(b1.summary())
print(b2.summary())

# Exercise 5 (Challenge 🚀): BankAccount
# - Attributes: owner, balance
# - Methods: deposit(amount), withdraw(amount)
# - Create account and test deposit/withdraw

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds!")

print("\n=== BankAccount Tests ===")
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)