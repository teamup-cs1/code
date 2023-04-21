"""
' r' Open file for reading. The stream is at the beginning of the file.
'r+' Open for reading and writing. The stream is at the beginning of the file.
'w' Truncate file to size zero or create a new file. The stream is at the beginning of the file.
'w+' Open for reading and writing. The file is created if it does not exist, otherwise it is truncated. The stream (Pointer) is at the beginning of the file.
'a' Open for writing. The file is created if it does not exist. The stream is at the end of the file.
'a+' Open for reading and writing.  The file is created if it does not exist.  The stream is at the end of the file.
'x' Open in exclusive mode. open for exclusive creation, failing if the file already exist.
"""
import os

os.chdir("personal")
# Example #1: Create a file handle
# travel = open("cities.txt", 'r')
# travel.close()

# Example #2: Create a file handle
"""travel = open("cities.txt", 'r+')
# Print the content of the file
print(f"Reading the content of the file ...")
#print(travel.read())
print(f"Writing a new city to the file ...")
travel.write(f"{'Santiago':<15} ${800:<15}\n")
travel.write(f"{'San Luis':<15} ${190:<15}\n")
travel.write(f"{'Durango':<15} ${260:<15}\n")
travel.close()"""

# Example #3: Create a file handle
"""travel = open("cities.txt", 'w')
# Print the content of the file
#print(f"Reading the content of the file ...")
#print(travel.read())
print(f"Writing a new city to the file ...")
travel.write(f"{'Houston':<15} ${800:<15}\n")
travel.write(f"{'Waco':<15} ${190:<15}\n")
travel.write(f"{'Dallas':<15} ${260:<15}\n")
travel.close()
"""
# Example #4: Create a file handle
"""travel = open("cities.txt", 'w+')
# Print the content of the file
print(f"Reading the content of the file ...")
print(travel.read())
print(f"Writing a new city to the file ...")
travel.write(f"{'New York':<15} ${800:<15}\n")
travel.write(f"{'Bufallo':<15} ${190:<15}\n")
travel.write(f"{'Omaha':<15} ${260:<15}\n")
travel.close()"""

# Example #5: Create a file handle
"""travel = open("cities.txt", 'a')
# Print the content of the file
#print(f"Reading the content of the file ...")
#print(travel.read())
print(f"Writing a new city to the file ...")
travel.write(f"{'Denver':<15} ${800:<15}\n")
travel.write(f"{'Cincinnati':<15} ${190:<15}\n")
travel.write(f"{'Cleveland':<15} ${260:<15}\n")
travel.close()"""

# Example #5: Create a file handle
travel = open("cities.txt", 'a+')
# Print the content of the file
print(f"Reading the content of the file ...")
travel.seek(0)  # Set the pointer at the beginning of the file
print(travel.read())
print(f"Writing a new city to the file ...")
travel.write(f"{'Miami':<15} ${800:<15}\n")
travel.write(f"{'Orlando':<15} ${190:<15}\n")
travel.write(f"{'Fort Lauderdale':<15} ${260:<15}\n")
travel.close()

# Example #6: Create a file handle
try:
    with open("southern_cities.txt", "x") as travel:
        travel.write(f"{'News Orleans':<15} ${260:<15}\n")
except Exception as e:
    print(f"Houston we got a problem!: {e}")

# Example #7: Create a file handle
try:
    with open("northern_cities.txt", "r") as travel:
        print(travel.read())
except Exception as e:
    print(f"Houston we got a problem!: {e}")

# Example #8: Create a file handle
try:
    inverse = 1 / 'math.pi'
    print(f"The inverse is {inverse}")
    with open("northern_cities.txt", "w") as travel:
        travel.write(f"{'Boston':<15} ${620:<15}\n")
except Exception as e:
    print(f"Houston we got a problem!: {e}")
finally:
    print(f"Attempted to open a file!")

print("more operations")
