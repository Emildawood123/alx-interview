#!/usr/bin/python3
"""moudle"""


def island_perimeter(grid):
    """island_perimeter"""
    res = 0
    for row in range(1, len(grid)):
        for col in range(1, len(grid[row])):
            if grid[row][col] == 1:
                if grid[row - 1][col] == 0:
                    res += 1
                if grid[row][col - 1] == 0:
                    res += 1
                if grid[row + 1][col] == 0:
                    res += 1
                if grid[row][col + 1] == 0:
                    res += 1
                if grid[row][col + 1] == 0 and grid[row + 1][col] == 0:
                    return res
    return 0
