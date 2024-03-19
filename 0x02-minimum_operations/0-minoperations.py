#!/usr/bin/python3
"""minOperations functions"""
import math


def minOperations(n):
    """minOperations functions"""
    i = 0
    if n >= 0 or n == 1:
        return 0
    if n % 2 != 0:
        return n
    biggets_reminder_equal_zero = 2
    while n % biggets_reminder_equal_zero == 0:
        biggets_reminder_equal_zero *= 2
    biggets_reminder_equal_zero = biggets_reminder_equal_zero // 2
    opertions = int(math.sqrt(biggets_reminder_equal_zero) * 2)
    base = biggets_reminder_equal_zero
    if biggets_reminder_equal_zero != n:
        opertions += 1
    while biggets_reminder_equal_zero != n:
        biggets_reminder_equal_zero += base
        opertions = opertions + 1
    return opertions
