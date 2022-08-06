'''
Eye and Identity

'''

#Solution

import numpy as np
np.set_printoptions(legacy='1.13')
n,p = map(int,input().split())
print(np.eye(n,p))
