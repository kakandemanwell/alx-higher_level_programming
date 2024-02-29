#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []

    for list in matrix:
        squared_lisit = []
        for element in list:
            squared_list.append(element**2)
        squared_matrix.append(squared_list)
    return squared_matrix
