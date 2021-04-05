"""
Question 06: Palindrome

Inplement a function to check if a list is a palindrome
"""

import sys


def is_palindrome(values: list) -> bool:
    """
    Function to check if a list of values is a palindrome
    """
    begin, end = [0, len(values) - 1]
    while begin < end:
        if values[begin] != values[end]:
            return False
        begin, end = [begin + 1, end - 1]

    return True


def main(argv):
    # Example of input

    values = argv[0]
    # idx_to_part = random.choice(range(20))
    print("Input :", values)
    print("Is Palindrome? ", is_palindrome(values))


if __name__ == '__main__':
    main(sys.argv[1:])
