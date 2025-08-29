# ------------------ Day 12: File Handling ------------------
# In Python, working with files involves 3 main steps:
# 1. Open the file (in a specific mode: read 'r', write 'w', append 'a')
# 2. Do something with it (read, write, etc.)
# 3. Close the file (or use "with open(...)" so it closes automatically)

# Example 1: Writing to a file (this creates the file if it doesn't exist)
with open("./day12/example.txt", "w") as file:
    file.write("Hello, Python learners!\n")
    file.write("This is Day 12: File Handling.\n")

# Example 2: Reading from a file
with open("./day12/example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Example 3: Appending data to the file (does not erase existing content)
with open("./day12/example.txt", "a") as file:
    file.write("We just added a new line!\n")

# Example 4: Reading line by line
with open("./day12/example.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())   # strip() removes newlines/spaces

# ------------------------------------------------------------
# Key Notes:
# - "w" = write (erases old content if file exists)
# - "a" = append (adds new content without deleting old)
# - "r" = read (only reads, error if file not found)
# - Always close files -> use "with open()" to do it automatically



# ---------------- Day 12: File Handling — Practice Exercises ----------------

# Exercise 1: Writing to a File
# - Ask the user to enter their favorite color.
# - Save it to a file called "favorite.txt".
# - Run the program multiple times and overwrite the file each time.

def exercise1():
    color = input("Enter your favorite color: ")
    with open("./day12/favorite.txt", "w") as file:
        file.write(color)
        
exercise1()

# Exercise 2: Reading from a File
# - Open the file "favorite.txt".
# - Print its content to the console.

def exercise2():
    favorite_color = open("./day12/favorite.txt", "r")
    print(favorite_color.read())
    favorite_color.close()

exercise2()

# Exercise 3: Appending Data
# - Create a file called "notes.txt".
# - Ask the user to enter a short note.
# - Append (not overwrite) the note into the file.
# - Each time you run the program, the note should be added as a new line.

def exercise3():
    notes = open("./day12/notes.txt", "a")
    user_note = input("Enter a short note: ")
    notes.write(f'{user_note}\n')
    notes.close()

exercise3()

# Exercise 4: Writing Multiple Lines
# - Write a program that asks the user for 3 names.
# - Save those names into a file called "names.txt", one per line.

def exercise4():
    name1, name2, name3 = input("Enter 3 names(separated by space): ").split()
    with open("./day12/names.txt", "w") as file:
        file.write(f"{name1}\n{name2}\n{name3}")

exercise4()

# Exercise 5: Reading Line by Line
# - Open "names.txt".
# - Read all the lines and print them one by one with a greeting.
#   Example:
#   Hello, Alice
#   Hello, Bob
#   Hello, Charlie

def exercise5():
    with open("./day12/names.txt", "r") as file:
        for line in file:
            print(f"Hello, {line.strip()}")

exercise5()

# Exercise 6: Counting Words in a File
# - Ask the user to enter a sentence.
# - Save it into "sentence.txt".
# - Reopen the file, read the sentence, and count how many words it has.
#   (Hint: use .split() to break the text into words.)

def exercise6():
    sentence = input("Write a sentence: ")
    sentence_file = open("./day12/sentence.txt", "w")
    sentence_file.write(sentence)
    sentence_file.close()
    with open("./day12/sentence.txt", "r") as file:
        word_count = file.read()
        print(len(word_count.split()))

exercise6()

# Exercise 7 (Challenge 🚀): File-Based To-Do List
# - Create a file "todo.txt".
# - Write a menu with options:
#   1. Add a new task
#   2. View all tasks
#   3. Exit
# - Tasks should be stored in "todo.txt" so they remain even after restarting the program.


def exercise7():
    while True:
        try:
            print(f"1. Add a new task \n2. View all tasks \n3. Exit")
            user_input = int(input("Enter a number(1-3): "))
            print()
            if user_input == 1:
                task = input("Enter task: ")
                with open("./day12/todo.txt", "a") as file:
                    file.write(f'{task}\n')
            elif user_input == 2:
                with open("./day12/todo.txt", "r") as file:
                    print(file.read())
            elif user_input == 3:
                break
            else:
                print("Please enter a number between 1-3")
        except ValueError as e:
            print(e)

exercise7()