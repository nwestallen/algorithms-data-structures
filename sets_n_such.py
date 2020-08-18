# The powerset of a set returns all possible subsets

def powerset_loop(oset):
    pset = [[]]
    for member in oset:
        for subset in pset.copy():
            newset = subset.copy()
            newset.append(member)
            pset.append(newset)
    return pset


def powerset_recursive(lst):
    if len(lst) == 0:
        return [lst]
    else:
        return [lst] + powerset_recursive(lst[1:])


def powerset_matrix(oset):
    lent = len(oset)
    frmt = '0' + str(lent) + 'b'
    digits = 2**lent
    return [[int(j) for j in list(str(format(i, frmt)))] for i in range(digits)]


my_set = [1, 2, 3]
print(powerset_recursive(my_set))
# print(recpend(my_set))
