#!/usr/bin/python3
"""alx interview question on Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle
    of n

    Args:
        n (n): size of triangle

    Returns:
        list: returns empty list if n <= 0 or list of lists of integers
        representing Pascal's triangle of n otherwise
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
            triangle.append(row)

    return triangle
