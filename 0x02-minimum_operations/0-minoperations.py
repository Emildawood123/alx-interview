#!/usr/bin/python3
"""minOperations functions"""
import math


def minOperations(n):
    """minOperations functions"""
    if n <= 0 or n == 1:
        return 0
    if True:
        i = 2
        while i < n:
            if n % i == 0:
                print(i)
                remind = i
            i += 1
        try:
            if remind:
                pass
        except Exception:
            return n
        if remind % 2 == 0:
            remind = remind / 2
        return (n / remind) + remind
