
# ROW SLICING #


'''slicing in python means taking elements from one given imdex to another given index
    1. we pass slice instead of index like this : [start : end]
    2. we can also define the step, like this : [start : end : step]
    3. if we don't start it considered "0" 
    4. if we don't pass end it considered length of array in the dimension 
    5. if we don't pass step it considered as "1"..'''
  
import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

'''print(arr[start:end:step])'''
 
print("ROW SLICING")
print("-------------------")

print(arr[0])
print(" \n") 
print(arr[1])
print(" \n")
print(arr[2])
print(" \n")
print(arr[3])
print(" \n")
print(" \n")

# we can also access reverse by given negetive values (-1, -2, -3, -4)

import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print(arr[0:4:1])
print(" \n")

print(arr[::-1])
print(" \n")
print(arr[::-2])
print(" \n")
print(arr[::-3])

print('----------------------')