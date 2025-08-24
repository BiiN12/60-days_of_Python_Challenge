# Functions You’ll Build
### String tools
# 1.Normalize text
# Function: normalize(text)
# Converts input to lowercase and strips spaces.
# Example: " Hello World " → "hello world"

# 2.Word count
# Function: word_count(text)
# Splits by spaces and returns number of words.
# Example: "Python is fun" → 3

# 3.Palindrome check
# Function: is_palindrome(word)
# Returns True if word reads the same forward/backward.
# Example: "level" → True

### Number tools
# 4.Average
# Function: average(numbers)
# Takes a list of numbers and returns the average.

# 5.Even/Odd filter
# Function: filter_even_odd(numbers, choice)
# choice = "even" → returns only even numbers
# choice = "odd" → returns only odd numbers

### Utilities (extra challenge 🚀)
# 6.Timing decorator
# Create a decorator @timing that measures how long a function takes to run.

# 7.Caching (memoization)
# For expensive operations (e.g., factorial), store results so repeated calls are instant.

## 🌀 Flow of the Program
# Start with a loop showing the menu.
# User chooses an option → call the corresponding function.
# Display the result.
# Loop again until user selects Exit.

def normalize(text):
    final_text = text.lower().strip()
    return final_text

def word_count(text):
    words = list(text.split())
    return len(words)

def is_palindrome(word):
    reversed_text = word[::-1]
    if word == reversed_text:
        return True
    else:
        return "It is not palindrome"

def average(numbers):
    total = int()
    for i in numbers:
        total += i
    return total/len(numbers)

def filter_even_odd(numbers, choice):
    if choice == 'even':
        even = []
        for i in numbers:
            if (i%2)==0: even.append(i)
        return even
    elif choice == 'odd':
        odd = []
        for i in numbers:
            if (i%2) != 0: odd.append(i)
        return odd
    
while True:
    print("""Welcome to the Text & Numbers Toolkit!
    1. Normalize a string
    2. Count words in a sentence
    3. Check if a word is a palindrome
    4. Calculate average of numbers
    5. Filter even/odd numbers
    6. Exit
    """)
    option = int(input("Choose an option (1-7): "))
    if option == 6: break
    elif option == 1:
        text = input("Enter a string: ")
        print(normalize(text))
    elif option == 2:
        word = input("Enter a sentence: ")
        print(word_count(word))
    elif option == 3:
        word = input("Enter a word: ")
        print(is_palindrome(word))
    elif option == 4:
        numbers_input = input("Enter numbers(separated by space): ")
        numbers = [int(x) for x in numbers_input.split()]
        print(average(numbers))
    elif option == 5:
        numbers_input = input("Enter numbers(separated by space): ")
        numbers = [int(x) for x in numbers_input.split()]
        choice = input("Select even or odd: ")
        print(filter_even_odd(numbers, choice))




