'''chain indexing is denoted by print(arr[layer][row][coloumn])'''

import numpy as np
arr = np.array([[['A', 'B', 'C'], ['D', 'E', 'F',], ['G', 'H', 'I']],
               [['J', 'K', 'L'], ['M', 'N', 'O'],  ['P', 'Q', 'R']],
               [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '0']]])

print(arr[2][0][0])
print(arr[1][2][2])
print(arr[0][0][0])
print(arr[2][1][0])
print(arr[0][0][0])
print(arr[1][1][1])

''' first square box indicates layer
    second square box indicates row 
    third  squate box indicates coloumn'''
