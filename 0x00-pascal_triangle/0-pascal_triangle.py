#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """pascal funcation"""
    all = []
    temp = []
    if n <= 0:
        return []
    else:
        for i in range(0, n):
            new = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    new.append(1)
                else:
                    new.append(temp[j] + temp[j - 1])
            temp = new
            print(temp)
            all.append(new)
        return all
