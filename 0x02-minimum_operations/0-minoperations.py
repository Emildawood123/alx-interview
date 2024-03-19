"""0-minoperations.py"""


def minOperations(n):
    """minOperations"""
    if n <= 1:
        return 0

    oper = 0
    div = 2

    while n > 1:
        while n % div == 0:
            oper += div
            n //= div
        div += 1

    return oper
