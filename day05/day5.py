# 📅 Day 5: Loops in Python
# Lesson:
# - for loop: iterate over a sequence or range
# - while loop: repeat until a condition is false
# - break: exit the loop early
# - continue: skip current iteration
#
# Exercise:
# 1. Use a for loop to print numbers 1 to 10
# 2. Print each character of your name using a loop
# 3. Use a while loop to print numbers from 10 down to 1
# 4. Ask the user for numbers repeatedly until they enter 0
#    - Print the sum of all numbers entered
# 5. Bonus: Print only even numbers between 1 and 20
#
# 👉 Write your solution below:

#1
for num in range(1, 11):
    print(num)

#2
name = "Biniyam"
for letter in name:
    print(letter)

#3
count = 10
while count >= 1:
    print("Count:", count)
    count -= 1

#4 
total_num = 0
while True:
    user_num = int(input("Enter a number (0 to stop): "))
    if user_num == 0:
        break
    total_num += user_num

print("Total sum:", total_num)


#5
for i in range(2, 21, 2):
    print(i)

