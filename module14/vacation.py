"""
The open() function creates a file object (a way of getting at the contents of the file).
The file object is also called a handle, it is used to read or write to the file.
filename is the path the file.
The mode is the file system permission.
"""
import os

# Step 1: create a dictionary of destinations
destinations = {'San Miguel': 800, 'Puerto Vellarta': 560, 'Tijuana': 300, 'Merida': 290}

# Step 2: create a separate directory to save our personal files
print(f"Creating a directory within: {os.getcwd()}")
print(f"First, lest check what is here!\n {os.listdir()}")

try:
    os.mkdir("personal")
except FileExistsError:
    print(f"The directory already existing")

os.chdir("personal")
print(f"What is the current path: {os.getcwd()}")

# Step 3: create a new file in the directory personal
try:
    travels = open('cities.txt', 'x')
except FileExistsError:
    print(f"Hold on! This file already exists")
    exit()

line = f"{'CITY NAME':<15}{'TICKET PRICE':<15}\n"
travels.write(line)
for city, price in destinations.items():
    line = f"{city:<15} ${price:<15}\n"
    travels.write(line)
print(f"All the destinations are saved!")
travels.close()