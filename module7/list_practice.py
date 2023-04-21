import random
import string

"""
Lists are sequences used to store collections of data.
Lists are ordered and their elements can be indexed by numbers.
Lists are mutable objects. You can change individual elements in a list.
You can create sub-lists using the slice operators.
Lists are heterogeneous
"""
"""
# Creating a list
# airports = list()
airports = ['CLL', 'DFW', 'JFK']

# iterate over the content of a list
for airport in airports:
    print(f"The airport is: {airport}")

# Append new objects to a list
new_airports = ['MIA', 'EVV', 'HOU', 'AUS']
for new_airport in new_airports:
    airports.append(new_airport)
print(f"Updated list of airports: {airports}")

# Extending a list
new_airports = ['LAX', 'CHI', 'OMA', 'HOB', 'CDG', 'COO']
airports.extend(new_airports)
print(f"Updated list of airports: {airports}")

# Populate a list dynamically using List Comprehension
# example 1: create a list of even numbers between 0 and 1000
# even_numbers = [expression for iterator in sequence if condition]
even_numbers = [2*k for k in range(0, int(1000/2) + 1)]
print(f"Even numbers between 0 and 1000:\n {even_numbers}")

even_numbers = [k for k in range(0, 1000 + 1) if k % 2 == 0]
print(f"Even numbers between 0 and 1000:\n {even_numbers}")


# example 2: create a list of odd numbers between 0 and 1000
# odd_numbers = [expression for iterator in sequence if condition]
odd_numbers = [2*k+1 for k in range(0, int(1000/2))]
print(f"Odd numbers between 0 and 1000:\n {odd_numbers}")

odd_numbers = [k for k in range(0, 1000 + 1) if k % 2 == 1]
print(f"Odd numbers between 0 and 1000:\n {odd_numbers}")

# Concatenation of lists
even = [2*n for n in range(10)]
odd = [2*n+1 for n in range(10)]
even_and_odd = even + odd
print(even_and_odd)

# Multiplication of lists
print(even * 3)


# Secure Password Generator
# Generate a password that contains letters and digits using a list comprehension
password = [random.choice(string.ascii_letters+string.digits+string.punctuation) for number in range(18)]
password_string = ""
password_string = password_string.join(password)
print(f"\nGenerated password: {password_string}")
"""

# Lists methods

# Examples generate a list of random airport codes
# .append()
airport_codes = int(input("How many airport codes would you like to generate? "))
list_of_airports = list()

for code in range(airport_codes):
    airport_name = [random.choice(string.ascii_letters.upper()) for number in range(3)]
    list_of_airports.append("".join(airport_name))
    print(f"Airport name: {airport_name}")
    print(f"Airport names: {list_of_airports}")

# .extend() vs .append()

# .extend()
texas_airports = ['CLLT', 'AUSTIN', 'HOUS', 'DFWO', 'SANTONIO']
list_of_airports.extend(texas_airports)
print(f"\nUpdated Airport names 1: {list_of_airports}")

# .append()
california_airports = ['LAX', 'LGB', 'FAT', 'MMH']
list_of_airports.append(california_airports)
print(f"\nUpdated Airport names 2: {list_of_airports}")

# .count()
# count the number of specific items in a list
print(f"\nCounts of airport: {list_of_airports.count('CLL')}")

# .remove()
# remove a specific item for a list
list_of_airports.remove('CLLT')
print(f"\nUpdated Airport names 3: {list_of_airports}")


# Sorting of a list
# Example sort the list of airports in ascending or descending order
# take second element for sort

# Lets remove the list of California airports
list_of_airports.remove(['LAX', 'LGB', 'FAT', 'MMH'])

# Sort the list of airports
list_of_airports.sort()
print(f"\nUpdated Airport names 4: {list_of_airports}")

list_of_airports.sort(reverse=True)
print(f"\nUpdated Airport names 5: {list_of_airports}")

list_of_airports.sort(reverse=False)
print(f"\nUpdated Airport names 6: {list_of_airports}")

list_of_airports.sort(key=len, reverse=False)
print(f"\nUpdated Airport names 7: {list_of_airports}")

# .clear()
# Clear the content of a list
list_of_airports.clear()
print(f"\nUpdated Airport names after clear: {list_of_airports}")
