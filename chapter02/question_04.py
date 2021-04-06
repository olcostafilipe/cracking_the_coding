"""
Question 04: Partition

Write code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x. If x is contained
within the list, the values of x only need to be after the elements less than x
(see below). The partition element x can appear anywhere in the "right
partition"; it does not need to appear between the left and right partitions.

Example:

Partition: 15
Input : [6, 14, 6, 7, 14, 17, 16, 19, 14, 16, 14, 19, 7, 15, 14]
Output: [6, 14, 6, 7, 14, 14, 7, 14, 14, 16, 19, 19, 16, 15, 17]
        |------------- < 15 -----------| |------- >= 15 -------|

"""

import random


def partition(my_list: list, part: int) -> list:
    """ Function which performs Partition  """
    begin = 0
    end = len(my_list) - 1
    while begin < end:
        check_lower = my_list[begin] < part
        check_higher = my_list[end] >= part

        if not check_lower and not check_higher:
            # Swap
            my_list[begin], my_list[end] = my_list[end], my_list[begin]
        else:
            if check_lower:
                begin += 1
            if check_higher:
                end -= 1

    return my_list


def main():
    # Example of input
    my_list = random.choices(range(20), k=15)
    idx_to_part = random.choice(range(20))
    print("Partition:", idx_to_part)
    print("Input :", my_list)
    print("Output:", partition(my_list, idx_to_part))


if __name__ == '__main__':
    main()
