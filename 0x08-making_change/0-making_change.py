#!/usr/bin/python3
"""moudle to solve makeChange"""


def makeChange(coins, total):
    """makeChange method"""
    count = 0
    coins.sort()
    coins.reverse()
    for i in coins:
        if total == 0:
            return count
        while i <= total:
            total -= i
            count += 1
    return -1
