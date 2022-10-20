# Merge sort algorithm

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left = lst[0:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def test_merge():
    list_1 = [4, 5, 6, 7, 8]
    list_2 = [0, 1, 2, 3]
    assert merge(list_1, list_2) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_merge_sort():
    list_3 = [11, 2, 4, 3, 1, 5, 24, 13, 2, -3, 0, 120]
    assert merge_sort(list_3) == [-3, 0, 1, 2, 2, 3, 4, 5, 11, 13, 24, 120]
