import random
grades = [random.randint(50, 100) for grades in range(8)]
print(f"Grades: {grades}")
grades.sort(reverse=True)
print(f"Grades: {grades}")
grades.sort(reverse=False)
print(f"Grades: {grades}")

grades = [random.randint(50, 100) for grades in range(8)]
print(f"Grades: {grades}")
ordered_grades = sorted(grades, reverse=True)
print(f"Grades: {grades}")
print(f"Ordered grades: {ordered_grades}")
print(f"{grades == ordered_grades}")