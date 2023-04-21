import math
# import math as algebra
# from math import pi

"""
Problem #1
The diagonal of a polygon is a line segment linking two non-adjacent vertices.
Write a program that asks for the number of sides of a polygon. 
Compute  the number of diagonals.
diagonals = sides * (sides - 3) / 2
Print the result in a full sentence.
"""
"""
sides = int(input("What is the number of sides? "))  # This is an explicit type conversion
diagonals = sides * (sides-3) / 2 # This is an implicit type conversion
print(f"The number of diagonals in a polygon of sides {sides} is {diagonals}")
"""

"""
Problem # 2
Write a program that calculates the volume of a cylinder
V = π * radius * radius * height
"""
"""
radius = float(input("What is the radius of the base of the cylinder? ")) # This is an explicit type conversion
height = float(input("What is the heigth of the base of the cylinder?")) # This is an explicit type conversion
# volume = math.pi * radius * radius * height
# volume = math.pi  * radius**2 * height
volume = math.pi * math.pow(radius, 2) * height
print(f"The volume of a cylinder of radius {radius} and height {height} is {round(volume, 2)}")
"""

"""
Problem # 3
Write a program that tells if a number is odd or even
even: 2k
odd: 2k+1
k is an integer
"""
"""
number = int(input("Enter an integer: "))
remainder = number % 2 # The % is the modulus operator
print(f"{number} modulus 2 is {remainder}")
"""

"""
Formatting outputs and alignment
"""
print(f"{'Courses':^10}{'Credit hours':^20}")
print(f"{'CSCE110':^10}{'4':^20}")
print(f"{'CSCE121':^10}{'3':^20}")
print(f"{'CSCE222':^10}{'2':^20}")