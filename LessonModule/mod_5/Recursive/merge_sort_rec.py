"""

We rewrite merge_sort using recursion and compare to the 
iterative version. The recursive version is natural to write 
and does not require a list/loop to maintain sublists. As a 
result, it is slightly more efficient.

"""


import time
import random


def time_function(L, func):
    """
    Illustrates how you can send a function as an argument
    to another function as well. Runs the function called func,
    and returns the time.

    """

    L1 = list(L)
    start = time.time()
    func(L1)
    end = time.time()
    print("Method: {:s} took {:f} seconds".format((func.__name__).ljust(20), end - start))


def merge(L1, L2):
    """
    Assume L1 and L2 are sorted.
    Create a new list L that is the merged
    version of L1&L2.

    This is the efficient version of merge
    that does not modify the input lists, as pop 
    is costly, even though it is a constant time operation.

    """

    L = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            val = L1[i]
            L.append(val)
            i += 1
        else:
            val = L2[j]
            L.append(val)
            j += 1
    ## at this point, either L1 or L2 has run out of values
    ## add all the remaining values to the end of L.
    L.extend(L1[i:])
    L.extend(L2[j:])
    return L


    
def merge_sort_iterative(L):
    """
    Complexity: O(n* log n)
    See earlier version of this code for explanation.

    """

    L1 = []
    for val in L:
        L1.append([val])

    while len(L1) > 1:
        L2 = []
        for i in range(0, len(L1) - 1, 2):
            Lmerged = merge(L1[i], L1[i + 1])
            L2.append(Lmerged)

        if len(L1) % 2 == 1:
            L2.append(L1[-1])
        L1 = L2
    return L1[0]


def merge_sort_recursive(L):
    """ Complexity: O(n logn)
        The function calls itself recursively logn times,
        and each time about n elements are merged.

    """

    if len(L) == 1:
        return L

    length = len(L)
    mid = length // 2
    left = merge_sort_recursive(L[:mid])
    right = merge_sort_recursive(L[mid:])
    return merge(left, right)

if __name__ == "__main__":
    ##Testing code
    k = 100000
    L = list(range(k))
    random.shuffle(L)
    
    time_function(L, merge_sort_iterative)
    time_function(L, merge_sort_recursive)
    time_function(L, list.sort)

