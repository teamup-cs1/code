import random
import string

majors = {'CS', 'EE', 'LAW', 'APMS', 'ISEN', 'GIST', 'BIOL', 'PHYS'}
minors = {'MATH', 'STATS', 'LAW', 'USAR', 'PM', 'ME', 'EE'}

print("\nUnion")
all_disciplines = majors.union(minors)
print(f"All the majors and the minors offered at TAMU: {all_disciplines}")

all_disciplines = majors | minors
print(f"All the majors and the minors offered at TAMU: {all_disciplines}")

print("\nIntersection")
common_disciplines = majors.intersection(minors)
print(f"The common majors and minors disciplines offered at TAMU: {common_disciplines}")

common_disciplines = majors & minors
print(f"The common majors and minors disciplines offered at TAMU: {common_disciplines}")

print("\nDifference")
majors_only = majors.difference(minors)
print(f"The disciplines only offered at TAMU as majors are: {majors_only}")

majors_only = majors - minors
print(f"The disciplines only offered at TAMU as majors are: {majors_only}")

majors_only = majors - majors.intersection(minors)
print(f"The disciplines only offered at TAMU as majors are: {majors_only}")

print("\nSymmetric Difference")
majors_minors_only = majors.symmetric_difference(minors)
print(f"Disciplines that cannot be both a major and a minor: {majors_minors_only}")

majors_minors_only = majors ^ minors
print(f"Disciplines that cannot be both a major and a minor: {majors_minors_only}")

majors_minors_only = majors.union(minors) - majors.intersection(minors)
print(f"Disciplines that cannot be both a major and a minor: {majors_minors_only}")
print(f"Are these sets equal?: {majors.union(minors) - majors.intersection(minors) == majors.symmetric_difference(minors)}")

print("\nComplement")
# Create a new set
all_majors = set()
# Generate 100 random majors names
for m in range(100):
    major = [random.choice(string.ascii_uppercase) for n in range(3)]
    major_string = ""
    major_string = major_string.join(major)
    all_majors.add(major_string)
all_majors.update(majors)
print(f"All the {len(all_majors)} majors: {all_majors}")

non_TAMU_majors = all_majors - majors
print(f"\nThe number of TAMU majors is: {len(majors)}")
print(f"\nThe complement of the TAMU majors contains {len(all_majors - majors)} elements: {non_TAMU_majors}")

# Set membership
print(f"\nIs EE part of the majors offered? {'EE' in majors}")

electrical = {'EE'}
print(f"Is EE part of the majors offered? {electrical.issubset(majors)}")

engineering = {'CS', 'EE'}
print(f"Is engineering part of the majors offered? {engineering.issubset(majors)}")
print(f"Do the majors included engineering? {majors.issuperset(engineering)}")

print(f"Are there any common minors and majors? {not majors.isdisjoint(minors)}")
print(f"Are there any common minors and majors? {any(majors.intersection(minors))} {majors.intersection(minors)}")


