from array_algorithms import *
from set_operations import *


test_set1 = create_set(10, 0, 20)
print('First set: {}').format(test_set1)

test_set2 = create_set(10, 0, 20)
print('Second set: {}').format(test_set2)

print('Union: {}').format(union(test_set1, test_set2))
print('Intersection: {}').format(intersection(test_set1, test_set2))
print('Absolute complement of the first set: {}').format(absolute_complement(test_set1, 0, 20))
print('Relative complement (A\B): {}').format(relative_complement(test_set1, test_set2))
print('Symmetric difference: {}').format(symmetric_difference(test_set1, test_set2))
