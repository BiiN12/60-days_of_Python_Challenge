"""
📘 Day 15: OOP - Encapsulation, Class vs Instance Variables, Special Methods  

1. Encapsulation → hiding data (private attributes)
2. Getters & Setters → controlled access to private data
3. Class vs Instance Variables → shared vs unique
4. Special Methods (__init__, __str__, __repr__) → customizing behavior
"""

# 📝 Practice Exercises

# Exercise 1: Bank Account with Encapsulation
# - Create a BankAccount class with private balance
# - Add methods: deposit, withdraw, get_balance

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f'You deposit ${amount}'
    
    def withdraw(self, amount):
        self.__balance -= amount
        return f'You withdraw ${amount}'
    
    def get_balance(self):
        return f'You have ${self.__balance}'

person1 = BankAccount(3000)
print(person1.deposit(200))
print(person1.withdraw(700))
print(person1.get_balance())

# Exercise 2: Student Grades with Getters & Setters
# - Create a Student class with private grade
# - Add getter and setter (only allow 0–100)

class Student:
    def __init__(self, grade):
        self.__grade = grade
    
    def getter(self):
        return self.__grade
    
    def setter(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade.")

student1 = Student(68)
student1.setter(82)
print(student1.getter())



# Exercise 3: Class vs Instance Variables
# - Create a Car class with class variable wheels = 4
# - Add brand and model as instance variables
# - Show difference between class and instance variables

class Car:
    # Class variable - shared by all instances
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance variables - unique to each instance
        self.brand = brand
        self.model = model
    
    def __str__(self):
        return f"{self.brand} {self.model} with {self.wheels} wheels"


# Create car instances
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Tesla", "Model 3")

print("Initial cars:")
print(f"Car 1: {car1}")
print(f"Car 2: {car2}")
print(f"Car 3: {car3}")

print(f"\nAccessing class variable through class: Car.wheels = {Car.wheels}")
print(f"Accessing class variable through instance: car1.wheels = {car1.wheels}")

# Modify class variable
print("\nChanging Car.wheels to 6...")
Car.wheels = 6
print(f"Car 1: {car1}")
print(f"Car 2: {car2}")
print(f"Car 3: {car3}")

# Modify instance variable (shadows class variable)
print("\nChanging car1.wheels to 3 (instance variable)...")
car1.wheels = 3
print(f"Car 1: {car1}")
print(f"Car 2: {car2}")
print(f"Car 3: {car3}")
print(f"Class variable Car.wheels is still: {Car.wheels}")

# Exercise 4: Book Representation
# - Create a Book class with title and author
# - Implement __str__ and __repr__
# - Print book instances

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        """User-friendly string representation"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Developer-friendly representation for debugging"""
        return f"Book('{self.title}', '{self.author}')"
    

# Create book instances
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Pride and Prejudice", "Jane Austen")

print("Using __str__ method (user-friendly):")
print(book1)
print(book2)
print(book3)

print("\nUsing __repr__ method (debugging):")
print(repr(book1))
print(repr(book2))
print(repr(book3))

print("\nIn a list (uses __repr__):")
books_list = [book1, book2, book3]
print(books_list)

# Exercise 5 (Challenge 🚀): Library System
# - Create a Library class storing Book objects
# - Add methods to add books, list books
# - Use __str__ in Book to print nicely

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # List to store Book objects
    
    def add_book(self, book):
        """Add a Book object to the library"""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print("Error: Can only add Book objects to the library")
    
    def list_books(self):
        """Display all books in the library"""
        if not self.books:
            print(f"{self.name} has no books.")
        else:
            print(f"\n📚 Books in {self.name}:")
            print("-" * 40)
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")  # Uses Book's __str__ method
    
    def find_books_by_author(self, author):
        """Find all books by a specific author"""
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if found_books:
            print(f"\nBooks by {author}:")
            for book in found_books:
                print(f"  - {book}")
        else:
            print(f"No books found by {author}")
    
    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books"
    

# Create library
library = Library("City Central Library")
print(library)

# Add books
print("\nAdding books to library:")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("Animal Farm", "George Orwell"))

# List all books
library.list_books()

# Find books by author
library.find_books_by_author("George Orwell")
library.find_books_by_author("J.K. Rowling")  # Not found

# Try to add invalid object
print("\nTrying to add invalid object:")
library.add_book("Not a book object")

print(f"\nFinal library status: {library}")