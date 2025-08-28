# Day 11 - Importing Modules (math, random, custom modules)

# --- Built-in math module ---
import math

print("Square root of 81:", math.sqrt(81))
print("45 degrees in radians:", math.radians(45))
print("GCD of 48 and 180:", math.gcd(48, 180))

print("\n--- Random module ---")
import random

print("Random integer between 1 and 6 (like dice):", random.randint(1, 6))
print("Random choice from list:", random.choice(["Alice", "Bob", "Charlie"]))
print("Random float between 0 and 1:", random.random())

print("\n--- Aliases and specific imports ---")
import math as m
from random import randint, choice

print("2^3 using math.pow:", m.pow(2, 3))
print("Dice roll using randint:", randint(1, 6))
print("Random yes/no/maybe:", choice(["yes", "no", "maybe"]))

print("\n--- Custom Module Example ---")
import my_math   

print("10 + 5 =", my_math.add(10, 5))
print("10 - 5 =", my_math.subtract(10, 5))
