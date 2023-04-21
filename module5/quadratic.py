from math import pow
from math import sqrt as real_sqrt
from cmath import sqrt as complex_sqrt

"""
Consider a second degree polynomial or Quadratic equation in the form:
ax2 + bx + c = 0
Write a program to compute the number of real roots of a quadratic equation.
"""

a, b, c = input("Enter a b c: ").split()
a = float(a)
b = float(b)
c = float(c)
print(f"The coefficients are: {a} {b} {c}")

discriminant = pow(b, 2) - 4 * a * c
print(f"The discriminant is {discriminant}")

"""
# If the discriminant is positive then the equation has two real roots
if discriminant > 0:
    x1 = (-b - real_sqrt(discriminant)) / (2 * a)
    x2 = (-b + real_sqrt(discriminant)) / (2 * a)
    print(f"Two real roots: {x1}, {x2}")
else:
    # If the discriminant is zero then the equation has one real root
    if discriminant == 0:
        x = -b / (2 * a)
        print(f"One real root: {x}")
    else:
        # If the discriminant is negative then the equation has two complex roots
        x1 = (-b - complex_sqrt(discriminant)) / (2 * a)
        x2 = (-b + complex_sqrt(discriminant)) / (2 * a)
        print(f"Two complex roots: {x1}, {x2}")
"""

# If the discriminant is positive then the equation has two real roots
if discriminant > 0:
    x1 = (-b - real_sqrt(discriminant)) / (2 * a)
    x2 = (-b + real_sqrt(discriminant)) / (2 * a)
    print(f"Two real roots: {x1}, {x2}")
elif discriminant == 0:  # If the discriminant is zero then the equation has one real root
    x = -b / (2 * a)
    print(f"One real root: {x}")
else:  # If the discriminant is negative then the equation has two complex roots
    x1 = (-b - complex_sqrt(discriminant)) / (2 * a)
    x2 = (-b + complex_sqrt(discriminant)) / (2 * a)
    print(f"Two complex roots: {x1}, {x2}")
