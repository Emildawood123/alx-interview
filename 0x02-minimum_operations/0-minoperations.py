#!/usr/bin/python3
"""minOperations functions"""
from sympy import isprime

def minOperations(n):
    """minOperations functions"""
    if n <= 1:
        return 0
    i = 0
    while i < n:
        if not isprime(i):
            pass
        elif n % i == 0:
            remind = i
        i += 1
    try:
        if remind:
            pass
    except Exception:
        return n
    return int((n / remind) + remind)

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))