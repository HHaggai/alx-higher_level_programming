#!/usr/bin/python3
"""Defynes a Pascal's Triangl functn."""


def pascal_triangle(n):
    """Rprsnt Pascal's Triangl of size n.

    Retrns a list of lists of intgrs reprsnting the triangl.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
