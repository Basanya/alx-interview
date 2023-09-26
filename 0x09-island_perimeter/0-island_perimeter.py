#!/usr/bin/python3
"""0-island_perimeter.py"""


def island_perimeter(grid):
    """Island perimeter"""
    # loop through all the grid
    perimeter = 0
    r, c = len(grid) - 1, len(grid[0]) - 1
    for row in range(len(grid)):
        for j in range(len(grid[row])):
            if grid[row][j] == 1:
                if row == 0 or grid[row - 1][j] == 0:
                    perimeter += 1
                if row == r or grid[row + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[row][j - 1] == 0:
                    perimeter += 1
                if j == c or grid[row][j + 1] == 0:
                    perimeter += 1
    return perimeter
