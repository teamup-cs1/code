"""
Write a program that simulates the number of heads and tails that appear using a fair coin.
"""
import random


def flip_coin(coin_type):
    """
    This function returns a random side of a coin
    @return:
    """
    if coin_type == 'fair':
        sides = ['head', 'tails']  # Model of fair coin (50% heads, 50% tails)
    else:
        sides = ['head', 'head', 'tails', 'head']  # Model of coin (75% heads, 25% tails)
    side = random.choice(sides)  # Random event
    return side


def main():
    """
    This function is the driver and prompts the user for the number of flips and returns the count of heads and tails
    @return: None
    """
    flips = int(input("Enter the number fo coin flips: "))
    heads_count = 0
    tails_count = 0

    for flip in range(1, flips + 1):
        side = flip_coin('unfair')
        print(f"On flip number {flip} the side {side} turned up")
        if side == 'head':
            heads_count += 1
        elif side == "tails":
            tails_count += 1

    # Print the results
    print(f"Stats: \t Heads up count: {heads_count}\t Tails up count: {tails_count}")
    print(f"Probability of heads up: {round(heads_count/ flips * 100,2)}%")
    print(f"Probability of tails up: {round(tails_count / flips * 100, 2)}%")


main()
