#!/usr/bin/python3
"""minOperations functions"""
import math


def minOperations(n):
    """minOperations functions"""
    if n <= 1:
        return 0
    i = 3
    while i < n:
        if n % i == 0:
            remind = i
        i += 2
    try:
        if remind:
            pass
    except Exception:
        return n
    while remind % 3 == 0 and remind / 3 != 1:
        remind = remind / 3
    return int((n / remind) + remind)
