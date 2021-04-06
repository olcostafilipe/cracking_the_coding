"""
Question 03: Delete Middle Node
Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a list,
given only access to that node.

EXAMPLE
Input:the node c from the list [a, b, c, d, e, f]
Result: [a, b, d, e, f]
"""

import random

def delete_middle(my_list: list, idx: int) -> list:
    """ Delete element in the middle of the list """
    if idx != 0 and idx != len(my_list) -1:
        my_list.pop(idx)
    else:
        print("Cannot remove first or last element")

    return my_list


def main():
    # Example of input
    my_list = random.choices(range(25), k=25)
    idx_to_remove = random.choice(range(len(my_list)))
    print("List  :", my_list)
    print("Index to remove:", idx_to_remove)
    print("Output:", delete_middle(my_list, idx_to_remove))


if __name__ == '__main__':
    main()
