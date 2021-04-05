"""
Question 07: Loop Detection

Given a circular list, implement an algorithm that returns the node at the 
beginning of the loop.

Definition - Circular list: A (corrupt) linked list in which a node's next
pointer points to an earlier node, so as to make a loop in the linked list.

EXAMPLE
Input:
Output:
A -> B -> C -> D -> E -> C [the same C as earlier]
C
"""

import sys
import random


class Node:
    """
    Values as objects
    """

    def __init__(self, value: int):
        self.value = value

    def get_value(self):
        return self.value


def check_loop(list_1: list) -> Node:
    """
    Function to check if there is a loop in a list and return the beginning of
    it. A loop is defined by the same node referenced twice in a list.
    """
    for idx, item in enumerate(list_1):
        if item in list_1[:idx]:
            return item

    return None


def main():
    # Creating example of input
    list_1 = [Node(int(x)) for x in range(20)]
    random.shuffle(list_1)
    list_1.append(list_1[7])  # Node to check intersection

    # Printing values
    # NOTE: The references of list_1[7] and list_1[-1] are exactly the same
    print([item for item in list_1])
    print([item.get_value() for item in list_1])

    loop = check_loop(list_1)
    if loop:
        print("Loop Node value:", loop.value)
    else:
        print("There is no loop")

    # You can change the value of list_1[-1], but the reference still remains
    # the same, which implies in also changing the value of list_1[7], in this
    # example.
    list_1[-1].value = 1000
    print([item for item in list_1])
    print([item.get_value() for item in list_1])

    loop = check_loop(list_1)
    if loop:
        print("Loop Node value:", loop.value)
    else:
        print("There is no loop")


if __name__ == '__main__':
    main()
