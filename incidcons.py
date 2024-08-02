import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr = np.pad(arr, (2, 1), mode='constant', align='center')
print(arr)
