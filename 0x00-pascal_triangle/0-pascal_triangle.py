#!/usr/bin/python3
"""
returns list of lists of integers representing Pascal’s triangle
"""


def pascal_triangle(v):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers
    '''
    if v <= 0:
        return []

    triangle = []
    for a in range(v):
        if a == 0:
            triangle.append([1])
        else:
            row = [1]
            prev_row = triangle[a-1]
            for b in range(1, a):
                row.append(prev_row[b-1] + prev_row[b])
            row.append(1)
            triangle.append(row)
    return triangle
