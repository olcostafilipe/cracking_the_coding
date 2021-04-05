"""
Question 05: One Away
There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write
a function to check if they are one edit (or zero edits) away.
"""
import sys

def is_one_away(string_1: str, string_2: str) -> bool:

    # Check difference of strings lenght
    if abs(len(string_1) - len(string_2)) > 1:
        return False

    str_B = string_1 if len(string_1) > len(string_2) else string_2
    str_S = string_1 if str_B != string_1 else string_2

    idx_s = 0
    idx_b = 0
    found_diff = False

    while idx_b < len(str_B) and idx_s < len(str_S):
        # If same characters, wall on the strings
        if str_S[idx_s] != str_B[idx_b]:
            if found_diff:
                return False

            found_diff = True
            if len(str_S) == len(str_B):
                idx_s += 1

        else:
            idx_s += 1

        idx_b += 1

    return True


def main(argv):
    string_1 = argv[0]
    string_2 = argv[1]
    print(is_one_away(string_1, string_2))


if __name__ == '__main__':
    main(sys.argv[1:])
