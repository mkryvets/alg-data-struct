from random import randint


def create_array(length, min_val, max_val):
    arr = []
    for i in range(length):
        arr.append(randint(min_val, max_val))
    return arr


def min_element(arr):
    min_el = arr[0]
    min_el_index = 0
    for i in range(len(arr)):
        if arr[i] < min_el:
            min_el = arr[i]
            min_el_index = i
    return min_el, min_el_index


def min_element_partial(arr, start, end):
    min_el = arr[start]
    min_el_index = start
    for i in range(start, end + 1):
        if arr[i] < min_el:
            min_el = arr[i]
            min_el_index = i
    return min_el, min_el_index


def max_element(arr):
    max_el = arr[0]
    max_el_index = 0
    for i in range(len(arr)):
        if arr[i] > max_el:
            max_el = arr[i]
            max_el_index = i
    return max_el, max_el_index


def max_element_partial(arr, start, end):
    max_el = arr[start]
    max_el_index = start
    for i in range(start, end + 1):
        if arr[i] > max_el:
            max_el = arr[i]
            max_el_index = i
    return max_el, max_el_index


def sort_asc(arr):
    for i in range(len(arr) - 1):
        min_el_index = min_element_partial(arr, i, len(arr) - 1)[1]
        arr[i], arr[min_el_index] = arr[min_el_index], arr[i]
    return arr


def sort_desc(arr):
    for i in range(len(arr) - 1):
        max_el_index = max_element_partial(arr, i, len(arr) - 1)[1]
        arr[i], arr[max_el_index] = arr[max_el_index], arr[i]
    return arr


def sort_min_center(arr):
    pass


def sort_max_center(arr):
    pass


def sort_max_min(arr):
    pass


def sort_index_even_desc_odd_asc(arr):
    pass
