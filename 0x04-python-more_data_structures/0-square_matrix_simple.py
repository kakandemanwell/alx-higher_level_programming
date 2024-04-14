#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared = []
    for l in matrix:
        squared.append([n**2 for n in l])
    return squared
