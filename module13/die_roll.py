"""
Write a program that calculates on average, the number of times to roll a die before all six numbers turn up.
"""
import random as die


def die_roll():
    """
    This function simulates a die roll
    @return:
    """
    side = die.randint(1, 6)
    return side


def roll_all_numbers():
    """
    This function simulates multiple die rolls until all sides turn up
    @return: 
    """
    rolls = 0
    dice = [0] * 7
    while sum(dice) != 6:  # Until the die is [0,1,1,1,1,1,1]
        side = die_roll()
        dice[side] = 1  # Write a 1 at index of side
        rolls += 1
    return rolls


def roll_all_numbers_set():
    """
    This function simulates multiple die rolls until all sides turn up using a set
    @return:
    """
    rolls = 0
    dice = set()
    while len(dice) != 6: # Only when the dice set is {1,2,3,4,5,6} then the length of the set will be 6
        side = die_roll()
        dice.add(side)
        rolls += 1
    return rolls


def calculate_average(experiments):
    """
    This function calculates the average number of rolls in multiple experiments
    @param experiments:
    @return:
    """
    sum_of_rolls = 0
    for experiment in range(experiments):
        #sum_of_rolls += roll_all_numbers()  # Sum up the numbers of rolls per experiment
        sum_of_rolls += roll_all_numbers_set()  # Sum up the numbers of rolls per experiment
    average = sum_of_rolls / experiments
    return average


def main():
    """This function takes a number of experiments from the user and return an average of the number of rolls for
    all sides of a die to turn up"""
    experiments = input("Number of experiments: ").split()
    experiments = [int(n) for n in experiments]
    for experiments in experiments:
        average = calculate_average(experiments)
        print(f"Number of experiments: {experiments} -> Average number of rolls: {average}")


main()
