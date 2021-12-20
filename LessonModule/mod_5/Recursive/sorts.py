"""

Implementation of a variety of sorting algorithms, including
.  Selection Sort,
.  Insertion Sort
.  Merge Sort

The main code gives tests for these functions.
"""


def sel_sort(v):
    """
    Sort based on the O(N^2) selection sort algorithm.  The ideas is
    discussed in the text book.  Students are not responsible for
    knowing this algorithm.
    """
    for i in range(0, len(v) - 1):
        k = i
        for j in range(i + 1, len(v)):
            if v[j] < v[k]:
                k = j
        v[i], v[k] = v[k], v[i]


def ins_sort(v):
    """
    The Insertion Sort algorithm
    """
    for i in range(1, len(v)):
        j = i - 1
        x = v[i]
        while j >= 0 and x < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = x


def merge(L1, L2):
    """
    Merge the contents of two lists, each of which is already sorted
    into a single sorted list.
    """
    i1 = 0
    i2 = 0
    L = []
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1
    L.extend(L1[i1:])
    L.extend(L2[i2:])
    return L


def merge_sort(v):
    """
    Implementation of the merge sort algorithm.
    """
    if len(v) <= 1:
        return

    lists = []
    for item in v:
        lists.append([item])

    i = 0
    while i < len(lists) - 1:
        new_list = merge(lists[i], lists[i + 1])
        lists.append(new_list)
        i += 2

    v[::] = lists[-1]




if __name__ == "__main__":

    v =  [10, 5, 3, 2, -4]
    ins_sort(v)
    print(v)
    v = []
    ins_sort(v)
    print(v)
    v = [5, 6, 7, 6, 5, 5]
    ins_sort(v)
    print(v)



    v1 = [26, 35, 145]
    v0 = [0, 0, 9, 9, 9.4, 9.6, 15, 21]
    print(v0)
    print(v1)
    print(merge(v0, v1))


    v = [9.1, 17.5, 9.8, 6.3, 12.4, 1.7]
    merge_sort(v)
    print(v)
