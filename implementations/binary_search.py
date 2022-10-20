from typing import List

#find the index of a value in a sorted list in O(log n) time
def binary_search_itr(lst: List, val: int) -> int:
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (high + low) // 2
        if lst[mid] > val:
            high = mid - 1
        elif lst[mid] < val:
            low = mid + 1
        else:
            return mid
    return -1

list1 = [-4, -2, 0, 3, 5, 8, 12, 13]

def test_search_match():
    assert binary_search_itr(list1, 12) == 6

def test_search_no_match():
    assert binary_search_itr(list1, 7) == -1