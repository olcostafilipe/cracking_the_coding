"""
Question 01: Remove Duplicates
Write code to remove duplicates from an unsorted list.
"""
from collections import defaultdict
import time
import random

def remove_duplicates_o_n2(my_list: list) -> list:
    """ Removing duplicates from a list - Version O(n^2) """ 
    idx = 0
    while idx < len(my_list):
        if my_list[idx] in my_list[:idx]:
            my_list.pop(idx)
        else:
            idx += 1
    return my_list

def remove_duplicates_o_n(my_list: list) -> list:
    """ Removing duplicates from a list - Version O(n) using dicts """ 

    uniques = defaultdict(int)
    idx = 0
    while idx < len(my_list):
        if uniques[my_list[idx]] == 1:
            my_list.pop(idx)
        else:
            uniques[my_list[idx]] = 1
        idx += 1

    return my_list


def main():

    my_list = random.choices(range(50), k=500000)
    print("Lenght of my list: %d elements"  % len(my_list))

    # Calculating time for the approach O(n^2)
    start_time = time.time()
    print(remove_duplicates_o_n2(my_list))
    print("--- %f seconds ---\n" % (time.time() - start_time))

    # Calculating time for the approach O(n)
    start_time = time.time()
    print(remove_duplicates_o_n(my_list))
    print("--- %f seconds ---\n" % (time.time() - start_time))



if __name__ == '__main__':
    main()

