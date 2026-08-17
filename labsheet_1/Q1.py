# Q1. Implement Push and Pop operations on a NumPy array.
import numpy as np
arr = np.array([1, 2, 3])
# Push
arr = np.append(arr, 4)
print("\nAfter push:", arr)
# Pop
arr = np.delete(arr, -1)
print("After pop:", arr)