"""
Question 03: URLify
Write a method to replace all spaces in a string with '%20'. You may assume that
the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
"""
import sys

def urlify(string: str) -> str:
    return string.replace(' ', '%20')

def main(argv):
    string = argv[0]
    print(urlify(string))


if __name__ == '__main__':
    main(sys.argv[1:])
