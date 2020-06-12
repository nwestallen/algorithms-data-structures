# The powerset of a set returns all possible subsets

def powerset(oset):
    pset = [[]]
    for member in oset:
        for subset in pset.copy():
            newset = subset.copy()
            newset.append(member)
            pset.append(newset)
    return pset


my_set = [1, 2, 3]

print(powerset(my_set))
