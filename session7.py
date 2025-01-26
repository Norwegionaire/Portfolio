# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:23:23 2024

@author: engeb
"""

import numpy as np
"""
import time
a = np.array([2,3,8])

result = 2.1*a

print(result)

starttime = time.time()

my_arr = np.arange(1000000)
#my_arr = list(range(1000000))
print(my_arr)

endtime = time.time()

diff = endtime - starttime

print(diff)

eh = np.array([1, 2, 3.0])

print(eh)

x = [0, 0.5, 1]; y = [-6.1, -2, 1.2]
a = np.array([x,y])

print(a)

b = np.array([1,2,3])
print(b.size)



print(a.shape)

b = np.array([[2,3,8], [4,5,6]])

print(b.shape)

print(len(b))



scalar = np.array(5)

print(a.ndim)
print(len(a))

a = np.array([[1,2,3], [4, 5, 6]], float)

print(a.shape)
print(a.dtype)
print(type(a))

a = np.array([11, 23, 7, 5, 29, 37, 43])

print(a[[2,5,1]])

print(a[1:6:2])

a = np.array((1,2,3,4), float)

print(a)

list1 = [[1,2,3],[4,5,6]]
mat = np.array(list1, complex)

print(mat)
c = np.linspace(0,1,6)
print(c)
d = np.linspace(10,20,6, endpoint = False)
print(d)
X = np.linspace(0, 2*np.pi, 100)
f = np.sin(X)
print(f)

a = np.ones((3, 3)) 
print(a)
arr1 = np.zeros((10,10))
print(arr1)

arr2 = np.ones((4,4))
arr2[2,3], arr2[3,1] = 2, 6

print(arr2)



a = np.linspace(1, 64, 64)
print(a)
a = a.reshape(8, 8)
print(a)
print(np.diag(a))

diag = np.zeros((6,5))
np.fill_diagonal(diag[1:], np.arange(2,7))

f = open("my_diag.txt", "w")

np.savetxt(f, diag, fmt="%.1f")

f.close()

print(diag)


v = np.array([[1.2, 2.5], [3.2, 1.8], [1.1, 4.3]])

b = np.array([True, False, True], dtype=bool)
print(v[b,:])

a = np.array([230, 10, 284, 39, 76])
cutoff = 200
a[a > cutoff] = 0
print(a)

alist = [i for i in range(5)]

print(*alist)
a = np.array([np.arange(6)+10*i for i in np.arange(6)])

print(a)
print()
print(a[0,3:5])
print()
print(a[4:,4:])
print()
print(a[:,2])
print()
print(a[2::2,::2])

a = np.array([[1,2,3], [4,5,6]])
print(a)
b = a.copy()
b[0,0] = 100
print(b)
a = np.loadtxt("matrix.txt", delimiter="\t", dtype=float)
print(a)


a = np.array([1,2,3,4])
print(a + 1)
print(2**a)

b = np.ones(4)+1 
print(a-b)
print(a*b)
"""

a = np.array([[1.2, 2.5],[3.2, 1.8],[1.1,4.3]])

b = np.array([[4.1, 2.6]])
c = np.append(a,b, axis=0)
print(c)

d = np.array([7.8],[6.1],[5.4])
print(np.append(a,d,axis=1))