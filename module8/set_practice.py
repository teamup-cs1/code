"""
A set is a collection of distinct and unordered objects.
Sets are mutable. (We can add or remove items from them)
Elements of sets are immutable.
Elements of sets are unique.
Sets cannot be indexed.
Sets support a standard collection of operations:
union
intersection
difference
symmetric difference
"""

# Create a set
majors = set()  # Set constructor
minors = {'MATH', 'ENG', 'BIO'}

print(f"Majors: {majors} contains {len(majors)} items")
print(f"Minors: {minors} contains {len(minors)} items")
# print(f"The second item in {minors} is {minors[1]}")
print(f"Is ENG offered as an minor? {'ENG' in minors}")
print(f"Is ENG not offered as an minor? {'ENG' not in minors}")
print(f"Is CS offered as an minor? {'CS' in minors}")

# '.append()' and '.extend()' equivalents for sets '.add()' and '.update()'

majors.add('CS')
print(f"Majors: {majors} contains {len(majors)} items")

majors.update(['CS', 'EE', 'LAW', 'APMS', 'ISEN', 'GIST'])
print(f"Majors: {majors} contains {len(majors)} items")

# .remove() and .discard()
# .remove()
try:
    majors.remove('LAW')
    print(f"Majors: {majors} contains {len(majors)} items")
except:
    print(f"We have a problem!")

try:
    majors.remove('STAT')
    print(f"Majors: {majors} contains {len(majors)} items")
except:
    print(f"We have a problem!")

# .discard()
majors.discard('APMS')
print(f"Majors: {majors} contains {len(majors)} items")

majors.discard('BIO')
print(f"Majors: {majors} contains {len(majors)} items")


