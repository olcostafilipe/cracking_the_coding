"""
Question 09: String Rotation
Assume you have a method 'isSubstringwhich' checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a
rotation of s1 using only ONE CALL to isSubstring.
E.g., 'waterbottle' is a rotation of 'erbottlewat'.
"""

import sys

def is_substring(string_01: str, string_02: str) -> bool:
    return string_01 in string_02

def string_rotation(string_01: str, string_02: str) -> bool:
    if len(string_01) != len(string_02):
        return False

    double_string_01 = string_01 + string_01
    return is_substring(string_02, double_string_01) # ONLY ONE CALL!!


def main(argv):
    string_1 = argv[0]
    string_2 = argv[1]
    print(string_rotation(string_1, string_2))


if __name__ == '__main__':
    main(sys.argv[1:])
