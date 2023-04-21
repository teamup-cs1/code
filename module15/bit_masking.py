def clear_all_bits(number):
    """
    The function clears all the bits of a number using the bitwise AND operator
    Any bit ANDed with a zero become a zero
    AND
    0 0 = 0
    0 1 = 0
    1 0 = 0
    1 1 = 1

    Example:
   10101111
AND
   00000000
   ________
   00000000

    @param number:
    @return:
    """
    mask = 0b00000000
    return bin(number & mask)


def clear_4msbits(number):
    """
    This function clears only the 4 most significant bits in a binary number.
    Example:
   10100101
AND
   00001111
   ________
   00000101
    @param number:
    @return:
    """
    mask = 0b00001111
    return bin(number & mask)


def clear_3lsbits(number):
     """
    This function clears only the 3 least significant bits in a binary number.
    Example:
   10100101
    AND
   11111000
   ________
   10100000
    @param number:
    @return:
    """
     mask = 0b11111000
     return bin(number & mask)


def flip_all_bits(number):
    """
        This function flips all bits in a binary number.
        XOR
        0 0 = 0
        0 1 = 1
        1 0 = 1
        1 1 = 0
        Example:
       10100101
        XOR
       11111111
       ________
       01011010
        @param number:
        @return:
        """
    mask = 0b11111111
    return bin(number ^ mask)


def flip_odd_bits(number):
    """
            This function flips all bits in a binary number.
            XOR
            0 0 = 0
            0 1 = 1
            1 0 = 1
            1 1 = 0
            Example:
           10100101
            XOR
           10101010
           ________
           00001111
            @param number:
            @return:
    """
    mask = 0b10101010
    return bin(number ^ mask)


def set_6msbits(number):
    """
        This function sets only the 6 most significant bits in a binary number.
        OR
        0 0 = 0
        0 1 = 1
        1 0 = 1
        1 1 = 1
        Every bit ORed wit a 1 becomes a 1

        Example:
       10100101
        OR
       11111100
       ________
       11111101
        @param number:
        @return:
        """
    mask = 0b11111100
    return bin(number | mask)


def main():
    """
    This program performs bit masking operations
    @return:
    """
    number = int(input("Enter a number in binary: "), 2)
    print(f"{bin(number)[2:]} with all bits cleared is {clear_all_bits(number)}")
    print(f"Clear the 4 most significant bits: {clear_4msbits(number)}")
    print(f"Clear the 3 least significant bits: {clear_3lsbits(number)}")
    print(f"Set the 6 most significant bits: {set_6msbits(number)}")
    print(f"Flit all bits: {flip_all_bits(number)}")
    print(f"Flit odd bits only: {flip_odd_bits(number)}")


main()
