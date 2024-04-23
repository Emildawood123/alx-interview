#!/usr/bin/python3
"""rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix"""
    whole_list = []
    for i in range(len(matrix)):
        part = []
        for lst in matrix:
            part.append(lst[i])
        part.reverse()
        whole_list.append(part)
    for i in range(len(matrix)):
        matrix[i] = whole_list[i]
