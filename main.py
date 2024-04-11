# Boolean index did not match indexed array along dimension 0

import numpy as np

array = np.array([1, 2, 3, 4])

bool_array = np.array([True, False, True, False])

print(array[bool_array])  # 👉️ [1 3]