'''

Min and Max

'''

#Solution

import numpy as np
n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)],int)

print(np.max(np.min(arr, axis = 1),axis = 0))
