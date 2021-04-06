"""
Question 02: Return Kth to Last
Implement an algorithm to find the kth to last element of a list.
"""

import random


def kth_to_last(my_list: list, kth_index: int) -> list:
    """ Return the kth to last element of a list """
    return my_list[(kth_index - 1):]


def main():
    # Example of input
    my_list = random.choices(range(20), k=20)
    kth = 13
    print("List:")
    print(my_list)
    print("K-th to end list:")
    print(kth_to_last(my_list, kth))


if __name__ == '__main__':
    main()
