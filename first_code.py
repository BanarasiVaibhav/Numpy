import numpy as np

x=np.array([1,2,3],np.int16)
print(x)

y=np.array([[1,2,3],[4,5,6]],np.int16)
print(y)


print(y[:,0])
print(y[:,1])
print(y[:,2])

#slicing columnb wise



#checking dimension of array
p=np.eye(13,dtype=np.uint8)
print(p)
print(p.itemsize)
print(p.size)
print(p.shape)
print(p.ndim)

x=np.zeros((3,8)) # no of rows =3 no of columns =8 all entries are '0'
print(x)

y=np.ones((10,10),dtype=np.uint8)
print(y)

z=np.arange(1,101,dtype=np.uint8)
print(z)
print(z.T)


a=np.linspace(1,10,19)
print(a)
