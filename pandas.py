import numpy as np
import time
import sys
l=range(1000)
print(sys.getsizeof(5)*len(l))
array=np.arange(1000)
print(array.size*array.itemsize)
a=np.array([(1,2,0),(4,7,6),(7,8,9)])
print(a[0:2,2])
for row in a.flat:
    print("rows is:",row)
b=np.arange(10).reshape(2,5)
c=np.arange(6,12).reshape(2,3)

w=b>6
p=b[w]=-1
print(b)
y=np.hsplit(b,4)
print(y[0])
