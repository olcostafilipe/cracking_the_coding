"""
Question 07: Intersection

Given two lists, determine if the two lists intersect. Return
the inter­secting node. Note that the intersection is defined based on reference,
not value. That is, if the kth node of the first linked list is the exact same
node (by reference) as the jth node of the second linked list, then they are
intersecting.
"""

import sys
import random

class Node:
    """
    Values as objects
    """
    def __init__(self, value: int):
        self.value = value


def there_is_intersection(list_1: list, list_2: list) -> Node:
    """
    Function to check if there is intersection between two lists, considering
    references, not values
    """
    for item in list_1:
        if item in list_2:
            return True

    return False


def main(argv):
    # Example of input

    list_1 = [Node(int(x)) for x in argv[0]]
    list_2 = [Node(int(x)) for x in argv[1]]
    dummy_node = Node(1000)  # Node to check intersection

    print("Intersection:", there_is_intersection(list_1, list_2))

    # Add dummy node in list_1
    list_1.append(dummy_node)
    print("Intersection:", there_is_intersection(list_1, list_2))

    # Add dummy node in list_2
    list_2.append(dummy_node)
    print("Intersection:", there_is_intersection(list_1, list_2))

    # Shuffle lists
    random.shuffle(list_1)
    random.shuffle(list_2)
    print("Intersection:", there_is_intersection(list_1, list_2))


if __name__ == '__main__':
    main(sys.argv[1:])
