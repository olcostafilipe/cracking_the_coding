"""
Question 02: Check permutation
Given two strings, write a method to decide if one is a permutation of the other
"""
import sys

def are_permutation(string_1: str, string_2: str) -> bool:
    return sorted(string_1) == sorted(string_2)


def main(argv):
    string_1 = argv[0]
    string_2 = argv[1]
    print(are_permutation(string_1, string_2))


if __name__ == '__main__':
    main(sys.argv[1:])
