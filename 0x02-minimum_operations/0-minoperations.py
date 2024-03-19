#!/usr/bin/python3
"""minOperations functions"""


def minOperations(n):
    """minOperations functions"""
    if n <= 1:
        return 0
    i = 1
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
        remind /= 2
    while remind % 3 == 0 and remind != 3:
        remind /= 3
    while remind % 5 == 0 and remind != 5:
        remind /= 5
    return int((n / remind) + remind)
