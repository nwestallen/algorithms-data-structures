# Demonstrates Two Methods of Computing Factorials
import math


# Defining factorials recursively
def rec_fact(n):
    if n == 0:
        return 1
    else:
        return n * rec_fact(n-1)


# Defining factorials iteratively
def it_fact(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result

def test_rec_fact():
    assert rec_fact(4) == 24
