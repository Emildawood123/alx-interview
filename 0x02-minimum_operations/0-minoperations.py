#!/usr/bin/python3
"""minOperations functions"""
import math


def minOperations(n):
    """minOperations functions"""
    if n <= 1:
        return 0
    i = 2
    while i < n:
        if n % i == 0:
            remind = i
        i += 1
    try:
        if remind:
            pass
    except Exception:
        return n
    while remind % 2 == 0 and remind != 2:
        remind = remind / 2
    return int((n / remind) + remind)


n = 40
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))