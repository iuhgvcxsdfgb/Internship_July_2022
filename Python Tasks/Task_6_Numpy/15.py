'''

Shape and Reshape


'''

#Solution

import numpy
def reshape_arr(arr):
    arr = numpy.array(arr,int)
    return numpy.reshape(arr,(3,3))

arr = input().strip().split(' ')
print(reshape_arr(arr))
