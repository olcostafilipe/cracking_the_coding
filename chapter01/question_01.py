"""
Question 01: Implement an algorithm to determine if a string has all unique
characters. You cannot use additional data structures?
"""
import sys


def all_unique(string: str) -> bool:
    sorted_string = sorted(string)
    for idx in range(1, len(sorted_string)):
        if sorted_string[idx] == sorted_string[idx - 1]:
            return False
    return True


def main(argv):
    string = argv[0]
    print(all_unique(string))


if __name__ == '__main__':
    main(sys.argv[1:])
