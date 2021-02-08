from array_algorithms import *
from set_operations import *
from matrix_algorithms import *


test_arr = create_array(10, -100, 100)
print('Array: {}'.format(test_arr))
print('Min element of the array: {}, its index: {}'.format(min_element(test_arr)[0], min_element(test_arr)[1]))
print('Max element of the array: {}, its index: {}'.format(max_element(test_arr)[0], max_element(test_arr)[1]))
print('Array sorted in ascending order: {}'.format(sort_asc(test_arr)))
print('Array sorted in descending order: {}'.format(sort_desc(test_arr)))
print('Center element is the minimum, left-right elements are ordered by ascending: {}'.format(sort_min_center(test_arr)))
print('Center element is the maximum, left-right elements are ordered by descending: {}'.format(sort_max_center(test_arr)))
print('Maximum-minimum-maximum-minimum...: {}'.format(sort_max_min(test_arr)))
print('Elements with even indices ordered by descending, odd - by ascending: {}'.format(sort_index_even_desc_odd_asc(test_arr)))
print('\n')


test_matrix = create_matrix(11, 0, 9)
print('Matrix:')
print_matrix(test_matrix)
print('Horizontal ascending sort:')
print_matrix(sort_horizontal_asc(test_matrix))
print('Vertical ascending sort:')
print_matrix(sort_vertical_asc(test_matrix))
print('Outer snake sort:')
print_matrix(sort_snake_out(test_matrix))
print('Inner snake sort:')
print_matrix(sort_snake_in(test_matrix))
print('Horizontal rolling asc-desc sort:')
print_matrix(sort_horizontal_asc_desc(test_matrix))


test_set1 = create_set(10, 0, 20)
print('First set: {}'.format(test_set1))
test_set2 = create_set(10, 0, 20)
print('Second set: {}'.format(test_set2))
print('Union: {}'.format(union(test_set1, test_set2)))
print('Intersection: {}'.format(intersection(test_set1, test_set2)))
print('Absolute complement of the first set: {}'.format(absolute_complement(test_set1, 0, 20)))
print('Relative complement (A\B): {}'.format(relative_complement(test_set1, test_set2)))
print('Symmetric difference: {}'.format(symmetric_difference(test_set1, test_set2)))
