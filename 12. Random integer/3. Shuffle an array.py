# For shuffling an array...

import numpy as np
rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)
print('\n')
print('-----------------------')
print('\n')

# For random choice...

fruits = np.array(['apple', 'orange', 'banana', 'coconut', 'pineapple'])
fruit = rng.choice(fruits)
print(fruit)


# For mote than one fruit selection...

fruits = rng.choice(fruits, size= (3, 3))   # 3X3 random fruits will be selected...


'''BONOUS POINT: WE CAN ALSO CHOOSE EMOJIES....'''