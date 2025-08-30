# -------------------------------
# Day 13: Error Handling in Python
# -------------------------------

# Why Error Handling?
# - Errors can happen anytime (wrong input, missing file, zero division, etc.)
# - Instead of crashing the program, we can "handle" these errors gracefully.

# -------------------------------
# Try & Except
# -------------------------------
# - Code that might fail goes inside "try"
# - Errors are caught inside "except"
#
# Example:
# try:
#     x = int("abc")   # This will cause ValueError
# except ValueError:
#     print("Invalid input!")

# -------------------------------
# Catching Multiple Errors
# -------------------------------
# - You can have multiple "except" blocks for different errors
#
# Example:
# try:
#     num = 10 / 0
# except ValueError:
#     print("Not a number")
# except ZeroDivisionError:
#     print("You can't divide by zero")

# -------------------------------
# Else Block
# -------------------------------
# - "else" runs if no exception occurs
#
# Example:
# try:
#     print("Hello World")
# except:
#     print("Error occurred")
# else:
#     print("No error happened!")

# -------------------------------
# Finally Block
# -------------------------------
# - "finally" always runs (good for cleanup)
#
# Example:
# try:
#     file = open("data.txt")
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     print("Execution finished")

# -------------------------------
# Raising Errors
# -------------------------------
# - You can raise your own errors with "raise"
#
# Example:
# age = -5
# if age < 0:
#     raise ValueError("Age cannot be negative!")

# -------------------------------
# Custom Exceptions
# -------------------------------
# - You can create your own exception types
#
# Example:
# class TooSmallError(Exception):
#     pass
#
# number = 5
# if number < 10:
#     raise TooSmallError("Number is too small!")


# ---------------- Day 13: Error Handling — Practice Exercises ----------------

# Exercise 1: Divide Numbers Safely
# - Ask user for two numbers
# - Try to divide them
# - Handle ValueError and ZeroDivisionError

def exercise1():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        div = num1/num2
        return div
    except ValueError:
        print("Please enter a number.")
    except ZeroDivisionError:
        print("You can't divide by zero!")

exercise1()

# Exercise 2: File Reader
# - Try opening "data.txt"
# - If file not found, print message
# - Always print "Execution finished" using finally

def exercise2():
    try:
        with open("data.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("File not found! Please check the file name.")
    finally:
        print("Execution finished")

exercise2()

# Exercise 3: Age Validator
# - Ask user for their age
# - If age < 0, raise ValueError("Age cannot be negative!")
# - Otherwise, print the age

def exercise3():
    try:
        age = int(input("How old are you? "))
        if age < 0:
            raise ValueError
    except ValueError:
        print("Age cannot be negative!")
    else:
        print(age)

exercise3()

# Exercise 4: Custom Exception
# - Create custom exception TooSmallError
# - Ask user for a number
# - If number < 10, raise TooSmallError
# - Handle exception and print "Number is too small!"

class TooSmallError(Exception):
    pass

def exercise4():
    try:
        num = int(input("Enter a number: "))
        if num < 10:
            raise TooSmallError("Number is too small!")
    except TooSmallError as e:
        print("Custom Exception:", e)
    except ValueError:
        print("Please enter a number!")

exercise4()

# Exercise 5: Multiple Exceptions
# - Ask user for numerator and denominator
# - Try to divide them
# - Handle ValueError and ZeroDivisionError
# - Use else block to print "Division successful!" if no error

def exercise5():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        div = num1/num2
    except ValueError:
        print("Please enter a number.")
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print("Division successful!")
        return div

exercise5()
