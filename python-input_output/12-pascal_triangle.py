#!/usr/bin/python3
""" Defines pascal_triangle """


def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascals triangle """

    if n <= 0:
        return []

    p_triangle = [[1]]
    while len(p_triangle) < n:
        triangle = p_triangle[-1]
        new_row = [1]

        for i in range(len(triangle) - 1):
            new_row.append(triangle[i] + triangle[i + 1])

        new_row.append(1)
        p_triangle.append(new_row)

    return (p_triangle)
