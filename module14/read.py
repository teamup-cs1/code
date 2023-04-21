"""
<file>.read() function returns the entire contents of the file as a single string.
"""
with open("destinations.txt") as places:
    cities = places.read()
    print(cities)


"""
<file>.readline() returns the next line of the file, returning the text up to and including the next newline character.
This operation reads a file line-by-line
"""
with open("destinations.txt") as places:
    line = places.readline().strip()
    while line != "":
        print(line)
        line = places.readline().strip()


"""
<file>.readlines() reads all the lines of a file and saves them into a list.
"""
with open("destinations.txt") as places:
    lines = places.readlines()
    print(lines[::-1])
    print(lines[3:10])
    # removes the lead characters in the list
    lines = [line.strip() for line in lines]
    print(lines)