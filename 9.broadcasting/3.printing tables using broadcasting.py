import numpy as np
arr_1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
arr_2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(arr_1.shape)          #(1, 10)
                                        # this can be broadcast because it has '1' on the row, & same numbers at coloumns...
print(arr_2.shape)          #(10, 1)

print(arr_1 * arr_2)