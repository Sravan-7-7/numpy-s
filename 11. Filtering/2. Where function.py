
import numpy as np
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]])

adults = np.where(ages >= 18, ages , 0)     # ages above '18' where printed, otherwise '0' will be printed...
print(adults)

# Any elements that don't match the condition are replaced with our fill value which we set to be '0'...