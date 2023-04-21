"""
Create a string
Index a string
String methods
"""
membership = "yearly subscription, for 2023"
plan = str(90)  # The built-in function str does an explicit conversion of an object to  a string
phone = str(9792146983)

# Index a string: Access a part of the string using indexes
print(f"{membership[0]}")
print(f"{membership[1]}")
print(f"{membership[2]}")
print(f"{membership[3]}")
print()

# We can index a string backwards
print(f"{membership[-1]}") # Gets the last item in the string
print(f"{membership[-2]}")
print(f"{membership[-3]}")
print(f"{membership[-4]}")
print()

# To break a string down in tokens
tokens1 = membership.split()
tokens2 = membership.split(',')
print(f"{tokens1}")
print(f"{tokens2}")
print()

# Get the size of a string
characters_count = len(phone)
print(f"The number of characters in the phone number is {characters_count}")
print(f"The last character in the phone number is {phone[-1]}, or {phone[characters_count-1]}")
print()

# Slicing a string
name = "Barbara Bush"
print(f"Name slicing Example 1: {name[:]}")
print(f"Name slicing Example 2: {name[0:]}")
print(f"Name slicing Example 3: {name[4:]}")
print(f"Name slicing Example 4: {name[:-1]}")
print(f"Name slicing Example 5: {name[:4]}")
print()

# Add a positive stride or a step to the slice
print(f"Name slicing Example 6: {name[::]}")
print(f"Name slicing Example 7: {name[::2]}")
print(f"Name slicing Example 8: {name[3:8:2]}")
print()

# Add a positive stride or a step to the slice
print(f"Name slicing Example 9: {name[::-1]}")
print(f"Name slicing Example 9: {name[::-3]}")
print(f"Name slicing Example 9: {name[8:0:-1]}")
print(f"Name slicing Example 9: {name[:0:-1]}")

# Phone number area code extraction
"""
phone = input("Enter a 10-digit phone number: ")
phone = phone.replace(" ", "")
phone = phone.replace("-", "")
phone = phone.replace(".", "")
print(f"The formatted phone number is: {phone}")
print(f"The area code in {phone[:3]}")

print(f"Zeros: {phone.count('0')}")
print(f"{'9' in phone}")
print(f"Where is 9? {phone.find('9')}")
"""
print()

# Password validation (part 1)
password = input("Enter a password: ")
print(f"password.isupper(): {password.isupper()}")
print(f"password.islower(): {password.islower()}")
print(f"password.isalpha(): {password.isalpha()}")
print(f"password.isalnum(): {password.isalnum()}")
print(f"password.isdigit(): {password.isdigit()}")
print(f"password.isnumeric(): {password.isnumeric()}")

print(f"Uppercase password: {password.upper()}")
print(f"Uppercase password: {password.lower()}")
print(f"Uppercase password: {password.capitalize()}")
print(f"Uppercase password: {password.title()}")

