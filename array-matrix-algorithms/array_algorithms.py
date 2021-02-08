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


def sort_asc(array):
    arr = array.copy()
    for i in range(len(arr) - 1):
        min_el_index = min_element_partial(arr, i, len(arr) - 1)[1]
        arr[i], arr[min_el_index] = arr[min_el_index], arr[i]
    return arr


def sort_desc(array):
    arr = array.copy()
    for i in range(len(arr) - 1):
        max_el_index = max_element_partial(arr, i, len(arr) - 1)[1]
        arr[i], arr[max_el_index] = arr[max_el_index], arr[i]
    return arr


def sort_min_center(arr):
    result_arr = [0] * len(arr)
    temp_arr = []
    for el in arr:
        temp_arr.append(el)
    if len(arr) % 2 == 1:
        center_index = int(len(arr) / 2)
        min_el = min_element(temp_arr)
        result_arr[center_index] = min_el[0]
        del temp_arr[min_el[1]]
        boundary = center_index + 1
        for i in range(1, boundary):
            min_el_left = min_element(temp_arr)
            result_arr[center_index - i] = min_el_left[0]
            del temp_arr[min_el_left[1]]
            min_el_right = min_element(temp_arr)
            result_arr[center_index + i] = min_el_right[0]
            del temp_arr[min_el_right[1]]
    else:
        left_center_index = int((len(arr) / 2)) - 1
        right_center_index = int(len(arr) / 2)
        boundary = int(len(arr) / 2)
        for i in range(0, boundary):
            min_el_left = min_element(temp_arr)
            result_arr[left_center_index - i] = min_el_left[0]
            del temp_arr[min_el_left[1]]
            min_el_right = min_element(temp_arr)
            result_arr[right_center_index + i] = min_el_right[0]
            del temp_arr[min_el_right[1]]
    return result_arr


def sort_max_center(arr):
    result_arr = [0] * len(arr)
    temp_arr = []
    for el in arr:
        temp_arr.append(el)
    if len(arr) % 2 == 1:
        center_index = int(len(arr) / 2)
        max_el = max_element(temp_arr)
        result_arr[center_index] = max_el[0]
        del temp_arr[max_el[1]]
        boundary = center_index + 1
        for i in range(1, boundary):
            max_el_left = max_element(temp_arr)
            result_arr[center_index - i] = max_el_left[0]
            del temp_arr[max_el_left[1]]
            max_el_right = max_element(temp_arr)
            result_arr[center_index + i] = max_el_right[0]
            del temp_arr[max_el_right[1]]
    else:
        left_center_index = int((len(arr) / 2)) - 1
        right_center_index = int(len(arr) / 2)
        boundary = int(len(arr) / 2)
        for i in range(0, boundary):
            max_el_left = max_element(temp_arr)
            result_arr[left_center_index - i] = max_el_left[0]
            del temp_arr[max_el_left[1]]
            max_el_right = max_element(temp_arr)
            result_arr[right_center_index + i] = max_el_right[0]
            del temp_arr[max_el_right[1]]
    return result_arr


def sort_max_min(arr):
    i = 0
    result_arr = []
    temp_arr = []
    for el in arr:
        temp_arr.append(el)
    while i < len(arr):
        max_el = max_element(temp_arr)
        result_arr.append(max_el[0])
        del temp_arr[max_el[1]]
        i += 1
        if i < len(arr):
            min_el = min_element(temp_arr)
            result_arr.append(min_el[0])
            del temp_arr[min_el[1]]
            i += 1
    return result_arr


def sort_index_even_desc_odd_asc(arr):
    even_elements = []
    odd_elements = []
    result_arr = []
    for i in range(len(arr)):
        if i % 2 == 0:
            even_elements.append(arr[i])
        else:
            odd_elements.append((arr[i]))
    even_elements = sort_desc(even_elements)
    odd_elements = sort_asc(odd_elements)
    boundary = int(len(arr) / 2)
    for i in range(0, boundary):
        result_arr.append(even_elements[i])
        result_arr.append(odd_elements[i])
    if len(arr) % 2 == 1:
        result_arr.append(even_elements[boundary])
    return result_arr
