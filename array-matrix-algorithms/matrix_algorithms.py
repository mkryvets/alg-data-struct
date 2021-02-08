from random import randint
from array_algorithms import *


def create_matrix(length, min_val, max_val):
    matrix = []
    for i in range(length):
        row = []
        for j in range(length):
            row.append(randint(min_val, max_val))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    length = len(matrix)
    for i in range(0, length):
        for j in range(0, length):
            print(matrix[i][j], end=' ')
        print()
    print()


def sort_horizontal_asc(matr):
    matrix = matr.copy()
    length = len(matrix)
    for i in range(0, length):
        matrix[i] = sort_asc(matrix[i])
    return matrix


def sort_vertical_asc(matr):
    matrix = matr.copy()
    length = len(matrix)
    for j in range(0, length):
        column = []
        for i in range(0, length):
            column.append(matrix[i][j])
        column = sort_asc(column)
        for i in range(0, length):
            matrix[i][j] = column[i]
    return matrix


def sort_snake_out(matr):
    matrix = matr.copy()
    length = len(matrix)
    snake_list = []
    boundary = int(length / 2) + 1
    for k in range(0, boundary):
        if (k != 0):
            for i in range((length - k - 1), (k - 1), -1):
                snake_list.append(matrix[i][k - 1])
        for j in range(0, length - k):
            snake_list.append(matrix[k][j])
        if (k == boundary - 1):
            break
        for m in range(k + 1, length - k):
            snake_list.append(matrix[m][length - 1 - k])
        for n in range((length - 2 - k), (k - 1), -1):
            snake_list.append(matrix[length - k - 1][n])
    snake_list = sort_asc(snake_list)
    l = 0
    for k in range(0, boundary):
        if (k != 0):
            for i in range((length - k - 1), (k - 1), -1):
                matrix[i][k - 1] = snake_list[l]
                l += 1
        for j in range(0, length - k):
            matrix[k][j] = snake_list[l]
            l += 1
        if (k == boundary - 1):
            break
        for i in range(k + 1, length - k):
            matrix[i][length - 1 - k] = snake_list[l]
            l += 1
        for j in range((length - 2 - k), (k - 1), -1):
            matrix[length - k - 1][j] = snake_list[l]
            l += 1
    return matrix



def sort_snake_in(matr):
    matrix = matr.copy()
    length = len(matrix)

    return matrix


def sort_horizontal_asc_desc(matr):
    matrix = matr.copy()
    length = len(matrix)
    for i in range(0, length):
        if (i % 2 == 0):
            matrix[i] = sort_asc(matrix[i])
        else:
            matrix[i] = sort_desc(matrix[i])
    return matrix


def sort_snake_special(matr):
    matrix = matr.copy()
    length = len(matrix)

