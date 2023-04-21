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
number = input("Enter a 3 digit number: ")
# 2. Reversal
reversed_number = number[::-1]
# 3. Subtract the reversed number from the original number.
difference = int(number) - int(reversed_number)
# 4. Reverse the difference.
reversed_difference = str(difference)[::-1]
# 5. Add the difference to the reversed difference.
einstein = difference + int(reversed_difference)

print(f"The einstein number is {einstein}")
