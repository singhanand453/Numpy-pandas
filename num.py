import numpy as np
x=np.arange(6).reshape(3,2)
y=np.savetxt("singh.txt",x)
print(y)
print(x)
dt=np.dtype(np.int32,copy=True,align=True)
print(dt)
a=np.arange(10)
print(a.flags)
p=np.zeros([3,3],dtype=np.int32,order='C')
print(p)
q=[1,2,3,4,5,6,7]
r=np.asarray(q)
print(r)
