
print("COLOUMN SLICING")
print("-------------------") 

# COLOUMN SLICING #

import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

# print(arr[ ,0]) ----> [row , coloumn]

# print syntax error to avoid syntax error give ":" , ","

print(arr[:,0])
print("\n")
print(arr[:,1])
print("\n")
print(arr[:,2])
print("\n")
print(arr[:,3])
print("\n")
print(arr[:,-1])
print("\n")

