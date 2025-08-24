# 📅 Day 8: Functions — Complete Guide
# Exercise
# Define functions for:
# add(a, b) →print(s sum of a + b
# subtract(a,) b) → returns a - b
# multiply(a, b) → returns a * b
# divide(a, b) → returns a / b (handle division by zero safely)

# User input:
# Ask the user for two numbers.
# Ask the user to choose an operation: +, -, *, /.
# Perform calculation:
# Call the correct function depending on user’s choice.
# Display the result in a clear format, e.g., “5 * 3 = 15”.
# Loop until exit:
# After showing the result, ask if the user wants another calculation.
# If they type "no", exit the program. If "yes", repeat.

# --Write your code here--
def calculator(first_number, second_number, operator):
    if operator == '+':
        print(first_number + second_number)
    elif operator == '-':
        print(first_number - second_number)
    elif operator == '*':
        print(first_number * second_number)
    elif operator == '/':
        print(first_number / second_number)
    
while True:
    print("Please enter two numbers and operator(Enter 'q' for quit)")
    first = input("Enter the first number('q' for quit): ")
    if first == 'q':
        print("Goodbye!")
        break
    second = input("Enter the second number: ")
    if second == 'q':
        print("Goodbye!")
        break
    operator = input("Choose an operator(+, -, *, /): ")
    if operator == 'q':
        print("Goodbye!")
        break
    calculator(int(first), int(second), operator)