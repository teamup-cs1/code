"""
Write a program that computes the letter grade of a student given her score grade.
"""
"""
# Version 1
score = int(input("Enter your score: "))

if score >= 90:
    letter = 'A'
if 80 <= score < 90:
    letter = 'B'
if 70 <= score < 80:
    letter = 'C'
if 60 <= score < 70:
    letter = 'D'
if score < 60:
    letter = 'F'

print(f"Letter grade for a score of {score}: {letter}")
"""

# Version 2
score = int(input("Enter your score: "))

if score >= 90:
    letter = 'A'
elif 80 <= score < 90:
    letter = 'B'
elif 70 <= score < 80:
    letter = 'C'
elif 60 <= score < 70:
    letter = 'D'
elif score < 60:
    letter = 'F'

print(f"Letter grade for a score of {score}: {letter}")