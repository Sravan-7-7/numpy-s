#   to find the dimension of an array

# zero dimensinal array

import numpy as np
arr = np.array('A')
print(arr.ndim)
print("-------------------")
# "HERE ndim IS NUMBER OF DIMENSIONS "

# one dimensinal array

import numpy as np
arr = np.array(['A', 'B', 'C'])
print(arr.ndim)
print("-------------------")
# two dimensinal array

import numpy as np
arr = np.array([['A', 'B', 'C'],
               ['D', 'E', 'F'],
               ['G', 'H', 'I']])
print(arr.ndim)
print("-------------------")
# three dimensinal array

import numpy as np
arr = np.array([[['A', 'B', 'C'], ['D', 'E', 'F',], ['G', 'H', 'I']],
               [['J', 'K', 'L'], ['M', 'N', 'O'],  ['P', 'Q', 'R']],
               [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '0']]])

print(arr.ndim )
print("-------------------")