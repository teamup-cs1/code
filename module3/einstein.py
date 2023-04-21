"""
Write a Python program to implement one of Einstein’s favorite puzzles:
1. Enter a 3 digit number. The first and last digit differ by at least two.
e.g. 742 is correct but 244 is not since the first and last digit differ by -2.
2. Reverse the input.
3. Subtract the reversed number from the original number.
4. Reverse the difference.
5. Add the difference to the reversed difference.
6. The sum should be 1089.
"""

# 1. Enter a 3 digit number.
number = int(input("Enter a 3-digit number: "))
hundreds = number // 100
tens = (number % 100) // 10
ones = number % 10
print(f"Number: {number}\nHundreds: {hundreds}\tTens: {tens}\tOnes: {ones}")

# 2. Reverse the input.
reversed = ones*100 + tens*10 + hundreds*1
print(f"The reversed number is : {reversed}")

# 3. Subtract the reversed number from the original number.
difference = number - reversed

# 4. Reverse the difference.
hundreds = difference // 100
tens = (difference % 100) // 10
ones = difference % 10
print(f"Difference: {difference}\nHundreds: {hundreds}\tTens: {tens}\tOnes: {ones}")

reversed_difference = ones*100 + tens*10 + hundreds*1
print(f"The reversed difference is : {reversed}")

# 5. Add the difference to the reversed difference.
einstein_number = difference + reversed_difference
print(f"The Einstein number is {einstein_number}")