#!/usr/bin/python3
"""minOperations functions"""
import math


def minOperations(n: int) -> int:
    """minOperations functions"""
    if n <= 0 or n == 1:
        return 0
    if n % 2 != 0:
        b_r_e_z: int = 3
        while n % b_r_e_z != 0 and b_r_e_z != n:
            b_r_e_z += 1
        operations: int = b_r_e_z
        base: int = b_r_e_z
        if n == b_r_e_z:
            return n
        while n != b_r_e_z:
            operations += 1
            b_r_e_z += base
        return operations
    biggets_reminder_equal_zero: int = 2
    while n % biggets_reminder_equal_zero == 0:
        biggets_reminder_equal_zero *= 2
    biggets_reminder_equal_zero = biggets_reminder_equal_zero // 2
    opertions: int = int(math.sqrt(biggets_reminder_equal_zero) * 2)
    base = biggets_reminder_equal_zero
    if biggets_reminder_equal_zero != n:
        opertions += 1
    while biggets_reminder_equal_zero != n:
        biggets_reminder_equal_zero += base
        opertions = opertions + 1
    return opertions
