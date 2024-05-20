#!/usr/bin/python3
"""This script divides each number in a matrix by the given number"""
    
    
def matrix_divided(matrix, div):
    """dividing function"""
    
    try:
        for lists in matrix:
            for nums in lists:
                if type(nums) not in [int, float]:
                    e = "matrix must be a matrix (list of lists) of integers/floats"
                    raise TypeError(e)
        for i in range(len(matrix)):
            if len(matrix[i]) != len(matrix[1]):
                e = "Each row of the matrix must have the same size"
                raise TypeError(e)
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError ("division by zero")
        new_matrix = [row[:] for row in matrix]
        for row in new_matrix:
            for i in range(len(row)):
                row[i] = round(row[i] / div, 2)
        return new_matrix
    except (TypeError, ZeroDivisionError) as err: 
        print(err)