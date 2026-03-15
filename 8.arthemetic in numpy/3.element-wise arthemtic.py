'''we have two arrays. Each operation is applied elenent between two arrays....'''

'--> we can apply operations between single elements between two arrays... '

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(arr1 + arr2)   # ADDITION
print("-----------------------")
print(arr1 - arr2)   # SUBTRACTION  
print("-----------------------")
print(arr1 * arr2)   # MULTIPLICATION
print("-----------------------")
print(arr1 / arr2)   # DIVISION
print("-----------------------")
print(arr1 % arr2)   # MODULUS
print("-----------------------")
print(arr1 ** arr2)  # EXPONENTIATION
print("-----------------------")
print(arr1 // arr2)  # FLOOR DIVISION
print("-----------------------")


'''NOTE:  here each operation is applied between two arrays elenment wise...
        i.e, first elenment of arr1 with first elenment of arr2 and so on...'''