#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []

    for list in matrix:
        squared_matrix.append([element**2 for element in list)
        return squared_matrix
