"""
Distance calculation
The formula to calculate the distance between two points of coordinates (x1, y1) and (x2, y2) is given below.
distance = (x1-x2)2 + (y1-y2)2
Write a Python program stored in a file distance.py that asks for two points’ coordinates and calculates the distance between the two points.
Assume that the points’ coordinates are always positive. Round the distance to two digits after the decimal point.
"""

import random


def gear_shift(number_of_shifts):
    """This function prints a random gear"""
    gears = ['first', 'second', 'third', 'fourth', 'fifth', 'reverse']
    gear = random.choice(gears)
    shifts = random.sample(gears, number_of_shifts)
    return shifts


def calculate_distance(x1, y1, x2, y2):
    """This function calculates the distance between two points of coordinates (x1, y1) and (x2, y2)."""
    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    distance = round((x + y) ** (1 / 2), 2)
    return distance


def main():
    print(f"We are running in: {__name__}")
    """This is the driver function or the entry point the program"""
    coordinate_x1 = float(input('x coordinate of the first point: '))
    coordinate_y1 = float(input('y coordinate of the first point: '))
    coordinate_x2 = float(input('\nx coordinate of the second point: '))
    coordinate_y2 = float(input('y coordinate of the second point: '))

    distance = calculate_distance(coordinate_x1, coordinate_y1, coordinate_x2,
                                  coordinate_y2)  # Calling the function calculate_dictance with the coordinates as arguments
    print(
        f"The distance between the points {coordinate_x1, coordinate_y1} and {coordinate_x2, coordinate_y2} is {distance}")


# Execute the function main()
if __name__ == "__main__":  # If running the program standalone (By itself)
    main()
