"""
Write a program that prompts a user for information.
And prints a driver licence for a user.
"""

first_name = input("What is your first name?")
last_name = input("What is your last name?")
month = input("What is your month of birth?")
day = input("What is your day of birth?")
year = input("What is your year of birth?")
address = input("What is your Texas address?")


print(f"{'Driver license'.upper():^60}")
date_of_birth = month + '/' + day + '/' + year
expiration_date = "12/31/2022"
print(f"{'DOB:':<5}{date_of_birth:<25}{expiration_date:<30}")
print(f"{'First:':<5}{first_name.capitalize():<25}")
print(f"{'Last:':<5}{last_name.capitalize():<25}")
print(f"\n{'Address:':<5}{address:<25}")
