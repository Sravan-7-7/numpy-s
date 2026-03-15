'''1. Aggregate functions = Summarize data & typically return a single value.
   2. We use same data to work with it.'''

import numpy as np
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

print(np.sum(arr))            #55
print('------------------')
print(np.mean(arr))         #5.5
print('------------------') 
print(np.std(arr))          #2.8722813232690143 # Standard Deviation it measures of spread within the data..
print('------------------') 
print(np.var(arr))          #8.25  # Variance, it is the square of the stabdard deviation..
print('------------------')
print(np.min(arr))          #1
print('------------------')
print(np.max(arr))          #10
print('------------------')
print(np.argmin(arr))       #0  # for position of min value..
print('------------------')
print(np.argmax(arr))       #9  # for position of max value..
print('------------------')


