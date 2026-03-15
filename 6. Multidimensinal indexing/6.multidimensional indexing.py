''' as we about chain indexing but with numpy we have accessed something called multidimensinal indexing

----->  multidimensinal indexing is faster than chain indexing 

 ----> we can also print words using multidimensinal indexing..'''

'''multidimensinal indexing is denoted by print(arr[layer,row,coloumn])'''


import numpy as np
arr = np.array([[['A', 'B', 'C'], ['D', 'E', 'F',], ['G', 'H', 'I']],
               [['J', 'K', 'L'], ['M', 'N', 'O'],  ['P', 'Q', 'R']],
               [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '0']]])

word = arr[0,0,0]+arr[2,0,0]+arr[2,0,0]
print(word)