import calculator


def favorite():
    """This function is a demo example to use definition from the calculator module"""
    print(f"This program calculates the distance between two offices: ")
    (office1_x, office1_y) = (6, 18)
    (office2_x, office2_y) = (84.25, 129.26)

    office_distance = calculator.calculate_distance(office1_x, office1_y, office2_x, office2_y)

    print(f"The distance between {(office1_x, office1_y)} and {(office2_x, office2_y)} is {office_distance}")

    # calculator.gear_shift()
    gears_sequence = calculator.gear_shift(3)
    print(f"Navigation starts on gear {gears_sequence[0]}")
    print(f"The full sequence of gears is {gears_sequence}")


favorite()