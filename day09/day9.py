# 📅 Day 9: Lists in Python
# Lesson:
# - Creating lists
# - Accessing elements (indexing, slicing)
# - Adding items (append, insert, extend)
# - Removing items (remove, pop, del)
# - List operations (len, in, not in, concatenation, repetition)
# - Iterating through lists (for loop, while loop)
# - Useful list functions: min, max, sum, sorted, reverse
# - Nested lists (list inside list)

# Exercise:
# 1. Create a list of 5 fruits. Print the first, middle and last fruit.
# 2. Create a list of numbers 1-10. Print only even numbers using slicing or comprehension.
# 3. Create a list of numbers [10, 20, 30, 40, 50].
#     - Replace the 3rd number with 99.
#     - Remove the last item.
#     - Insert 15 at the second position.
# 4. Create a nested list (2x2 matrix) and print each element separately.
# 5. Use list comprehension to:
#     - Generate squares of numbers from 1 to 10.
#     - Generate all odd numbers from 1 to 20.
# 
# 👉 Write your solution below:

# 1.
foods = ["Pizza", "Sushi", "Burger", "Pasta", "Ice Cream"]

print("First food:", foods[0])
print("Middle food:", foods[len(foods)//2])
print("Last food:", foods[-1])


# 2.
numbers = list(range(1, 11))

even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)


# 3.
nums = [10, 20, 30, 40, 50]

nums[2] = 99

nums.pop()

nums.insert(1, 15)

print("Modified list:", nums)


# 4.
matrix = [[1, 2], [3, 4]]

for row in matrix:
    for element in row:
        print("Matrix element:", element)


# 5.
squares = [n**2 for n in range(1, 11)]
print("Squares 1–10:", squares)

odds = [n for n in range(1, 21) if n % 2 != 0]
print("Odd numbers 1-20:", odds)
