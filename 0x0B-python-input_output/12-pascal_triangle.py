#!/usr/bin/python3
"""Module containing the function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): rows of triangle.

    Returns:
        list: lists of lists of integers.
    """
    if n <= 0:
        return []
    
    pascal = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    return pascal
