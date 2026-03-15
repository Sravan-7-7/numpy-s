import numpy as np
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

print(np.sum(arr, axis=0))  # Sum of each column
print('----------------')
print(np.sum(arr, axis=1))  # Sum of each row