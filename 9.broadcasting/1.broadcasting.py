'''1. Broadcasting allows numpy to perform operations on arrays.
   2. With different shapes by virually expanding dimensions.
   3. So they match the larger arrays shape.
   4. The dimensions have the same size. 
                (OR)
   5. One of the dimensions has a size of 1.'''

import numpy as np
arr_1 = np.array([[1, 2, 3, 4]])
arr_2 = np.array([[1], [2], [3], [4]])
 
print(arr_1.shape)
print(arr_2.shape)

'''NOTE : For broadcasting we have to follow those two rules, when matching the dimensions they eiether need to be same number (or) one of them has a
          a value of '1'. we read these dimensions to right to left, if these dimensions don't match, but one of then is '1'. the dimensions are 
          compatible with the next setr of dimensions. these dimensions don't match, but ine of them is '1'. so we can broadcast them... '''

print(arr_1 * arr_2)