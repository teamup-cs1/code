"""
Get the number of grades
Get the highest grades
Get the lowest grade
Get the sum of all grades
"""

grades = input('enter numbers: ').split()
print(f"Grades: {grades}")
numbers = [float(grade) for grade in grades]  # List comprehension
print(f"Grades: {numbers}")

# Use the built-in pyhton functions for computation
number_of_grades = len(numbers)
highest_grade = max(numbers)
lowest_grade = min(numbers)
sum_of_grades = sum(numbers)

print(f"The number of grades: {number_of_grades}")
print(f"The highest grade: {highest_grade}")
print(f"The lowest grade: {lowest_grade}")
print(f"The sum of grades: {sum_of_grades}")