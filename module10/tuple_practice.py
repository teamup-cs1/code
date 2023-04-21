"""
A tuple is a sequence of values. The values can be of any type, and they are indexed by integers, so in that respect, tuples are similar to lists.
Unlike lists, tuples are immutable.
It is common to enclose tuples in parentheses:
t = ('a', 'b', 'c', 'd', 'e')
"""

# Create a tuple of Video Games
games = ()
games = tuple()
games = ('Elden Ring',)
games = 'Elden Ring',
games = ('Elden Ring','LEGO Star Wars', 'Gran Turismo', 'Tunic')
print (f"{games} is {type(games)}")

(game1, game2, game3, game4) = games
for game in games:
    print(game)

for game in (game1, game2, game3, game4):
    print(game)

print()

# Swap variables
# Example: Swap two courses in your schedule
course1 = 110 # Python
course2 = 121 # C++

# This below does not work
#print(f"Before the swap: Course1:{course1}\tCourse2:{course2}")
#course1 = course2
#course2 = course1
#print(f"After the swap: Course1:{course1}\tCourse2:{course2}")

# Lets try this!
print(f"\nBefore the swap: Course1:{course1}\tCourse2:{course2}")
temp = course1
course1 = course2
course2 = temp
print(f"Before the swap: Course1:{course1}\tCourse2:{course2}")


# Lets try this!
print(f"\nBefore the swap: Course1:{course1}\tCourse2:{course2}")
course1 = course1 + course2 # 121 + 110= 231
course2 = course1 - course2 # 231 - 110 = 121
course1 = course1 - course2 # 231 - 121 = 110
print(f"Before the swap: Course1:{course1}\tCourse2:{course2}")


# Lets try this! Using a tuple
print(f"\nBefore the swap: Course1:{course1}\tCourse2:{course2}")
(course1, course2) = (course2, course1)
print(f"Before the swap: Course1:{course1}\tCourse2:{course2}")