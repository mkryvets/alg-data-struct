from random import randint
from array_algorithms import min_element, max_element, sort_asc
from matrix_algorithms import min_matrix_element, max_matrix_element


def create_3dim_array(length, min_val, max_val):
    dim = []
    for i in range(length):
        dim2 = []
        for j in range(length):
            dim3 = []
            for k in range(length):
                dim3.append(randint(min_val, max_val))
            dim2.append(dim3)
        dim.append(dim2)
    return dim


def print_3dim_array(dim):
    length = len(dim)
    for i in range(0, length):
        for j in range(0, length):
            print(dim[i][j], end=' ')
        print()
    print()


def min_3dim_array_element(dim):
    length = len(dim)
    min_list = []
    for i in range(0, length):
        min_of_the_matrix = min_matrix_element(dim[i])
        min_list.append(min_of_the_matrix)
    min_el = min_element(min_list)[0]
    return min_el

def max_3dim_array_element(dim):
    length = len(dim)
    max_list = []
    for i in range(0, length):
        max_of_the_matrix = max_matrix_element(dim[i])
        max_list.append(max_of_the_matrix)
    max_el = max_element(max_list)[0]
    return max_el


def sort_3dim_array(dim):
    dim_copy = list(map(list, dim))
    length = len(dim_copy)
    # third dim
    for i in range(0, length):
        for j in range(0, length):
            dim_copy[i][j] = sort_asc(dim_copy[i][j])
    return dim_copy
