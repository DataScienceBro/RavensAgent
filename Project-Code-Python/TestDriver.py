import numpy as np
from Agent import interpolateObjectCount

# x = np.asarray([[2, 3, 4], [3, 4, 5], [4, 5, None]], dtype=float)

# results = interpolateObjectCount(x)
# print(results)

# x = np.asarray([[1, 2, 3], [2, 4, 6], [3, 6, None]], dtype=float)

# results = interpolateObjectCount(x)
# print(results)

# x = np.asarray([[0, 2, 4], [2, 3, 4], [4, 4, None]], dtype=float)

# results = interpolateObjectCount(x)
# print(results)

# x = np.asarray([[3, 4, 5], [2, 3, 4], [1, 2, None]], dtype=float)

# results = interpolateObjectCount(x)
# print(results)

x = np.asarray([[2, 2, 2], [2, 1, 2], [2, 2, None]], dtype=float)

results = interpolateObjectCount(x)
print(results)
