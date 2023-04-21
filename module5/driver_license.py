"""
Part 1
Write a program that asks a user for their age and determines if the user can drive in the state of Texas.

Part 2
Add some conditions to issue the driver license.
- Age must be at least 16
- Applicant must have Texas residency (water bill or electric bill)
- Valid Social Security number

"""
# Part 1
"""
age = int(input("Enter your age: "))
if 16 <= age <= 90:
    print("You can drive!")
else:
    print("Sorry you cannot drive :(")
"""

# Part 2
# Age must be at least 16
age = int(input("Enter your age: "))
valid_age = 16 <= age
print(f"Valid age: {valid_age}")

# Applicant must have Texas residency (water bill or electric bill)
water_bill = input("Do you have a water bill? (yes/no): ")
electric_bill = input("Do you have an electric bill? (yes/no): ")
valid_residency = (water_bill.lower() == "yes") or (electric_bill.lower() == "yes")
print(f"Valid residency: {valid_residency}")

# Valid Social Security number
# 9 digits
# must contains only numbers
SSN = input("Enter your social security number: ")
SSN = SSN.replace(" ", "")
SSN = SSN.replace(".", "")
SSN = SSN.replace("-", "")
valid_SSN = (len(SSN) == 9) and (SSN.isnumeric())
print(f"Valid SSN: {valid_SSN}")

# Decision on issuing a driver license
if valid_age and valid_residency and valid_SSN:
    print("You can drive!")
else:
    print("Sorry you cannot drive :(")



"""Enter your age: 12
Valid age: False
Do you have a water bill? (yes/no): YeS
Do you have an electric bill? (yes/no): no
Valid residency: False
Enter your social security number: 318 90 6621"""

