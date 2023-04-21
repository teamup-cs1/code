import matplotlib.pyplot as drawing
import os

# Step 1: Prepare data
# Step 2: Customize and annotate! (xlabel, ylabel,legend,title)
# Step 3: Plot !

try:
    os.mkdir('classroom_charts')
    os.chdir('classroom_charts')
except Exception as e:
    print(e)

# Plot #1: Drawing a line
x_values = list(range(20))
y_values = list(range(6,26))
print(x_values)
print(y_values)
drawing.plot(x_values, y_values, marker='$f$', color='g', linestyle="--", label="Linear equation") # Draw a line

# Plot #2: Drawing a cubic equation y = 2x^3 + 6x^2 + 5x + 9
x_values = list(range(-60,60))
y_values = [6*(x**2) + 5*x + 9 for x in x_values]
drawing.plot(x_values, y_values, marker="^", color='r', linestyle="-.", label="Cubic equation") # Draw a line

drawing.xlabel("x values")
drawing.ylabel("y values")
drawing.yscale('linear')
drawing.grid()
drawing.legend()
drawing.title("Multiple equation charts")

drawing.savefig("my_favorite_line.jpg")
drawing.savefig("my_favorite_line.png")
drawing.savefig("my_favorite_line.pdf")
drawing.show()