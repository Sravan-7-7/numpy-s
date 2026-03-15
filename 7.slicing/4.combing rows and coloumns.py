import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

# combing rows and coloumns
print("COMBING ROWS AND COLOUMNS...")
print("-------------------------------")
print(arr[0:2,0:2])
print("\n")
print(arr[0:2,2:])
print("\n")
print(arr[2:,0:2])
print("\n")