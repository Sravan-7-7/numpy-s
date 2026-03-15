'''using comparision operators we can create boolean arrays, filtered data & use elements-wise comparision...'''

import numpy as np
scores = np.array([91, 87, 77, 66, 50, 100, 35])

print(scores == 100)
print("-----------------------")
print(scores >= 60)
print("-----------------------")

# considering below 60 scores students as '0'.

scores[scores < 60] = 0
print(scores)