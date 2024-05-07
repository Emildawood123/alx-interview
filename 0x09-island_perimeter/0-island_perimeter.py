#!/usr/bin/python3
"""Moudle"""


def island_perimeter(grid):
    """island_perimeter"""
    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                res += 4
                if col != 0 and grid[row][col - 1] == 1:
                    res -= 1
                if col != len(grid[row]) - 1 and grid[row][col + 1] == 1:
                    res -= 1
                if row != 0 and grid[row - 1][col] == 1:
                    res -= 1
                if row != len(grid) - 1 and grid[row + 1][col] == 1:
                    res -= 1
    return res
