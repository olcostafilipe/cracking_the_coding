"""
Question 04: Palindrome Permutation
Given a string, write a function to check if it is a permutation of a
palin­drome. A palindrome is a word or phrase that is the same forwards and
backwards. A permutation is a rearrangement of letters.
"""
import sys
from collections import defaultdict

def is_palindrome_permutation(string: str) -> bool:
    str_dict = defaultdict(int)
    sum_odds = 0 # Variable to control characters with odds occurence numbers
    for char in string:
        str_dict[char] += 1
        if (str_dict[char] % 2) == 0:
            sum_odds -= 1
        else:
            sum_odds += 1

    return sum_odds <= 1


def main(argv):
    string = argv[0]
    print(is_palindrome_permutation(string))


if __name__ == '__main__':
    main(sys.argv[1:])
