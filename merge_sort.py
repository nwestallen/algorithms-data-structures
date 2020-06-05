# Merge sort algorithm

list_1 = [4, 5, 6, 7, 8]
list_2 = [0, 1, 2, 3]


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


list_1 = [4, 5, 6, 7, 8]
list_2 = [0, 1, 2, 3]

print(merge(list_1, list_2))
