from random import randint
from array_algorithms import sort_asc, sort_desc, min_element, max_element


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


def min_matrix_element(matrix):
    length = len(matrix)
    min_list = []
    for i in range(0, length):
        min_of_the_row = min_element(matrix[i])[0]
        min_list.append(min_of_the_row)
    min_el = min_element(min_list)[0]
    return min_el

def max_matrix_element(matrix):
    length = len(matrix)
    max_list = []
    for i in range(0, length):
        max_of_the_row = max_element(matrix[i])[0]
        max_list.append(max_of_the_row)
    max_el = max_element(max_list)[0]
    return max_el


def sort_horizontal_asc(matr):
    matrix = list(map(list, matr))
    length = len(matrix)
    for i in range(0, length):
        matrix[i] = sort_asc(matrix[i])
    return matrix


def sort_vertical_asc(matr):
    matrix = list(map(list, matr))
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
    matrix = list(map(list, matr))
    length = len(matrix)
    snake_list = []
    for f in range(0, length):
        for r in range(0, length):
            snake_list.append(matrix[f][r])
    snake_list = sort_asc(snake_list)
    boundary = int(length / 2) + 1
    for k in range(0, boundary):
        if (k != 0):
            for i in range((length - k - 1), (k - 1), -1):
                matrix[i][k - 1] = snake_list.pop(0)
        for j in range(k, length - k):
            matrix[k][j] = snake_list.pop(0)
        if (k == boundary - 1):
            break
        for n in range(k + 1, length - k):
            matrix[n][length - 1 - k] = snake_list.pop(0)
        for m in range((length - 2 - k), (k - 1), -1):
            matrix[length - k - 1][m] = snake_list.pop(0)
    return matrix


def sort_snake_in(matr):
    matrix = list(map(list, matr))
    length = len(matrix)
    snake_list = []
    for f in range(0, length):
        for r in range(0, length):
            snake_list.append(matrix[f][r])
    snake_list = sort_desc(snake_list)
    boundary = int(length / 2) + 1
    for k in range(0, boundary):
        if (k != 0):
            for j in range((length - k - 1), (k - 1), -1):
                matrix[k - 1][j] = snake_list.pop(0)
        for i in range(k, length - k):
            matrix[i][k] = snake_list.pop(0)
        if (k == boundary - 1):
            break
        for m in range(k + 1, length - k):
            matrix[length - 1 - k][m] = snake_list.pop(0)
        for n in range((length - 2 - k), (k - 1), -1):
            matrix[n][length - k - 1] = snake_list.pop(0)
    return matrix


def sort_horizontal_asc_desc(matr):
    matrix = list(map(list, matr))
    length = len(matrix)
    for i in range(0, length):
        if (i % 2 == 0):
            matrix[i] = sort_asc(matrix[i])
        else:
            matrix[i] = sort_desc(matrix[i])
    return matrix


def sort_snake_special(matr):
    matrix = list(map(list, matr))
    length = len(matrix)
    snake_list = []
    for f in range(0, length):
        for r in range(0, length):
            snake_list.append(matrix[f][r])
    snake_list = sort_asc(snake_list)

    if ((length - 1) % 4 != 0):
        flag = True
    else:
        flag = False

    for c in range(0, length - 1, 4):
        for r in range(0, length - 1, 2):
            matrix[r][c] = snake_list.pop(0)
            matrix[r][c + 1] = snake_list.pop(0)
            matrix[r + 1][c + 1] = snake_list.pop(0)
            matrix[r + 1][c] = snake_list.pop(0)
        if flag and (c + 4 >= length - 1):
            break
        for m in range(0, 4):
            matrix[length - 1][c + m] = snake_list.pop(0)
        for r in range(length - 2, 0, -2):
            matrix[r][c + 3] = snake_list.pop(0)
            matrix[r][c + 2] = snake_list.pop(0)
            matrix[r - 1][c + 2] = snake_list.pop(0)
            matrix[r - 1][c + 3] = snake_list.pop(0)
    if flag:
        matrix[length - 1][length - 3] = snake_list.pop(0)
        matrix[length - 1][length - 2] = snake_list.pop(0)
        for i in range(length - 1, -1, -1):
            matrix[i][length - 1] = snake_list.pop(0)
    else:
        for i in range(0, length):
            matrix[i][length - 1] = snake_list.pop(0)
    return matrix
