import matplotlib.pyplot as drawing
import random

# Step 1: Prepare data
# Step 2: Annotate
# Step 3: Plot

quizzes = ['quiz 1', 'quiz 2', 'quiz 3', 'quiz 4', 'quiz 5', 'quiz 6', 'quiz 7', 'quiz 8']
grades = [random.randint(50, 100) for grade in quizzes]

drawing.xlabel('Quiz number')
drawing.ylabel('Quiz grade')
drawing.title('CSCE 110 Quiz grades')

bars = drawing.barh(quizzes, grades, align='center', label="Quiz grades for CSCE 110")
drawing.legend()

for bar in bars:
    color = random.choice(['b', 'r', 'y', 'c', 'm'])
    bar.set_color(color) # Set a random color to each bar

drawing.show()
