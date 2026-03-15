'''a vector is another linear algbra term, a vector is a single dimensinal, such as 1-D list, whereas in a scalar is a single value,
   using vectorised math functions we can apply a function to an entire array without writing a loop...'''

'''---> we can access the library of np,which is numpy, called the sqrt function . pass in an array...'''

import numpy as np
arr = np.array([1, 2, 3.94])
print(np.sqrt(arr))           # SQUARE ROOT
print("-------------------")

print(np.round(arr))          # ROUNDING THE VALUES
print("-------------------")    

print(np.floor(arr))          # FLOORING THE VALUES 
print("-------------------")

print(np.ceil(arr))           # CEILING THE VALUES  
print("-------------------")    


# SQUARE ROOT: find the values for sqrt

# ROUNDING: find (or) given approx nearest integer value not float

# FLOORING: gives out before decimal number 

# CEILING: give one number greater while in float


'there are some built in functions like "pi"'

print(np.pi)                  # PI VALUE
print("-------------------")    


# for example: area of circle = pi * r^2

import numpy as np
radii = np.array([1, 2, 3])

print(np.pi * radii**2)   # AREA OF CIRCLE
print("-------------------")    