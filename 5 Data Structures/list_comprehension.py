# list_comprehension.py

# Create list using loop
numbers = [1, 2, 3, 4, 5]

# Normal way
squares = []
for n in numbers:
    squares.append(n * n)

print("Squares (loop):", squares)

# List comprehension
squares2 = [n * n for n in numbers]

print("Squares (comprehension):", squares2) 