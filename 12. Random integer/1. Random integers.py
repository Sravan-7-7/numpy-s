'''using numpy, you may want to generate random numbers. it's useful for simulations, modeling, applying randon transfermation,
   testinh purpose...'''

# for dice rolling randomly...

import numpy as np 
rng = np.random.default_rng()
print(rng.integers(1, 7))          # randomly generates integer value b/w in range '1' to '6'...

print('-------------------------------')
print('\n')
#  we can also set size for it..

print(rng.integers(1, 7, size= 3))    # randomly generats '3' integers values b/w range '1' to '6'...

print('--------------------------------')
print('\n')

print(rng.integers(1, 7,size=(3, 2)))   # randonly genetates 3X2 array integers 

