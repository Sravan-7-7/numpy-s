# Filtering = refers to the process of selecting elements from an array that match a given condition.

'''by using filtering we can filters out some of this data & create a new array. by taking our original set of data we can filter out
   of out elements that don't match a certain comdition. these use the elements that to match to create a new array...'''

import numpy as np
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]      # ages below '18' where printed...
print(teenagers)
print('-------------------')

'''this is boolean indexing, now pay attention to your shape by using boolean indexing. this will flaatten your 2-D array. 
but there is a way to preserve your shape using the where function...'''

'''this array of teenagers, it's a new array. by filrering out elements & creating a new array, we can preserve the original,
   we still have our original students, the original ages of them...'''

print(ages)    # original array...
print('-------------------')    

adults = ages[ages >= 18]     # ages above '18' where printed...
print(adults)

# But we have 65 and 99, so we use a logical operator...

adults = ages[(ages >= 18) & (ages < 65)]     # ages above '18' and below '65' where printed...
print(adults)

#                                      ''' (or)'''                                                #

adults = ages[(ages >= 18) | (ages < 65)]     # ages above '18' or below '65' where printed...
print(adults)  

# creating another array for seniors...

seniors = ages[ages >= 65]     # ages above '65' where printed...
print(seniors)

# even ages...

even_ages = ages[ages % 2 == 0]     # ages which are even where printed...
print(even_ages)  

# odd ages...  

odd_ages = ages[ages % 2 != 0]     # ages which are odd where printed...
print(odd_ages)
