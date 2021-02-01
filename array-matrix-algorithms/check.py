from array_algorithms import *
from set_operations import *


test_arr = create_array(200, -1000, 1000)
print('Array: {}'.format(test_arr))
print('Min element of the array: {}, its index: {}'.format(min_element(test_arr)[0], min_element(test_arr)[1]))
print('Max element of the array: {}, its index: {}'.format(max_element(test_arr)[0], max_element(test_arr)[1]))
print('Array sorted in ascending order: {}'.format(sort_asc(test_arr)))
print('Array sorted in descending order: {}'.format(sort_desc(test_arr)))


print('\n')

test_set1 = create_set(10, 0, 20)
print('First set: {}'.format(test_set1))

test_set2 = create_set(10, 0, 20)
print('Second set: {}'.format(test_set2))

print('Union: {}'.format(union(test_set1, test_set2)))
print('Intersection: {}'.format(intersection(test_set1, test_set2)))
print('Absolute complement of the first set: {}'.format(absolute_complement(test_set1, 0, 20)))
print('Relative complement (A\B): {}'.format(relative_complement(test_set1, test_set2)))
print('Symmetric difference: {}'.format(symmetric_difference(test_set1, test_set2)))
