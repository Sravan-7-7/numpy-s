'''Seed :- it use don't set a seed, numpy will create a seed for you. But if you need to reproduce the same results, you can set a seed... 
           for example :- seed = 1.'''

import numpy as np
rng = np.random.default_rng(seed = 1)
print(rng.integers(1,7,size= (3,2)))
print('------------------------------')
print('\n')


'''NOTE: It's kind of like in minecraft. if you use the same world seed as somebody else, you'll have a other copy of the same world
         as your friend setting a seed is useful it you need to reproduce the same results...'''


'''FLOATING POINT NUMBER''' #: A floatingpoint number is a number with the decimal position... 

'''UNIFORM METHOD'''  #: Uniform means uniform disrtibution.Each value has an equal chance of being selected...

print(np.random.uniform(low= -1, high= 1))  # will get a floatingpoint numbers b/w -1 and 1...
print('\n')
print('------------------------------')
# For size

print(np.random.uniform(-1, 1, size= 3))   # 1-D array

print(np.random.uniform(-1, 1, size= (3, 2)))  #2-D array
print('\n')
print('-------------------------')
print('\n')

# Seed using 

np.random.seed(seed = 1)
print(np.random.uniform(-1, 1, size= (3, 2)))   # reduce some values...