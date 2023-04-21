"""
Conversions of number
Number systems practice
"""

print(f"Conversion to base 2 (Binary)")
numbers = [23, 357, 12, 86.4, 86]
for number in numbers:
    try:
        print(f"{number} in binary is {bin(number)[2:]}")
    except TypeError:
        print(f"Incorrect type conversion")

print(f"Conversion from base 2 (Binary) to decimal")
numbers = ['1010', '1011', '1100', '1011000101', '10111', '1010110']
for number in numbers:
    try:
        print(int(number, 2)) # The base of 2 means that the first argument is a binary number!
    except TypeError:
        print(f"Incorrect type conversion")

print(f"Conversion from base 16 (Hexadecimal) to decimal")
numbers = ['1010', '1011', '1100', '1011000101', '10111', '1010110', 'ABCDEF', 'DEADBEEF', 'CAFE']
for number in numbers:
    try:
        print(int(number, 16)) # The base of 16 means that the first argument is a Hexadecimal number!
    except TypeError:
        print(f"Incorrect type conversion")

"""
In the hexadecimal system the base is 16.
Numbers (0 to 15): 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

10111 in base 16 = (1*16**0) + (1*16**1) + (1*16*2) + (0*16**3) + (1*16**4)
CAFE in base 16 = (14*16**0) + (15*16**1) + (10*16**2) + (12*16**3)
"""

# Operations on binary numbers
print(f"Bitwise addition of binary numbers")
"""
Rules of binary addition (0, 1)
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10

Add: 1010 + 1011

   1 1
    1010
+ 
    1011
    _____
   10101
"""

# BITWISE operators
# AND, OR, XOR, NOT
# 0 is False, 1 is True

x = 10 # 1010
y = 12 # 1100

"""
AND
0 0 = 0
0 1 = 0
1 0 = 0
1 1 = 1
"""
print(f"AND: {x} & {y} = {x & y}")
print(f"AND: {bin(x)[2:]} & {bin(y)[2:]} = {bin(x & y)[2:]}")

"""
   1010
AND
   1100
   ____
   1000
"""


"""
OR
0 0 = 0
0 1 = 1
1 0 = 1
1 1 = 1
"""
print(f"\nOR: {x} | {y} = {x | y}")
print(f"OR: {bin(x)[2:]} | {bin(y)[2:]} = {bin(x | y)[2:]}")

"""
   1010
OR
   1100
   ____
   1110
"""

"""
XOR
0 0 = 0
0 1 = 1
1 0 = 1
1 1 = 0
"""
print(f"\nXOR: {x} ^ {y} = {x ^ y}")
print(f"XOR: {bin(x)[2:]} ^ {bin(y)[2:]} = {bin(x ^ y)[2:]}")

"""
   1010
OR
   1100
   ____
   0110
"""

"""
NOT (Unary)
0 -> 1
1 -> 0
"""
print(f"\nNOT: {x} -> {~x}")
print(f"NOT: {bin(x)[2:]} -> {bin(~x)}")

"""
NOT 0001010
       ____
    1110101

0101 in 2s complement
flip the bits of 0101 -> 1010
add 1 to 1010 -> 1011 (Which is 11)
so ~(1010) is -11

The computer uses a two's complement format to represent negative number
"""

# Shifting binary
"""
Shift left
x << n
Multiplication by 2^n
"""
x = 12 #1100
# 1100 << 3 ->  1100000
print(f"\n{bin(x)[2:]} << 3 is {bin(x << 3)}")
print(f"{bin(x)[2:]} << 3 is {x << 3}")

"""
Shift right
x >> n
Floor division by 2^n
"""
x = 12 # 1100
# 1100 >> 3 :  0110 -> 0011 -> 0001
print(f"\n{bin(x)[2:]} >> 3 is {bin(x >> 3)}")
print(f"{bin(x)[2:]} >> 3 is {x >> 3}")

x = 25 # 11001
# 11001 >> 3: 00011
print(f"\n{bin(x)[2:]} >> 3 is {bin(x >> 3)}")
print(f"{bin(x)[2:]} >> 3 is {x >> 3}")




