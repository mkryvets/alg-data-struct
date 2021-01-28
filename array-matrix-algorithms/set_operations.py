from random import randint


def create_set(length, min_val, max_val):
    set_as_arr = []
    i = 0
    while i < length:
        rand_val = randint(min_val, max_val)
        if rand_val not in set_as_arr:
            set_as_arr.append(rand_val)
            i += 1
    return set_as_arr


def union(set_as_arr1, set_as_arr2):
    result_set = []
    for val in set_as_arr1:
        result_set.append(val)
    for val in set_as_arr2:
        if val not in result_set:
            result_set.append(val)
    return result_set


def intersection(set_as_arr1, set_as_arr2):
    result_set = []
    for val in set_as_arr1:
        if val in set_as_arr2:
            result_set.append(val)
    return result_set


def absolute_complement(set_as_arr1, inf, sup):
    result_set = []
    for val in range(inf, sup + 1):
        if val not in set_as_arr1:
            result_set.append(val)
    return result_set


def relative_complement(set_as_arr1, set_as_arr2):
    result_set = []
    for val in set_as_arr1:
        if val not in set_as_arr2:
            result_set.append(val)
    return result_set


def symmetric_difference(set_as_arr1, set_as_arr2):
    result_set = []
    union_set = union(set_as_arr1, set_as_arr2)
    inter_set = intersection(set_as_arr1, set_as_arr2)
    for val in union_set:
        if val not in inter_set:
            result_set.append(val)
    return result_set