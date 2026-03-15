import numpy as np
arr_1 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

arr_2 = np.array([[1], [2], [3], [4]])

print(arr_1.shape)
print(arr_2.shape)

'print(arr_1 * arr_2)'  # ---> "value error" because operands could not be broadcast together with shapes (2,4) (4,1)...

import numpy as np
arr_1 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

arr_2 = np.array([[1], [2], [3], [4]])

print('-------------------')
print(arr_1.shape)
print(arr_2.shape)
print('-------------------')
print(arr_1 * arr_2)

# these can be broadcast because it has '1' on the coloumn, & same numbers at rows...
