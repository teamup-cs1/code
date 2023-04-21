# 1 -Default way to import
# import random

# 2 - rename a module
# import random as canvas

# 3 - import all definitions from a module
# from random import *

# 4- import specific definitions from a module
from random import sample, choice, shuffle
"""
Some programs require randomness.
Python comes with a module, called random, that allows us to use random numbers in our programs.
The sequence of numbers generated depends on a seed.
Because the random number generation is not truly random, the seed is the number that generates the random numbers.
"""
"""
Example 1: Guessing game
The goal of the Guessing Game is to guess a secret number between 1 and 100.
The program generates a secret number between 1 and 100.
If the users guess is wrong, the program prompts if the guess is too low or too high and keeps asking for a new number.
The program should count and show the number of guesses.
Draw the flowchart and write the code for this program.
"""

"""
secret = randint(1, 100)
guess = int(input("Enter a number between 1 and 100: "))
trials = 1

while guess != secret:
    if guess < secret:
        print(f"{guess} is too low!")
    else:
        print(f"{guess} is too high!")
    guess = int(input("Enter a number between 1 and 100: "))
    trials += 1
print(f"You guessed the secret number in {secret} in {trials}")
"""

"""
Example 2: Randomly generate teams of size n from a list of students
"""
students = ["Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David",
            "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah", "William",
            "Jonathan", "Stephanie", "Brian", "Nicole", "Nicholas", "Anthony", "Heather", "Eric", "Elizabeth", "Adam",
            "Megan", "Melissa", "Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle", "Rachel", "Laura",
            "Lauren", "Amber", "Brittany", "Danielle", "Richard", "Kimberly", "Jeffrey", "Amy", "Crystal", "Michelle",
            "Tiffany", "Jeremy", "Benjamin", "Mark", "Emily", "Aaron", "Charles", "Rebecca", "Jacob", "Stephen",
            "Patrick", "Sean", "Erin", "Zachary", "Jamie", "Kelly", "Samantha", "Nathan", "Sara", "Dustin", "Paul",
            "Angela", "Tyler", "Scott", "Katherine", "Andrea", "Gregory", "Erica", "Mary", "Travis", "Lisa"]

team_size = int(input("Enter the team size: "))
teams_count = int(input("Enter the number of teams: "))
print(f"Building teams of {team_size} out of {len(students)}")

for team in range(1, teams_count+1):
    group = sample(students, team_size)
    team_leader = choice(group)
    print(f"Team #{team}: {group}\t The team leader is {team_leader}")
    shuffle(group)
    print(f"Team #{team} shuffled version {group}\n")
