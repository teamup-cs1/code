""""
Write a program in Python that simulates the number of heads and tails that appear using a fair coin with:
10 flips
100 flips
1,000 flips
10,000 flips
100,000 flips
1,000,000 flips
Calculate the average and plot the results in a line chart, defining one curve of each output.

Plot the result
"""

# Step 1: Prepare data
# Step 2: Customize and annotate! (xlabel, ylabel,legend,title)
# Step 3: Plot !
import os
import random
import matplotlib.pyplot as graph


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


def simulation_flips(flips):
    """
    This function performs the simulation of multiple coin flips and computes the probabilities of heads up and tails up.
    @param flips:
    @return:
    """
    heads_count = 0
    tails_count = 0

    for flip in range(1, flips + 1):
        side = flip_coin('unfair')
        print(f"On flip number {flip} the side {side} turned up")
        if side == 'head':
            heads_count += 1
        elif side == "tails":
            tails_count += 1
    probability_heads_up = round(heads_count / flips * 100)
    probability_tails_up = round(tails_count / flips * 100)

    return probability_heads_up, probability_tails_up


def plot_simulation(experiments, probabilities_heads_up, probabilities_tails_up):
    """
    This function plots line chart of probabilities of heads up versus probabilities of tails up for multiple experiments of coin flips

    @param experiments:
    @param probabilities_heads_up:
    @param probabilities_tails_up:
    @return:
    """
    graph.plot(experiments, probabilities_heads_up, marker='o', label="Probabilities of heads up")
    graph.plot(experiments, probabilities_tails_up, marker='x', label="Probabilities of tails up")
    graph.grid('r')
    graph.xlabel("Number of experiments")
    graph.ylabel("Probabilities")
    graph.legend()
    graph.title("Fair coin simulation")
    graph.xscale('log')

    path = 'coin_simulation'
    if not os.path.isdir(path): # Check if the directory `coin_simulation` already exists
        os.mkdir(path)  # Make a directory
    os.chdir(path)  # Change directory

    graph.savefig("fair-coin-simulation.jpg")
    graph.show()



def main():
    """
    This function is the driver and prompts the user for the number of flips and returns the count of heads and tails
    @return: None
    """
    experiments = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
    probabilities_heads_up = []
    probabilities_tails_up = []

    for flips in experiments:
        probability_heads_up, probability_tails_up = simulation_flips(flips)
        probabilities_heads_up.append(probability_heads_up)
        probabilities_tails_up.append(probability_tails_up)

    print(f"The probabilities of heads up: {probabilities_heads_up}")
    print(f"The probabilities of tails up: {probabilities_tails_up}")

    plot_simulation(experiments, probabilities_heads_up, probabilities_tails_up)


main()
