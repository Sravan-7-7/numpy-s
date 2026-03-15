#   the setting an array element with a sequence. the requested array has an inhomogenous shape after 2 dimensions.

#   you can also access the shape uding shape attribute 

# print(arr.shape) --->   this will introduce a tuuple of integers

import numpy as np
arr = np.array([[['A', 'B', 'C'], ['D', 'E', 'F',], ['G', 'H', 'I']],
               [['J', 'K', 'L'], ['M', 'N', 'O'],  ['P', 'Q', 'R']],
               [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '0']]])

print(arr.shape)

# output --->   (3, 3, 3) , the first "3" indicates depth , 
                            #the second "3" indicates no.of rows, 
                            # the third "3" indicates no.of colounms

