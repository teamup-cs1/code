# An exception is an error than occurs at runtime

import math
import sys

numbers = [2, 4, 5, 12.5, 0, 3.45, 78, 20203, 'pi', 78, 90]

for num in numbers:
    try:
        inverse = 1 / num
        print(f"The inverse of {num} is: {inverse}")
    except ZeroDivisionError:
        print(f"\nDivision by zero is invalid")
        print(f"You cannot divide 1 by {num} Exception type: {sys.exc_info()}")
    except TypeError:
        print(f"\nDivision by an invalid type")
        print(f"You cannot divide 1 by {num} Exception type: {sys.exc_info()}")
    else:
        print("No Exceptions")
    finally:
        print("Division operation attempted\n")

