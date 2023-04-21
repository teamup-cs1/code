import random

"""
For loop practice
"""

# Ask for a users name and print the letter of the name in a table.
"""first_name = input("Enter your first name: ")
print(f"{'Letter'.upper():^10}")
for letter in first_name:
    print(f"{letter.upper():^10}")"""

# Generate random 100 numbers between 0 and 1000
"""for number in range(100):
    random_number = random.randint(0, 1000)
    print(f"Random number: {random_number}", end="\t@cindy@\t")"""

# Capitalize the first letter in a name:
"""print(f"{'Updated names'.upper():^20}")
for name in ['blake', 'julia', 'david', 'michael', 'Iris']:
    updated_name = name[:3].upper() + name[3:]
    print(f"{updated_name:^20}")
    print(f"{updated_name * 6:^20}")"""

# Generate even number between 12 and 110
# Solution 1
"""for number in range(12, 110+1):
    if number % 2 == 0:
        print(f"Even number : {number}")"""

# Solution 2
"""for number in range(12, 110+1, 1):
    print(f"Even number : {number}")"""

# Control statements: break
# Generate even number between 12 and 110 if we reach the number 86 then stop.
"""for number in range(12, 111, 2):
    print(f"Even number: {number}")
    if number == 86:
        print("End of the loop")
        break"""

# Control statements: continue
# Generate even number between 12 and 110 if we reach the number 86 then print a congratulations message.
"""for number in range(12, 111, 2):
    if number == 86:
        print("Congratulations your reached level 86!")
        continue
    print(f"Even number: {number}")"""


# Control statements: pass
# Generate even number between 12 and 110 if we reach the number 86 do nothing.
"""for number in range(12, 111, 2):
    if number == 86:
        pass # No op
    print(f"Even number: {number}")"""


# Else after a for loop
"""for age in range(19, 23):
    print(f"Age: {age}")
    if age == 21:
        print(f"Your are {age}! Congratulations buy yourself a beer!")
        break
else: # We execute the body of the else statement if the the for loop reached the end of the sequence succesfully
    print(f"Reached the age to graduate!")"""


# Nesting consists of placing a loop inside another loop

"""
Write a program that prints a menu of computer configurations to a customer.
"""
computers = ['macbook pro', 'macbook air', 'ipad', 'surface']
operating_systems = ['windows', 'linux', 'macOS']
prices = [500.96, 845, 1250, 925]

options = len(computers) * len(operating_systems) * len(prices)
print(f"Howdy! Here are all your {options} options")
print(f"{'Computer'.upper():^15}{'Operating system'.upper():^20}{'Price'.upper():^10}")
for computer in computers:
    for os_type in operating_systems:
        for price in prices:
            print(f"{computer:^15}{os_type:^20}{price:^10}")



