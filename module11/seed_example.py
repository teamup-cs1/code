import random
random.seed(6) # Seed is 6 and is used to generate a sequence of pseudorandom numbers
# Non determinism: 2 is a constant!

for n in range (10):
    print(random.random())
    print(random.random())
    print(random.random())