"""
Question 05: Sum lists

You have two numbers represented by a linked list, where each node contain a
single digit. Write a function that adds the two numbers and returns the sum as
a linked list.

Example
Input:[4, 5, 8, 2] + [8, 7, 5]. That is, 4582 + 875.
Output: [5, 4, 5, 7]. That is, 5457.

"""

import sys


def sum_lists(list_1: list, list_2) -> list:
    biggest = list_1 if len(list_1) > len(list_2) else list_2
    smallest = list_1 if list_1 != biggest else list_2
    output = []

    idx_b = len(biggest) - 1
    idx_s = len(smallest) - 1
    while idx_b >= 0:
        if idx_s >= 0:
            sum_digit = biggest[idx_b] + smallest[idx_s]
            last_sum_digit = sum_digit - (sum_digit // 10) * 10
            offset = sum_digit // 10
            output.insert(0, last_sum_digit)
            idx_b -= 1
            idx_s -= 1
            biggest[idx_b] += offset

        else:
            sum_digit = biggest[idx_b]
            last_sum_digit = sum_digit - (sum_digit // 10) * 10
            offset = sum_digit // 10
            output.insert(0, last_sum_digit)
            idx_b -= 1
            biggest[idx_b] += offset

    if idx_b < 0 and offset > 0:
        output.insert(0, offset)

    return output


def main(argv):
    # Example of input

    first_number = [int(char) for char in argv[0]]
    second_number = [int(char) for char in argv[1]]

    # idx_to_part = random.choice(range(20))
    print("Input :", first_number, second_number)
    print("Output :", sum_lists(first_number, second_number))


if __name__ == '__main__':
    main(sys.argv[1:])
