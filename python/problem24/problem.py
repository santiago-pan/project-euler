import time
import itertools
permutations = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
value = permutations[999999]
valueStr = (''.join([str(x) for x in value]))
print(valueStr)